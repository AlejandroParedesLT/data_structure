'''
Titulo: Implementacion de nodo

Autor: Alejandro Paredes
'''

class node:
	def __init__(self,value=None):
		self.value=value
		self.left_child=None
		self.right_child=None
		self.parent=None # pointer to parent node in tree