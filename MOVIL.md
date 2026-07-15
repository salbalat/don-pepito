# Don Pepito — app para iPhone y Android (Capacitor)

La misma web (`web/`) empaquetada como app nativa. appId **com.okmeisson.donpepito**.

## IMPORTANTE (una vez): Firebase
Para que la app funcione en el móvil de verdad (no localhost), primero configura Firebase:
pega tu config en `web/firebase-config.js` (ver **DEPLOY.md**). Luego:

```bash
npx cap sync        # copia la web (con la config) a iOS y Android
```

## iPhone
```bash
npx cap open ios    # abre Xcode → elige tu equipo en Signing → ▶ para probar en simulador/iPhone
```
Team ID de Apple (Flux): 4UYL2U36M4.

## Android
```bash
npx cap open android  # abre Android Studio → ▶ para probar en emulador/móvil
```

## Cada vez que cambies la web
```bash
npx cap sync
```
