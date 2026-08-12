# Desplegar Don Pepito en Firebase (HTTPS + tiempo real)

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
- ⚠️ **Nada de ejecutables en `web/`** (`.apk`, `.aab`, `.keystore`, `.exe`…). El plan
  gratis de Firebase (**Spark**) los **prohíbe** y el deploy revienta con *«Executable files
  are forbidden on the Spark billing plan»*. Ya están excluidos en `firebase.json` (`ignore`),
  pero NO copies una APK a `web/`. La **APK vive en `apk/Don-Pepito.apk`** y se descarga por
  GitHub: `https://github.com/salbalat/don-pepito/raw/master/apk/Don-Pepito.apk`.
- Las **reglas están abiertas** para el piloto (`firestore.rules`). Antes de abrirlo al público
  de verdad, hay que restringirlas (te aviso cuando toque).
- El backend local (`backend/`) queda solo para pruebas; en producción no se usa.
- Coste: Firestore free tier sobra para un piloto. HTTPS y hosting, gratis.
