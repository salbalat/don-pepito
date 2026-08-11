"""Don Pepito — API en tiempo real (Fase 1, prototipo).

Estado EN MEMORIA (suficiente para el piloto): posición del barco + cola de pedidos + carta.
Sirve la PWA (../web) y expone /api/*. Para la nube (Fase 2) se cambia por Firebase/Supabase.

Arrancar:
    uvicorn app:app --host 0.0.0.0 --port 5700     (desde backend/)
"""
from __future__ import annotations

import math
import time
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

WEB = Path(__file__).resolve().parent.parent / "web"
SPEED_KMH = 12.0          # velocidad de crucero del barco (ajustable)
SERVICE_MIN = 3           # minutos de servicio por pedido en cola (por delante)

# --- Carta (cócteles + refrescos + algo de picar) ---
MENU = [
    {"id": "mojito", "cat": "cóctel", "name": "Mojito", "price": 8.0, "emoji": "🍸"},
    {"id": "mojito-fresa", "cat": "cóctel", "name": "Mojito de fresa", "price": 8.5, "emoji": "🍓"},
    {"id": "pinacolada", "cat": "cóctel", "name": "Piña colada", "price": 9.0, "emoji": "🍍"},
    {"id": "gintonic", "cat": "cóctel", "name": "Gin-tonic", "price": 9.0, "emoji": "🍋"},
    {"id": "sangria", "cat": "cóctel", "name": "Sangría (copa)", "price": 6.0, "emoji": "🍷"},
    {"id": "cerveza", "cat": "refresco", "name": "Cerveza", "price": 4.0, "emoji": "🍺"},
    {"id": "refresco", "cat": "refresco", "name": "Refresco", "price": 3.0, "emoji": "🥤"},
    {"id": "agua", "cat": "refresco", "name": "Agua", "price": 2.0, "emoji": "💧"},
    {"id": "patatas", "cat": "picar", "name": "Patatas fritas", "price": 4.0, "emoji": "🍟"},
    {"id": "nachos", "cat": "picar", "name": "Nachos", "price": 6.0, "emoji": "🧀"},
]
MENU_BY_ID = {m["id"]: m for m in MENU}

# Arroces del día (carta real): ración 18 € · refresco de la ración +2 € (= 20 € con refresco).
ARROCES = {
    "arroz-senoret": "Arroz del señoret",
    "fideua-secreto": "Fideuá de secreto ibérico y pimiento rojo a la llama",
    "fideua-senoret": "Fideuá del señoret",
    "arroz-pato": "Arroz de pato y setas",
    "fideua-negra": "Fideuá negra con gambón y calamar",
    "arroz-negro": "Arroz negro con gambón y calamar",
    "fideua-pato": "Fideuá de pato y setas",
    "paella-valenciana": "Paella Valenciana",
}
for _id, _name in ARROCES.items():
    MENU_BY_ID[_id] = {"id": _id, "cat": "arroz", "name": _name, "price": 18.0, "emoji": "🥘"}
MENU_BY_ID["racion-refresco"] = {"id": "racion-refresco", "cat": "arroz",
                                 "name": "Refresco con tu ración (+2 €)", "price": 2.0, "emoji": "🥤"}

# Estado en memoria
BOAT = {"lat": None, "lng": None, "speed": SPEED_KMH, "updated": 0.0}
ORDERS: list[dict] = []
_seq = {"n": 0}


def _haversine_km(a_lat, a_lng, b_lat, b_lng) -> float:
    R = 6371.0
    p1, p2 = math.radians(a_lat), math.radians(b_lat)
    dp = math.radians(b_lat - a_lat)
    dl = math.radians(b_lng - a_lng)
    h = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * R * math.asin(min(1.0, math.sqrt(h)))


def _pending():
    return [o for o in ORDERS if o["status"] != "entregado"]


def _eta_min(order) -> int | None:
    """Tiempo estimado: viaje del barco al cliente + cola por delante."""
    if BOAT["lat"] is None or order.get("lat") is None:
        return None
    dist = _haversine_km(BOAT["lat"], BOAT["lng"], order["lat"], order["lng"])
    travel = dist / max(1.0, BOAT["speed"]) * 60.0
    pend = _pending()
    ahead = next((i for i, o in enumerate(pend) if o["id"] == order["id"]), 0)
    return max(1, round(travel + ahead * SERVICE_MIN))


