Definicion de Componentes Léxicos
=================================

Expresiones Regulares
---------------------

num = [0..9], let = [a-Z]

Constante numerica:
 num num* ( | . num num*)( | E ( | - ) num num*)

Identificador:
 (_|let)(_ | let | num)*
