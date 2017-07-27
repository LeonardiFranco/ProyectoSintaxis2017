'''Definicion de la estructura que devuelve el analizador sintactico'''
class ATree(object):
    '''Clase principal de la estructura, define un arbol de analisis sintactico.'''
    def __init__(self,data,parent):
        self.data = data
        self.parent = parent
        self.children = []

    def add_child(self,child):
        self.children.append(child)

    def get_parent(self):
        return self.parent

    def get_children(self):
        return self.children

    def get_data(self):
        return self.data

    def __repr__(self):
        return str(self.data) + str(self.children)
