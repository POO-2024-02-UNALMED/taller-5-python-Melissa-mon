from .animal import Animal

class Reptil(Animal):
    listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorEscamas = None, largoCola = None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil.listado.append(self)

    def movimiento():
        return "reptar"
    
    @classmethod
    def cantidadReptiles(cls):
        return len(cls.listado)
    
    @staticmethod
    def crearIguana(nombre, edad, genero):
        iguana = Reptil(nombre, edad, "humedal", genero)
        iguana.setColorEscamas("verde")
        iguana.setLargoCola(3)
        Reptil.iguanas += 1
        return iguana
    
    @staticmethod
    def crearSerpiente(nombre, edad, genero):
        serpiente = Reptil(nombre, edad, "jungla", genero)
        serpiente.setColorEscamas("blanco")
        serpiente.setLargoCola(1)
        Reptil.serpientes += 1
        return serpiente
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def getColorEscamas(self):
        return self._colorEscamas

    def setLargoCola(self, largoCola):
        self._largoCola = largoCola

    def getLargoCola(self):
        return self._largoCola