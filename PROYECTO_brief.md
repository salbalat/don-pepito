# Mojito Boat — brainstorm (grill-me)

**Resumen:** PWA para pedir cócteles a un barco que sirve en el mar; localiza el barco,
da tiempo estimado de llegada y pone el pedido en cola.

## Decisiones
- (pendiente de la entrevista)

## Q&A
- (se irá rellenando)

## Pendientes / a averiguar
- ¿De quién es el negocio? ¿real o idea?
- ¿Desde dónde piden los clientes (playa / su barco / nadando)?
- Modelo de localización y ETA
- Pagos, mapa/GPS, offline en el mar, idioma

---
## Ronda 1
- **De quién:** solo una IDEA a validar → objetivo = prototipo/MVP para probar el concepto.
- **Quién pide:** desde su propio barco/hamaca en el mar → modelo "Uber del cóctel":
  cliente con posición GPS, el Mojito Boat va a él. ETA = distancia/velocidad + cola.

### Decisiones
- Enfoque: PROTOTIPO para validar, no sistema de producción.
- Modelo: entrega a la posición del cliente en el mar (no playa, no a bordo).

## Ronda 2
- **MVP elegido:** Cliente + barco + pago (versión completa).
- **Pago:** en la app con tarjeta (necesita pasarela tipo Stripe).
- ⚠️ TENSIÓN detectada: dijo "idea a validar" pero pide la versión completa con pago.
  Riesgo: mucho trabajo/coste antes de saber si la gente pide. A confirmar en ronda 3.

### Pendientes nuevos
- Pasarela de pago (Stripe): cuenta, comisiones, claves.
- ¿Posición del barco: GPS en vivo del operario, a mano, o simulada?
- Conectividad en alta mar (riesgo gordo).

## Ronda 3
- **Alcance:** POR FASES. Fase 1 = cliente (pedir, ver barco, ETA, cola) + pantalla del
  barco, pago AL RECIBIR. Fase 2 = pago con tarjeta (Stripe).
- **Posición barco:** GPS en vivo del operario (app del barco comparte posición).

### Decisiones técnicas (propuestas, ajustables)
- PWA móvil con DOS modos: Cliente y Barco (operario). Un solo código.
- Backend en tiempo real: Firebase (Firestore) o Supabase — free tier para el prototipo.
- ETA = distancia (haversine cliente↔barco) / velocidad asumida + tiempo de cola.

## Ronda 4
- **¿Hay barco?** SÍ, este verano → Fase 1 = prueba REAL con clientes en el mar (no demo).
- **Carta:** cócteles + refrescos + algo de picar.

### RIESGO gordo a gestionar
- Cobertura en el mar: si no hay señal, no se puede pedir. Mitigación: cerca de costa/calas
  suele haber 4G; los pedidos y posiciones se reintentan al recobrar señal; avisar al
  cliente si está sin cobertura. GPS funciona sin datos, pero enviar el pedido necesita red.

## Ronda 5
- **Éxito:** un pedido REAL de punta a punta (cliente pide en el agua → ETA → barco lo ve →
  entrega ≈ en ese tiempo).
- **Idiomas:** cliente ES/EN/DE; operario ES.

---
# BRIEF FINAL (para OK)
- **Qué es:** PWA "Uber del cóctel". Barco que sirve cócteles en el mar; clientes (en su
  barco/flotando) piden desde el móvil; la app localiza el Mojito Boat (GPS en vivo del
  operario), da tiempo estimado (distancia + cola) y el barco entrega.
- **Para quién:** idea propia a validar, con BARCO REAL este verano → Fase 1 = piloto real.
- **MVP (Fase 1):** una PWA con 2 modos:
  · Cliente → mapa con el barco, carta, pedir, ETA + nº en cola, seguir el pedido.
  · Barco/operario → comparte su GPS y ve la cola de pedidos (por cercanía/turno).
  Pago AL RECIBIR (sin tarjeta todavía).
- **Carta:** cócteles + refrescos + algo de picar (carta de ejemplo editable).
- **Idiomas:** cliente ES/EN/DE · operario ES.
- **Técnica (propuesta):** PWA móvil + backend en tiempo real (Firebase Firestore, free
  tier) para posiciones y cola. ETA = haversine + velocidad asumida (ajustable).
- **Fase 2:** pago con tarjeta (Stripe).
- **Riesgo principal:** cobertura en alta mar (reintentos + aviso sin señal; cerca de costa
  suele haber 4G).
- **Éxito:** un pedido real de punta a punta con el tiempo cumplido.
- **Dónde vive:** ~/Documents/Claude/Projects/Mojito Boat/ (proyecto NUEVO, carpeta propia).
