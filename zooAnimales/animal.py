class Animal:
    totalAnimales = 0

    def __init__(self, nombre = None, edad = None, habitat = None, genero = None, zona = None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
        Animal.totalAnimales += 1

    def movimiento():
        return 'desplazarse'
    
    @staticmethod
    def totalPorTipo():
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.ave import Ave
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.reptil import Reptil
        from zooAnimales.pez import Pez
        mam = Mamifero.cantidadMamiferos()
        ave = Ave.cantidadAves()
        anf = Anfibio.cantidadAnfibios()
        rep = Reptil.cantidadReptiles()
        pez = Pez.cantidadPeces()

        return f"Mamiferos : {mam}\nAves : {ave}\nReptiles : {rep}\nPeces : {pez}\nAnfibios : {anf}"
    
    def getNombre(self):
        return self._nombre
    
    def getEdad(self):
        return self._edad
    
    def getHabitat(self):
        return self._habitat
    
    def getGenero(self):
        return self._genero
    
    def getZona(self):
        return self._zona
    
    def __str__(self):
        from gestion.zona import Zona
        if self._zona != None:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self._zona.getNombre()} en el {self._zona.getZoo().getNombre}"
        else:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"
        
    def toString(self):
        from gestion.zona import Zona
        if self._zona != None:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self._zona.getNombre()} en el {self._zona.getZoo().getNombre}"
        else:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"
        
    

