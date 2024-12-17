class Zoologico:

    def __init__(self, nombre = None, ubicacion = None, zonas = None):
        self._nombre = nombre
        self._ubicacion = ubicacion
        if zonas == None:
            zonas = []
        self._zonas = zonas

    def agregarZonas(self,zona):
        self._zonas.append(zona)

    def cantidadTotalAnimales(self):
        from gestion.zona import Zona
        tot = 0
        for elm in self._zonas:
            tot += elm.cantidadAnimales()
        return tot
    
    def getNombre(self):
        return self._nombre
    
    def getZona(self):
        return self._zonas
    
