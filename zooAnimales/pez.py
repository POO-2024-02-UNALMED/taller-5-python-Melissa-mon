from .animal import Animal

class Pez(Animal):
    listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorEscamas = None, cantidadAletas = None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez.listado.append(self)

    def movimiento():
        return "nadar"
    
    @classmethod
    def cantidadPeces(cls):
        return len(cls.listado)
    
    @staticmethod
    def crearSalmon(nombre, edad, genero):
        salmon = Pez(nombre, edad, "oceano", genero)
        salmon.setColorEscamas("rojo")
        salmon.setCantidadAletas(6)
        Pez.salmones += 1
        return salmon
    
    @staticmethod
    def crearBacalao(nombre, edad, genero):
        bacalao = Pez(nombre, edad, "oceano", genero)
        bacalao.setColorEscamas("gris")
        bacalao.setCantidadAletas(6)
        Pez.bacalaos += 1
        return bacalao
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def getColorEscamas(self):
        return self._colorEscamas

    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas

    def getCantidadAletas(self):
        return self._cantidadAletas