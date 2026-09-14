# Arquitectura — Don Pepito

## Identidad arquitectónica

- Tipo: `product`
- Capacidad: `marine_food_delivery`
- Ciclo de vida: `pilot`
- Fuente de verdad de estado: `ESTADO.md`
- Relaciones: `factoria`

## Documentos y entradas canónicas

- No se ha localizado una especificación arquitectónica detallada independiente. Este archivo es el índice mínimo y el vacío queda pendiente de definición.

## Frontera del proyecto

Este proyecto conserva su código, datos y reglas de dominio. Las capacidades compartidas de HomeAI, PPD, Factoría o MEISSON se consumen mediante contratos o integraciones documentadas; no deben copiarse sin una decisión explícita.

## Gobierno de cambios

Antes de modificar arquitectura se leen `ESTADO.md`, este índice, ADR existentes, pruebas y estado Git. Una reorganización física requiere verificar despliegue y rollback.

## Estructura y deuda

El índice no implica que la estructura física esté normalizada. Datos operativos, artefactos generados, backups y ejecutables que estén en la raíz se separarán solamente después de comprobar dependencias, despliegue y recuperabilidad.
