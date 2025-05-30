

from utils.methods import Bicicleta, PuntoDistribucion


locations = [
    PuntoDistribucion(
        nombre="Centro",
        id_punto="loc001",
        bicicletas= 10,
        tiempo_reparto_por_bloque=30 
    ),
    PuntoDistribucion(
        nombre="Norte",
        id_punto="loc002",
        bicicletas=10,
        tiempo_reparto_por_bloque=45
    ),
    PuntoDistribucion(
        nombre="Extremo sur",
        id_punto="loc003",
        bicicletas=10,
        tiempo_reparto_por_bloque=85
    )
]

pedidos = []
