# Cómo hablar con Salvador: SIEMPRE con widgets

Regla de Salvador (09-10-2026, repetida muchas veces): **trabaja con widgets y quiere verlos siempre.**

- **Toda respuesta lleva un panel visual (widget)** con lo que haya que enseñar: estado, resultados,
  comprobaciones, informes. Sin excepción, también en respuestas cortas.
- **Cuando haya que elegir algo, el cuadro de selección** (la herramienta de preguntas con opciones,
  `AskUserQuestion`), nunca solo una pregunta en texto.
- **Al final, los siguientes pasos como botones** que envían el prompt al tocarlos. Nada de bloques
  `text` para copiar.
- Texto corto, en castellano llano. Resultados, no volcados de terminal.
- **Nada de copiar y pegar** (Salvador, 10-10-2026: «tienes que crear widgets de respuesta, que no tengo que copiar y pegar»): las elecciones y los siguientes pasos van como **botones** en el widget o en el cuadro de selección, que se envían al tocarlos. Los bloques `text` NO se usan (14-10-2026, Salvador harto: «no sé cómo decirte que tienes que hacer widget de respuestas»). Cada respuesta acaba: panel con resultado → botones → cuadro `AskUserQuestion` → panel otra vez tras su elección. No se le dan órdenes para que las copie: lo que se pueda hacer, lo hace Claude.
