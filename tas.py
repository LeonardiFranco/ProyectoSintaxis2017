'''Tabla de Analisis Sintactico, implementada en un diccionario'''
TAS = {
    'programa':{
        'ID':['seq', 'END'],
        'READ':['seq', 'END'],
        'WRITE':['seq', 'END'],
        'IF':['seq', 'END'],
        'WHILE':['seq', 'END'],
        'END':['seq', 'END'],
        '}':['seq', 'END'],
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
        'ELSE':['ELSE','bloque'],
        'END':[],
        '}':[]
        },
    'ciclo':{
        'WHILE':['WHILE','bool','DO','bloque']
        },
    'bool':{
        '(':['condicion','sbool'],
        'OPNOT':['condicion','sbool']
        },
    'sbool':{
        'OPLOG':['OPLOG','condicion','sbool'],
        'THEN':[],
        'DO':[]
        },
    'condicion':{
        '(':['(','exparit','OPREL','exparit',')'],
        'OPNOT':['OPNOT','condicion']
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