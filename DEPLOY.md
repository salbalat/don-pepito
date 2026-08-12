# Desplegar Don Pepito en Firebase (HTTPS + tiempo real)

## ⚠️ Publicación automática: estado de cada dirección (agosto 2026)

| Dirección | Estado | Arreglo |
|---|---|---|
| `salbalat.github.io/don-pepito` | Daba **404** porque GitHub Pages nunca se activó en los ajustes del repo. | **Arreglado**: el workflow de Pages ahora lo activa y publica solo en cada cambio de master. |
| `donpepito-javea.web.app` y `donpepito-2607151158.web.app` (la del QR) | Abren, pero **solo se actualizan cuando ejecutas `firebase deploy` a mano**: sin el secreto de Firebase, la publicación automática se salta en silencio en cada merge (ahora al menos deja un aviso visible en Actions). | Una sola vez, desde el ordenador con sesión de Firebase iniciada: `firebase init hosting:github` (crea el secreto `FIREBASE_SERVICE_ACCOUNT_DONPEPITO_2607151158` en GitHub). |

Ese arreglo pide tu sesión de Google (`firebase login`), por eso no se puede hacer
desde aquí. Con el secreto creado, cada cambio en master actualizará las dos
direcciones de Firebase él solo, igual que la de GitHub Pages. Mientras tanto:
`git pull && firebase deploy` después de cada merge.

La app funciona en **dos modos**: si `web/firebase-config.js` tiene tu config, usa
**Firebase** (nube, tiempo real, HTTPS); si está vacío, usa el **backend local** (para pruebas
en el Mac). Para el barco de verdad → Firebase.

## Pasos (los de login/crear proyecto los haces tú; el resto lo hago yo)

1. **Instalar la herramienta** (una vez):
   ```bash
   npm i -g firebase-tools
   ```
2. **Entrar en tu cuenta** (tu Google — yo no toco credenciales):
   ```bash
   firebase login
   ```
3. **Crear el proyecto** (en la consola es más fácil): https://console.firebase.google.com
   → *Añadir proyecto* → nombre p.ej. `mojito-boat`. Apunta el **Project ID**.
4. **Activar Firestore**: en la consola, *Build → Firestore Database → Crear base de datos*
   (modo *producción*; las reglas del piloto ya están en `firestore.rules`).
5. **Añadir app Web** y copiar su config: consola → ⚙ *Configuración del proyecto* →
   *Tus apps* → **Web (</>)** → *SDK setup and configuration → Config*. Pega ese objeto en
   **`web/firebase-config.js`** (es config PÚBLICA, segura).
6. **Poner el Project ID** en `.firebaserc` (o dime el ID y lo pongo yo), y **desplegar**:
   ```bash
   firebase deploy
   ```
7. Firebase te da la URL: **https://TU-PROJECT-ID.web.app** — esa es la que abres en el móvil
   (HTTPS → el GPS funciona). Modo Cliente para pedir, modo Barco para servir.

## Notas
- Las **reglas están abiertas** para el piloto (`firestore.rules`). Antes de abrirlo al público
  de verdad, hay que restringirlas (te aviso cuando toque).
- El backend local (`backend/`) queda solo para pruebas; en producción no se usa.
- Coste: Firestore free tier sobra para un piloto. HTTPS y hosting, gratis.
