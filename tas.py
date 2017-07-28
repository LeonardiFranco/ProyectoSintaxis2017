'''Tabla de Analisis Sintactico, implementada en un diccionario.
Los cambios en la gramatica se pueden hacer facilmente y lo unico que hariamos es editar este archivo.'''
TAS = {
    'programa':{
        'ID':['seq', 'END'],
        'READ':['seq', 'END'],
        'WRITE':['seq', 'END'],
        'IF':['seq', 'END'],
        'WHILE':['seq', 'END'],
        '$':['seq', 'END'],
    },
    'seq':{
        'ID':['sentencia', 'seq'],
        'READ':['sentencia', 'seq'],
        'WRITE':['sentencia', 'seq'],
        'IF':['sentencia', 'seq'],
        'WHILE':['sentencia', 'seq'],
        'END':[],
        '}':[],
    },
    'sentencia':{
        'ID':['asignacion'],
        'READ':['lectura'],
        'WRITE':['escritura'],
        'IF':['condicional'],
        'WHILE':['ciclo']
    },
    'asignacion':{
        'ID':['ID','=','exparit']
    },
    'lectura':{
        'READ':['READ','(','CADENA', ',' ,'ID',')']
    },
    'escritura':{
        'WRITE':['WRITE','(','CADENA', ',' ,'exparit',')']
    },
    'condicional':{
        'IF':['IF','bool','THEN','bloque','else']
    },
    'else':{
        'ID':[],
        'READ':[],
        'WRITE':[],
        'IF':[],
        'WHILE':[],
        'ELSE':['ELSE','bloque'],
        'END':[],
        '}':[]
    },
    'ciclo':{
        'WHILE':['WHILE','bool','DO','bloque']
    },
    'bool':{
        'ID':['condicion','sbool'],
        '(':['condicion','sbool'],
        'CONST':['condicion','sbool'],
        'OPNOT':['condicion','sbool']
    },
    'sbool':{
        'OPLOG':['OPLOG','condicion','sbool'],
        'THEN':[],
        'DO':[]
    },
    'condicion':{
        'ID':['exparit','scond'],
        '(':['exparit','scond'],
        'OPR':['exparit','scond'],
        'CONST':['exparit','scond'],
        'OPNOT':['OPNOT','(','condicion',')']
    },
    'scond':{
        'OPREL':['OPREL','exparit']
    },
    'bloque':{
        '{':['{','seq','}']
    },
    'exparit':{
        'ID':['term', 'sexparit'],
        '(':['term', 'sexparit'],
        'CONST':['term', 'sexparit'],
        'OPR':['term', 'sexparit'],
    },
    'sexparit':{
        'ID':[],
        'READ':[],
        'WRITE':[],
        'IF':[],
        'WHILE':[],
        'DO':[],
        'THEN':[],
        'OPLOG':[],
        'OPR':['OPR','term','sexparit'],
        'OPS':['OPS','term','sexparit'],
        'OPREL':[],
        'END':[],
        ')':[],
        '}':[]
    },
    'term':{
        'ID':['neg', 'sterm'],
        '(':['neg', 'sterm'],
        'CONST':['neg', 'sterm'],
        'OPR':['neg', 'sterm'],
    },
    'sterm':{
        'ID':[],
        'READ':[],
        'WRITE':[],
        'IF':[],
        'WHILE':[],
        'DO':[],
        'THEN':[],
        'OPLOG':[],
        'OPR':[],
        'OPS':[],
        'OP2':['OP2','neg','sterm'],
        'OPREL':[],
        'END':[],
        ')':[],
        '}':[]
    },
    'neg':{
        'ID':['pot'],
        '(':['pot'],
        'CONST':['pot'],
        'OPR':['OPR', 'pot'],
    },
    'pot':{
        'ID':['factor','spot'],
        '(':['factor','spot'],
        'CONST':['factor', 'spot'],
    },
    'spot':{
        'ID':[],
        'READ':[],
        'WRITE':[],
        'IF':[],
        'WHILE':[],
        'DO':[],
        'THEN':[],
        'OPLOG':[],
        'OPR':[],
        'OPS':[],
        'OP2':[],
        'OP3':['OP3','factor','spot'],
        'OPREL':[],
        'END':[],
        ')':[],
        '}':[]
    },
    'factor':{
        'ID':['ID'],
        '(':['(','exparit',')'],
        'CONST':['CONST']
    },
}