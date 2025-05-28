# Ejemplo de creación de datos
from .methods import Bicicleta, PuntoDistribucion

bicicletas_punto1 = [
    Bicicleta("bike001"),
    Bicicleta("bike002"),
    Bicicleta("bike003")
]

bicicletas_punto2 = [
    Bicicleta("bike004"),
    Bicicleta("bike005")
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
    )
]
