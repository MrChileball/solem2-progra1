
# Ejemplo de creación de datos
from utils.methods import Bicicleta, PuntoDistribucion

bicicletas_punto1 = [
    Bicicleta("B0P3001"),
    Bicicleta("B0P3002"),
    Bicicleta("B0P3003")
]

bicicletas_punto2 = [
    Bicicleta("B0P2001"),
    Bicicleta("B0P3002"),
    Bicicleta("B0P3003"),
    Bicicleta("B0P3004")
]
bicicletas_punto3 = [
    Bicicleta("B0P3001"),
    Bicicleta("B0P3002"),
    Bicicleta("B0P3003")
]

locations = [
    PuntoDistribucion(
        nombre="Centro",
        id_punto="loc001",
        bicicletas=bicicletas_punto1,
        tiempo_reparto_por_bloque=30  # minutos
    ),
    PuntoDistribucion(
        nombre="Norte",
        id_punto="loc002",
        bicicletas=bicicletas_punto2,
        tiempo_reparto_por_bloque=45
    ),
    PuntoDistribucion(
        nombre="Extremo sur",
        id_punto="loc003",
        bicicletas=bicicletas_punto3,
        tiempo_reparto_por_bloque=85
    )
]

