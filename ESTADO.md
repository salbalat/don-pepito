# Don Pepito — ESTADO (este documento MANDA)

> **Antes de tocar, probar o "arreglar" nada: LEE este ESTADO.md y el git** (`git branch -a`, `git log --all --oneline`).
> No rehagas de cero lo que ya existe: casi siempre está en otra rama o en el historial. Consolidar por fusión.

Última actualización: 2026-08-28 (autogenerado desde git + README reales; **revisar y completar lo marcado "por confirmar"**).

## Repositorio PÚBLICO a propósito (decisión de Salvador, 29-09-2026)
`salbalat/don-pepito` es **público** aunque la regla general es privado: el botón y el QR de
descarga de la APK apuntan a `https://github.com/salbalat/don-pepito/raw/master/apk/Don-Pepito.apk`
(`web/www/index.html`, `README.md`, `MOVIL.md`), y ese enlace solo funciona con el repo público.
Por eso: **nunca subir aquí claves ni datos privados.** Si algún día se hace privado, antes hay
que mover la APK a otro sitio o el botón deja de funcionar.

## Qué es
Arroces y cócteles a tu barco, en el mar (Jávea). El cliente pide desde su barco o flotando en una cala; la app localiza el Don Pepito, enseña el tiempo estimado y su turno, y el barco le lleva el pedido (se paga al recibir). Tiene **Modo Cliente** (ES/EN/DE/NL: mapa marino, carta, pedido con ETA y cola, perfil "Mi barco", pedir por WhatsApp) y **Modo Barco** (protegido con código: GPS en vivo, cola con colores/fotos, aviso sonoro, mapa de flota numerado), más una **web pública** con carta semanal, tiempo/olas de Jávea, cala del día, QR y descarga de la app.

## Estado y ramas
- Rama principal: `master`. Existe `gh-pages` en remoto y ramas `claude/*` (`don-pepito-9kv6ce`, `don-pepito-continuation-n7z1s0`, `factoría-no-abre-zun1ef`, `mapa-mar-tiempo-real-9gkgg8`) y `okm/configurar-firebase-en-el-proyec-70e9e83`.
- Último commit: `f65d8e2` — "Repo: dejar de rastrear la cache de despliegue de Firebase (.firebase/)" (fecha por confirmar: el log no trae fecha).
- Actividad reciente: publicación desde Firebase y ajustes de despliegue. Se resolvió que Firebase (plan Spark) prohíbe ejecutables, así que la APK descargable (botón + QR) apunta a GitHub raw en vez de al hosting. Antes: caja del día y recorrido del barco en el mapa, refresco horario de pronóstico/mar/temperatura del agua, cala recomendada para los próximos días según viento, letrero UX junto a la flecha del navegador, y libro de versiones con norma de aprobación previa.

## Stack y despliegue
- `package.json` (`name: don-pepito`). Apps nativas con **Capacitor** (`ios/`, `android/`); iconos/splash con `npx @capacitor/assets generate`. `capacitor.config.json` en raíz.
- Hosting en **Firebase** (plan Spark): publicar con `git pull && firebase deploy`. Se publica en `donpepito-javea.web.app` y `donpepito-2607151158.web.app` (el QR impreso apunta a la segunda, que redirige a `javea`).
- Aviso duro del README: **no meter ejecutables (`.apk`/`.aab`/`.keystore`) en `web/`** — Spark los prohíbe y el deploy falla; están excluidos en `firebase.json` (`ignore`). La APK vive en `apk/`.
- Docs: `README.md`, `DEPLOY.md`, `MOVIL.md`, `PROYECTO.md`, `PROYECTO_brief.md`, `VERSIONES.md`.

## Dónde corre / dispositivos
- Web/app en producción: `https://donpepito-javea.web.app` (web pública en `/www`) y alias `donpepito-2607151158.web.app`.
- Móvil (iPhone/Android donde se instaló la app Capacitor / la APK): por confirmar.

## Decisiones y lo que se probó/descartó
- Descartado servir ejecutables desde Firebase Hosting (Spark lo prohíbe): la APK se distribuye por GitHub raw, no por el hosting.
- Se dejó de rastrear la cache de despliegue `.firebase/` en el repo.
- Norma de aprobación previa + libro de versiones (`VERSIONES.md`).

## Pendiente / próximos pasos
- Hay ramas `claude/*` abiertas (incluida `factoría-no-abre-zun1ef` y `mapa-mar-tiempo-real-9gkgg8`) y `okm/configurar-firebase-en-el-proyec-*` que conviene revisar y fusionar o descartar explícitamente.
- Resto: por confirmar.
