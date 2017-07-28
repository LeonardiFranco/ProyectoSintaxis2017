Definición Sintáctica
=====================

Gramática BNF
-------------

| <Programa> ::= <Seq> “fin” | “fin”
| <Seq> ::= <Sentencia> <Seq> | <Sentencia>
| <Sentencia> ::= <Asignación> | <Lectura> | <Escritura> | <Condicional> | <Ciclo>
| <Asignación> ::= “identificador” “=” <ExpArit>
| <Lectura> ::= “LEER” “(“ “cadena” “,” ”identificador” “)”
| <Escritura> :== “ESCRIBIR” “(“ “cadena” “,” ExpArit “)”
| <Condicional> :== “si” <Bool> “entonces” <Bloque> <Else> | “si” <Bool> “entonces” <Bloque>
| <Else> :== “sino” <Bloque>
| <Ciclo> :== “mientras” <Bool> “hacer” <Bloque>
| <Bool> :== <Condición> <SBool> | <Condición>
| <SBool> :==  <opLog> <Condición> <SBool> | <opLog> <Condición>
| <Condición> :==  <ExpArit> <SCond>  | “not” “(“  <Condición> “)”
| <SCond> :== “OPREL” <ExpArit>
| <Bloque> :== “{” <Seq> “}”|“{”“}”
| <ExpArit> :== <Term> <SExpArit> | <Term>
| <SExpArit> :== “OPS” <Term> <SExpArit> | “OPS” <Term> | “OPR” <Term> <SExpArit> | “OPR” <Term>
| <Term> :== <Neg> <STerm> | <Neg>
| <STerm> :== “OP2” <Neg> <STerm> | “OP2” <Neg>
| <Neg> :== “OPR”<Pot> | <Pot>
| <Pot> :== <Factor> <SPot> | <Factor>
| <SPot> :== “OP3” <Factor> <SPot> | “OP3” <Factor>
| <Factor> :== “id” | “const” | “(” <ExpArit> “)”



Gramática
---------

| **Programa** → **Seq** fin
| **Seq** → **Sentencia Seq** | ε
| **Sentencia** → **Asignación** | **Lectura** | **Escritura** | **Condicional** | **Ciclo**
| **Asignación** → identificador = **ExpArit**
| **Lectura** → leer ( “cadena” ,identificador)
| **Escritura** → escribir( “cadena” , **ExpArit** )
| **Condicional** → si **Bool** entonces **Bloque** **Else**
| **Else** → sino **Bloque** | ε
| **Ciclo** → mientras **Bool** hacer **Bloque**
| **Bool** → **Condición** **SBool**
| **SBool** →  OPLOG **Condición** **SBool** | ε
| **Condición** →  **ExpArit** **SCond**  | not ( **Condición** )
| **SCond** → OPREL **ExpArit**
| **Bloque** → { **Seq** }
| **ExpArit** → **Term** **SExpArit**
| **SExpArit** → OPS **Term** **SExpArit** | OPR **Term** **SExpArit** | ε
| **Term** → **Neg** **STerm**
| **STerm** → OP2 **Neg** **STerm** | ε
| **Neg** → OPR **Pot** | **Pot**
| **Pot** → **Factor** **SPot**
| **SPot** → OP3 **Factor** **SPot** | ε
| **Factor** → id | const | ( **ExpArit** )

La gramatica esta factorizada y no tiene recursividad por izquierda.

Tabla de Análisis Sintáctico
----------------------------

Tabla de Análisis Sintáctico hecha a partir de la gramatica anterior.
Se incluye el archivo `Primeros y Siguientes <primeros_y_siguientes.txt>`_ que tiene los resultados de las funciones Primero y Siguiente para las variables.


`TAS <TAS.html>`_
+++++++++++++++++