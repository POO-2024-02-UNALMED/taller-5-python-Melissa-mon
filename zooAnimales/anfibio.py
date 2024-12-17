from .animal import Animal

class Anfibio(Animal):
    listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre = None, edad = None, habitat = None, genero = None, colorPiel = None, venenoso = None):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio.listado.append(self)

    def movimiento(self):
        return "saltar"
    
    @classmethod
    def cantidadAnfibios(cls):
        return len(cls.listado)
    
    @staticmethod
    def crearRana(nombre, edad, genero):
        rana = Anfibio(nombre, edad, "selva", genero)
        rana.setColorPiel("rojo")
        rana.setVenenoso(True)
        Anfibio.ranas += 1
        return rana
    @staticmethod
    def crearSalamandra(nombre, edad, genero):
        salamandra = Anfibio(nombre, edad, "selva", genero)
        salamandra.setColorPiel("negro y amarillo")
        salamandra.setVenenoso(False)
        Anfibio.salamandras += 1
        return salamandra
    
    def isVenenoso(self):
        return self._venenoso

    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel

    def getColorPiel(self):
        return self._colorPiel

    def setVenenoso(self, venenoso):
        self._venenoso = venenoso
