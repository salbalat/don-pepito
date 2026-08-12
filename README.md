# Don Pepito 🍹⛵ — arroces y cócteles a tu barco, en el mar

**Web:** https://donpepito-javea.web.app/www · **App:** https://donpepito-javea.web.app

El cliente pide desde su barco o flotando en una cala; la app localiza el Don Pepito,
enseña el tiempo estimado y su turno, y el barco le lleva el pedido. Se paga al recibir.

- **Carta real** del 15º aniversario (Jávea): arroces del día 18 € (20 € con refresco),
  mojitos, cócteles, smoothies con nombres de calas, batidos y granizados.
  Original en [`docs/carta/`](docs/carta/).
- **Modo Cliente** (ES/EN/DE/NL): mapa marino real, carta, pedido con ETA y cola, perfil
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
apunta a la segunda; `2607151158` redirige a `javea`, incluida la raíz).

> ⚠️ **No metas ejecutables (`.apk`, `.aab`, `.keystore`) dentro de `web/`.** El plan
> gratis de Firebase (Spark) los prohíbe y el deploy falla con *«Executable files are
> forbidden on the Spark billing plan»*. Ya están excluidos en `firebase.json` (`ignore`),
> pero si copias una APK a `web/` volverá a romper. La APK vive en `apk/` (ver abajo).

## Apps móviles

Proyectos nativos con Capacitor (`ios/`, `android/`) — pasos en [`MOVIL.md`](MOVIL.md).
Icono y pantalla de arranque se regeneran con `npx @capacitor/assets generate` desde
[`assets/`](assets/). La PWA (botón «Instalar» de la propia app) es la vía sin tiendas.

**APK de Android** (generada con PWABuilder): vive en [`apk/Don-Pepito.apk`](apk/Don-Pepito.apk).
Firebase (plan gratis) **no puede servir la APK** (es ejecutable), así que NO se sube a
`web/`. Se descarga desde GitHub:

```
https://github.com/salbalat/don-pepito/raw/master/apk/Don-Pepito.apk
```

Para regenerarla: PWABuilder → Android → descarga el .zip → `apk/Don-Pepito.apk`
(NO la copies a `web/`). La clave de firma va en el .zip (`signing.keystore`); guárdala
fuera del repo si es sensible.

## Estructura

```
web/        PWA (app cliente/barco) + web pública (web/www)
backend/    modo local de pruebas (FastAPI)
ios/ android/  proyectos nativos (Capacitor)
docs/carta/    la carta real (PDF + texto extraído)
```
