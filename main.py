from functools import reduce
import random
import os

class Juego:
    def __init__(self):
        self.path_completo = f"{'mapas'}/{random.choice( os.listdir('./mapas') )}"
        self.mapa_str = self.read_map( self.path_completo )
        self.mapa_matriz = self.cadenaMatriz( self.mapa_str )

    def cadenaMatriz(self,data):
        matriz = list(map(list, map(str.strip, data.split('\n') )))
        return matriz

    def read_map(self, filename):
        file = open(filename, 'r')
        lines = file.readlines()
        map_data = reduce(lambda x, y: x + y, lines)
        return map_data
    
    def getMapaStr(self):
        return self.mapa_str
    
    def getMapaMatriz(self):
        return self.mapa_matriz

juego = Juego()

print(juego.getMapaStr())