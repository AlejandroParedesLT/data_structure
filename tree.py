# Este es un codigo ejemplo de la clase treeNode 
class treeNode():
    # Metodo para instanciar objeto de tipo treeNode
    def __init__(self, value):
        self.left=None
        self.right=None
        self.data=value
        self.level=0
    def getData(self):
        return self.data
    def setData(self,x):
        self.data = x
# Como codificaria los demas metodos?


#https://github.com/jpeinado/structure