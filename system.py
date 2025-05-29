from utils.data import locations
from utils.methods import Warehouse

warehouse = Warehouse()

menuCommands = """==============00==============
Bienvenido al panel de EcoLogistik!
1. Ver puntos de distribución
2. Gestionar ubicaciones
3. Gestionar bicicletas
0. Salir
==============00==============
"""

submenu_ubicaciones = """
1. Añadir Ubicación
2. Eliminar ubicación
0. Volver
"""

submenu_bicicletas = """
1. Añadir bicicleta
2. Eliminar bicicleta
0. Volver
"""

while True:
    print(menuCommands)
    val = input("Ingrese una opción: ")
    
    if val == "0":
        break
        
    elif val == "1":
        warehouse.status(locations)
        
    elif val == "2":
        while True:
            print(submenu_ubicaciones)
            sub_val = input("Elija una opción: ")
            
            if sub_val == "0":
                break
            elif sub_val in ["1", "2"]:
                action = "add" if sub_val == "1" else "remove"
                locations = warehouse.ubicacion(action, locations)
            else:
                print("Opción no válida")
                
    elif val == "3":
        while True:
            print(submenu_bicicletas)
            sub_val = input("Elija una opción: ")
            
            if sub_val == "0":
                break
            elif sub_val in ["1", "2"]:
                action = "add" if sub_val == "1" else "remove"
                locations = warehouse.bicicleta(action, locations)
            else:
                print("Opción no válida")
    
    else:
        print("Opción no válida")

# Ejemplos de acceso directo a los datos
#print("\nDatos actualizados:")
#print(locations[0].nombre)
#print(len(locations[0].bicicletas))
#if len(locations[0].bicicletas) > 0:
#    print(locations[0].bicicletas[0].id_bicicleta)