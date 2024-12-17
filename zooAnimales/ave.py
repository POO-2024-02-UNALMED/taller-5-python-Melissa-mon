from .animal import Animal

class Ave(Animal):
    listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorPlumas = None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave.listado.append(self)

    def movimiento(self):
        return "volar"
    
    @classmethod
    def cantidadAves(cls):
        return len(cls.listado)
    
    @staticmethod
    def crearHalcon(nombre, edad, genero):
        halcon = Ave(nombre, edad, "montañas", genero)
        halcon.setColorPlumas("cafe glorioso")
        Ave.halcones += 1
        return halcon
    
    @staticmethod
    def crearAguila(nombre, edad, genero):
        aguila = Ave(nombre, edad, "montañas", genero)
        aguila.setColorPlumas("blanco y amarillo")
        Ave.aguilas += 1
        return aguila
    
    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas

    def getColorPlumas(self):
        return self._colorPlumas