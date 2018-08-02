'''Definición de la estructura que devuelve el analizador sintáctico'''
class ATree(object):
    '''Clase principal de la estructura, define un arbol con su padre y sus hijos.'''
    def __init__(self,data,parent):
        self.data = data
        self.parent = parent
        self.children = []

    def add_child(self,child):
        self.children.append(child)

    def add_children(self, *args):
    	children = [*args]
    	self.children.extend(children)

    def __repr__(self):
        return str(self.data) + str(self.children)

if __name__ == "__main__":
	tree = ATree('programa', None)
	var = ['chulengo','sandunga']
	print(tree.children)