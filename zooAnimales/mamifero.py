from .animal import Animal

class Mamifero(Animal):
    listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, pelaje = None, patas = None):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero.listado.append(self)
    
    @classmethod
    def cantidadMamiferos(cls):
        return len(cls.listado)
    
    @staticmethod
    def crearCaballo(nombre, edad, genero):
        caballo = Mamifero(nombre, edad, "pradera", genero)
        caballo.setPelaje(True)
        caballo.setPatas(4)
        Mamifero.caballos += 1
        return caballo
    
    @staticmethod
    def crearLeon(nombre, edad, genero):
        leon = Mamifero(nombre, edad, "selva", genero)
        leon.setPelaje(True)
        leon.setPatas(4)
        Mamifero.leones += 1
        return leon
    
    def setPelaje(self, pelaje):
        self._pelaje = pelaje

    def setPatas(self, patas):
        self._patas = patas

    def getPatas(self):
        return self._patas

    def isPelaje(self):
        return self._pelaje