
from utils.data import locations

menuCommands = """==============00==============
Bienvenido al panel de EcoLogistik!
1. Pan
2. Palta
3. Mayonesa
4. Tomate
5. Pollito
0. salir
==============00==============
"""


while(True):
	print(menuCommands)
	val = int(input("Ingrese un número para continuar (0-5): "))
	print(val)
	if val == 0:
		break
	

# Acceso a los datos (ejemplo)
print(locations[0].nombre)  # "Centro"
print(len(locations[0].bicicletas))  # 3 bicicletas en el punto "Centro"
print(locations[0].bicicletas[0].id_bicicleta)  # 3 bicicletas en el punto "Centro"
print(locations[1].bicicletas[0].id_bicicleta)  # "bike004"
