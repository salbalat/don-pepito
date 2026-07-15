# Don Pepito 🍹⛵ — "Uber del cóctel" en el mar

PWA para pedir cócteles a un barco que sirve en el mar. El cliente (en su barco o flotando)
pide desde el móvil; la app **localiza el Don Pepito**, calcula el **tiempo estimado**
(distancia + cola) y el barco le lleva el pedido. Brief completo: [brainstorms/mojito-boat.md](brainstorms/mojito-boat.md).

## Cómo se decidió (grill-me)
Idea a validar **con barco real este verano** → Fase 1 = piloto real, no demo.

## Fase 1 (esta) — MVP
Una PWA con **dos modos**:
- **Cliente**: mapa con el barco, carta, hacer pedido, ver **ETA + nº en cola**, seguir el estado.
- **Barco (operario)**: comparte su **GPS en vivo** y ve la **cola de pedidos** (por cercanía/turno), marca "en camino" / "entregado".
- **Pago AL RECIBIR** (tarjeta = Fase 2).
- **Idiomas**: cliente ES/EN/DE · operario ES.

## Fase 2 (después)
- Pago con tarjeta (Stripe).
- Backend en la nube (para que los móviles conecten por internet en el mar): Firebase/Supabase/Render.

## Cálculo del tiempo (ETA)
`ETA ≈ distancia(cliente↔barco) / velocidad del barco + tiempo de cola`
(haversine; velocidad ajustable; cada pedido por delante suma servicio).

## Riesgo principal
Cobertura en alta mar: si no hay señal no se puede pedir. Mitigación: reintentos, aviso al
cliente sin cobertura; cerca de costa/calas suele haber 4G. El GPS funciona sin datos.

## Éxito
Un pedido **real de punta a punta**: cliente pide en el agua → la app da un tiempo → el
barco lo ve en su cola → entrega ≈ en ese tiempo.

## Estructura
```
Don Pepito/
├── PROYECTO.md · brainstorms/  (este brief)
├── backend/    API en tiempo real (posición del barco + cola de pedidos)
└── web/        PWA (modo Cliente y modo Barco) + manifest + service worker
```
