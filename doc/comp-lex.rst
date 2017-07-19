Definicion de Componentes Léxicos
=================================

Las siguientes lineas definen las expresiones regulares de los componentes lexicos complejos:

num = [0..9], let = [a-Z]

Constante numerica:
 num num* ( | . num num*)( | E ( | - ) num num*)

Identificador:
 (_|let)(_ | let | num)*
