

from utils.methods import PuntoDistribucion

tiempoEstimado = {
    "santiago": {"ñuñoa": 30, "providencia": 20},
    "ñuñoa": {"santiago": 30, "san joaquin": 45},
    "providencia": {"santiago": 20, "san joaquin": 17},
    "san joaquin": {"providencia": 17, "ñuñoa": 45}
}

locations = [
    PuntoDistribucion(
        nombre="santiago",
        id_punto="loc001",
        bicicletas= 0,
        tiempo_reparto_por_bloque=30 
    ),
    PuntoDistribucion(
        nombre="ñuñoa",
        id_punto="loc002",
        bicicletas=2,
        tiempo_reparto_por_bloque=45
    ),
    PuntoDistribucion(
        nombre="providencia",
        id_punto="loc003",
        bicicletas=1,
        tiempo_reparto_por_bloque=20
    ),
    PuntoDistribucion(
        nombre="san joaquin",
        id_punto="loc004",
        bicicletas=3,
        tiempo_reparto_por_bloque=17
    )
]

pedidos = []
