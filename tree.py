'''Definicion de la estructura que devuelve el analizador sintactico'''
class ATree(object):
    '''Clase principal de la estructura, define un arbol de analisis sintactico.'''
    def __init__(self,data,parent):
        self.data = data
        self.parent = parent
        self.children = []

    def add_child(self,child):
        self.children.append(child)

    def __repr__(self):
        return str(self.data) + str(self.children)
