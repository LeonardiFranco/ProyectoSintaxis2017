'''Traductor, toma un arbol de analisis sintactico y lo traduce a codigo de Python 3'''

class Interpreter(object):
    '''Clase principal del traductor.'''
    def __init__(self, tree):
        self.tree = tree
        self.ts = {}

    def inter(self):
        '''Inicia el interprete con el arbol de analisis sintactico provisto.'''
        self.programa(self.tree)

    def programa(self,tree):
        self.seq(tree.children[0])

    def seq(self,tree):
        if tree.children:
            self.sentencia(tree.children[0])
            self.seq(tree.children[1])

    def sentencia(self, tree):
        child = tree.children[0]
        if child.data == 'asignacion':
            self.asignacion(child)
        elif child.data == 'lectura':
            self.lectura(child)
        elif child.data == 'escritura':
            self.escritura(child)
        elif child.data == 'condicional':
            self.condicional(child)
        elif child.data == 'ciclo':
            self.ciclo(child)

    def asignacion(self, tree):
        resultado = self.exparit(tree.children[2])
        self.ts[tree.children[0].children[0].data.atrib] = resultado

    def lectura(self, tree):
        cadena = tree.children[2].children[0]
        _temp = float(input(cadena.data.atrib))
        self.ts[tree.children[4].children[0].data.atrib] = _temp

    def escritura(self, tree):
        print(tree.children[2].children[0].data.atrib+str(self.exparit(tree.children[4])))

    def condicional(self, tree):
        _bool = self._bool(tree.children[1])
        if _bool:
            self.bloque(tree.children[3])
        else:
            self._else(tree.children[4])

    def _else(self, tree):
        if tree.children:
            self.bloque(tree.children[1])

    def ciclo(self, tree):
        _bool = self._bool(tree.children[1])
        while _bool:
            self.bloque(tree.children[3])
            _bool = self._bool(tree.children[1])

    def _bool(self, tree):
        _1cond = self.condicion(tree.children[0])
        resultado = self.sbool(tree.children[1], _1cond)
        return resultado

    def sbool(self, tree, _1cond):
        if not tree.children:
            return _1cond
        else:
            _2cond = self.condicion(tree.children[1])
            if tree.children[0].children[0].data.atrib == 'or':
                _res = _1cond or _2cond
            else:
                _res = _1cond and _2cond
            resultado = self.sbool(tree.children[2], _res)
            return resultado

    def condicion(self, tree):
        _1exp = self.exparit(tree.children[0])
        resultado = self.scond(tree.children[1], _1exp)
        return resultado

    def scond(self, tree, _1exp):
        _2exp = self.exparit(tree.children[1])
        _OP = tree.children[0].children[0].data.atrib
        if _OP == '==':
            return _1exp == _2exp
        elif _OP == '<=':
            return _1exp <= _2exp
        elif _OP == '>=':
            return _1exp >= _2exp
        elif _OP == '!=':
            return _1exp != _2exp
        elif _OP == '<':
            return _1exp < _2exp
        elif _OP == '>':
            return _1exp > _2exp

    def bloque(self, tree):
        self.seq(tree.children[1])

    def exparit(self, tree):
        _1term = self.term(tree.children[0])
        resultado = self.sexparit(tree.children[1], _1term)
        return resultado

    def sexparit(self,tree, _1term):
        if not tree.children:
            return _1term
        else:
            _2term = self.term(tree.children[1])
            if tree.children[0].data == 'OPS':
                _res = _1term + _2term
            else:
                _res = _1term - _2term
            resultado = self.sexparit(tree.children[2], _res)
            return resultado

    def term(self,tree):
        _1neg = self.neg(tree.children[0])
        resultado = self.sterm(tree.children[1], _1neg)
        return resultado

    def sterm(self, tree, _1neg):
        if not tree.children:
            return _1neg
        else:
            _2neg = self.neg(tree.children[1])
            if tree.children[0].children[0].data.atrib == '*':
                _res = _1neg * _2neg
            else:
                _res = _1neg / _2neg
            resultado = self.sterm(tree.children[2], _res)
            return resultado

    def neg(self, tree):
        return - self.pot(tree.children[1]) if tree.children[0].data == 'OPR' else self.pot(tree.children[0])

    def pot(self, tree):
        _1factor = self.factor(tree.children[0])
        resultado = self.spot(tree.children[1], _1factor)
        return resultado

    def spot(self, tree, _1factor):
        if not tree.children:
            return _1factor
        else:
            _2factor = self.factor(tree.children[1])
            if tree.children[0].children[0].data.atrib == '**':
                _res = _1factor ** _2factor
            else:
                _res = _1factor ** (1.0/_2factor)
            resultado = self.spot(tree.children[2], _res)
            return resultado

    def factor(self, tree):
        if tree.children[0].data == 'ID':
            return self.ts.get(tree.children[0].children[0].data.atrib)
        elif tree.children[0].data == 'CONST':
            return tree.children[0].children[0].data.atrib
        else:
            return self.exparit(tree.children[1])

