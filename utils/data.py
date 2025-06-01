

from utils.methods import PuntoDistribucion



locations = [
    PuntoDistribucion(
        nombre="santiago",
        id_punto="loc001",
        bicicletas= 10,
        tiempo_reparto_por_bloque=30 
    ),
    PuntoDistribucion(
        nombre="ñuñoa",
        id_punto="loc002",
        bicicletas=10,
        tiempo_reparto_por_bloque=45
    ),
    PuntoDistribucion(
        nombre="providencia",
        id_punto="loc003",
        bicicletas=10,
        tiempo_reparto_por_bloque=20
    ),
    PuntoDistribucion(
        nombre="san joaquin",
        id_punto="loc004",
        bicicletas=10,
        tiempo_reparto_por_bloque=17
    )
]

pedidos = []
