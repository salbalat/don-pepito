# Don Pepito — app para iPhone y Android (Capacitor)

La misma web (`web/`) empaquetada como app nativa vía Capacitor.  
appId: **com.okmeisson.donpepito** · Apple Team ID: **4UYL2U36M4**

---

## Estado actual ✅

Ya está todo generado en este repo:
- `capacitor.config.json` — config de Capacitor (apunta a `web/`, sin `server.url` = modo producción)
- `ios/` — proyecto Xcode listo
- `android/` — proyecto Android Studio listo
- `node_modules/` — dependencias instaladas

---

## Setup inicial (solo una vez, en un Mac nuevo o tras clonar)

```bash
# Desde la raíz del proyecto:
npm install
```

Si en algún momento necesitas regenerar los proyectos nativos desde cero:
```bash
npx cap add ios
npx cap add android
```
> ⚠️ No es necesario si ya existen las carpetas `ios/` y `android/`.

---

## Flujo habitual (cada vez que cambies la web)

```bash
npx cap sync
```
Copia `web/` a los proyectos nativos iOS y Android. Haz esto siempre antes de abrir Xcode o Android Studio.

---

## iPhone

```bash
npx cap open ios    # abre Xcode
```

En Xcode:
1. Selecciona el target `App`
2. Ve a **Signing & Capabilities**
3. En *Team* elige tu cuenta / Team ID: **4UYL2U36M4**
4. Elige un simulador o tu iPhone conectado
5. Pulsa ▶ para compilar y lanzar

---

## Android

```bash
npx cap open android    # abre Android Studio
```

En Android Studio:
1. Espera a que sincronice Gradle (barra de progreso abajo)
2. Elige un emulador o tu Android conectado
3. Pulsa ▶ para compilar y lanzar

---

## IMPORTANTE: Firebase en el móvil

Para que la app funcione en el móvil de verdad (no localhost), la config de Firebase tiene que estar en `web/firebase-config.js` antes de hacer `npx cap sync`. Ver **DEPLOY.md** para los pasos de Firebase.

Orden correcto:
```bash
# 1. Asegúrate de tener la config en web/firebase-config.js
# 2. Sincroniza con el proyecto nativo:
npx cap sync
# 3. Abre Xcode o Android Studio y lanza la app
```

---

## Referencia rápida

| Acción | Comando |
|--------|---------|
| Instalar dependencias (1ª vez) | `npm install` |
| Copiar web → nativo | `npx cap sync` |
| Abrir en Xcode | `npx cap open ios` |
| Abrir en Android Studio | `npx cap open android` |
| Añadir plataforma (si no existe) | `npx cap add ios` / `npx cap add android` |

## APK de Android (descarga directa)

Generada con **PWABuilder** (Android → descarga el .zip). Vive en `apk/Don-Pepito.apk`.
**Firebase (plan gratis) NO puede servir la APK** (es ejecutable), así que NO la copies a
`web/` — el deploy fallaría. Se descarga desde GitHub:

```
https://github.com/salbalat/don-pepito/raw/master/apk/Don-Pepito.apk
```

La vía recomendada de instalación sigue siendo la **PWA** (botón «Instalar» / «Añadir a
pantalla de inicio»); la APK es solo para quien la quiera suelta.