def _queue_pos(order) -> int:
    pend = _pending()
    return next((i + 1 for i, o in enumerate(pend) if o["id"] == order["id"]), 0)


def _public(o) -> dict:
    return {**{k: o.get(k) for k in ("id", "name", "items", "lat", "lng", "status", "total",
                                     "created", "color", "photo")},
            "eta_min": _eta_min(o), "queue_pos": _queue_pos(o)}


app = FastAPI(title="Don Pepito API")


@app.middleware("http")
async def _no_cache(request, call_next):
    resp = await call_next(request)
    resp.headers["Cache-Control"] = "no-store"
    return resp


@app.get("/api/menu")
async def menu():
    return {"menu": MENU}


@app.get("/api/state")
async def state():
    """Todo lo que necesita el cliente y el barco: posición del barco + cola."""
    return {"boat": BOAT, "orders": [_public(o) for o in ORDERS], "menu": MENU,
            "pending": len(_pending())}


class BoatIn(BaseModel):
    lat: float
    lng: float
    speed: float | None = None


@app.post("/api/boat")
async def set_boat(b: BoatIn):
    BOAT.update(lat=b.lat, lng=b.lng, updated=time.time())
    if b.speed:
        BOAT["speed"] = b.speed
    return {"ok": True, "boat": BOAT}


class OrderItem(BaseModel):
    id: str
    qty: int = 1


class OrderIn(BaseModel):
    name: str = ""
    items: list[OrderItem] = []
    lat: float | None = None
    lng: float | None = None
    color: str | None = None          # color del barco del cliente (opcional)
    photo: str | None = None          # foto pequeña del barco en data-URL (opcional)


@app.post("/api/order")
async def create_order(o: OrderIn):
    items, total = [], 0.0
    for it in o.items:
        m = MENU_BY_ID.get(it.id)
        if not m or it.qty <= 0:
            continue
        items.append({"id": m["id"], "name": m["name"], "qty": it.qty,
                      "price": m["price"], "emoji": m["emoji"]})
        total += m["price"] * it.qty
    if not items:
        return JSONResponse({"error": "sin_items", "mensaje": "El pedido está vacío."}, status_code=400)
    _seq["n"] += 1
    photo = o.photo if (o.photo and len(o.photo) < 40_000) else None
    order = {"id": _seq["n"], "name": (o.name or "").strip() or f"Pedido {_seq['n']}",
             "items": items, "lat": o.lat, "lng": o.lng, "status": "pendiente",
             "total": round(total, 2), "created": time.time(),
             "color": o.color, "photo": photo}
    ORDERS.append(order)
    return {"ok": True, **_public(order)}


@app.get("/api/order/{oid}")
async def get_order(oid: int):
    o = next((x for x in ORDERS if x["id"] == oid), None)
    if not o:
        return JSONResponse({"error": "no_existe"}, status_code=404)
    return _public(o)


class StatusIn(BaseModel):
    status: str


@app.delete("/api/order/{oid}")
async def cancel_order(oid: int):
    o = next((x for x in ORDERS if x["id"] == oid), None)
    if not o:
        return JSONResponse({"error": "no_existe"}, status_code=404)
    if o["status"] != "pendiente":
        return JSONResponse({"error": "en_marcha", "mensaje": "El pedido ya está en marcha."},
                            status_code=409)
    ORDERS.remove(o)
    return {"ok": True}


@app.post("/api/order/{oid}/status")
async def set_status(oid: int, s: StatusIn):
    o = next((x for x in ORDERS if x["id"] == oid), None)
    if not o:
        return JSONResponse({"error": "no_existe"}, status_code=404)
    if s.status in ("pendiente", "en_camino", "entregado"):
        o["status"] = s.status
    return {"ok": True, **_public(o)}


app.mount("/", StaticFiles(directory=str(WEB), html=True), name="web")
