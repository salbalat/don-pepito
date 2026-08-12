# Don Pepito 🍹⛵ — arroces y cócteles a tu barco, en el mar

**Web:** https://donpepito-javea.web.app/www · **App:** https://donpepito-javea.web.app

El cliente pide desde su barco o flotando en una cala; la app localiza el Don Pepito,
enseña el tiempo estimado y su turno, y el barco le lleva el pedido. Se paga al recibir.

- **Carta real** del 15º aniversario (Jávea): arroces del día 18 € (20 € con refresco),
  mojitos, cócteles, smoothies con nombres de calas, batidos y granizados.
  Original en [`docs/carta/`](docs/carta/).
- **Modo Cliente** (ES/EN/DE): mapa marino real, carta, pedido con ETA y cola, perfil
  «Mi barco» (nombre, color y foto opcionales), pedir por WhatsApp.
- **Modo Barco** (protegido con código): GPS en vivo, cola con colores y fotos de los
  barcos, aviso sonoro de pedidos nuevos, mapa de flota numerado.
- **Web pública** con la carta semanal, el tiempo y las olas de Jávea, recomendación
  de cala del día, QR y descarga de la app (iPhone y Android).

## Publicar cambios

```bash
git pull && firebase deploy
```

Se publica en donpepito-javea.web.app y donpepito-2607151158.web.app (el QR impreso
apunta a la segunda; las dos sirven lo mismo).

## Apps móviles

Proyectos nativos con Capacitor (`ios/`, `android/`) — pasos en [`MOVIL.md`](MOVIL.md).
Icono y pantalla de arranque se regeneran con `npx @capacitor/assets generate` desde
[`assets/`](assets/). La PWA (botón «Instalar» de la propia app) es la vía sin tiendas.

## Estructura

```
web/        PWA (app cliente/barco) + web pública (web/www)
backend/    modo local de pruebas (FastAPI)
ios/ android/  proyectos nativos (Capacitor)
docs/carta/    la carta real (PDF + texto extraído)
```
