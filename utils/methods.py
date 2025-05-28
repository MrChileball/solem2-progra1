print("hola")

class Bicicleta:
    def __init__(self, id_bicicleta):
        self.id_bicicleta = id_bicicleta

class PuntoDistribucion:
    def __init__(self, nombre, id_punto, bicicletas, tiempo_reparto_por_bloque):
        self.nombre = nombre
        self.id_punto = id_punto
        self.bicicletas = bicicletas  # Lista de instancias de Bicicleta
        self.tiempo_reparto_por_bloque = tiempo_reparto_por_bloque
