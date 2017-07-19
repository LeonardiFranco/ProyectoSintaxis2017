Gramática modificada y TAS.
===========================

Gramática
---------

| **Programa** → **Seq** Fin
| **Seq** → **Sentencia** **Seq**\| ε
| **Sentencia** → **Asignación** \| **Lectura** \| **Escritura** \| **Condicional** \| **Ciclo**
| **Asignación** → id = **ExpArit**
| **Lectura** → LEER ( “cadena” ,identificador)
| **Escritura** → ESCRIBIR ( “cadena” ,ExpArit)
| **Condicional** → si **Bool** entonces **Bloque** **Else**
| **Else** → sino **Bloque** \| ε
| **Ciclo** → mientras **Bool** hacer **Bloque**
| **Bool** → **Condición** **SBool**
| **SBool** →  **OpLog** **Condición** **SBool** \| ε
| **Condición** → ( **ExpArit** **OpRel** **ExpArit** ) \| not **Condición**
| **Bloque** → { **Seq** }
| **ExpArit** → **Term** **SExpArit**
| **SExpArit** → **Op1** **Term** **SExpArit**\| ε
| **Term** → **Neg** **STerm**
| **STerm** → **Op2** **Neg** **STerm** \| ε
| **Neg** → -**Pot** \| **Pot**
| **Pot** → **Factor** **SPot**
| **SPot** → **Op3** **Factor** **SPot** \| ε
| **Factor** → id \| const \| ( **ExpArit** )
| **Op1** → + \| -
| **Op2** → * \| /
| **Op3** → ** \| //
| **OpLog** → or \| and
| **OpRel** → < \| > \| <= \| >= \| =
|


Tabla de Análisis Sintáctico
----------------------------

`TAS <TAS.html>`_
