from utils.data import locations, pedidos
from utils.methods import Warehouse, Order

def main():
    warehouse = Warehouse()
    order_system = Order(warehouse)

    menu_principal = """
    ============== EcoLogistik ==============
    1. Ver puntos de distribución
    2. Gestionar ubicaciones
    3. Ver pedidos
    4. Crear pedido
    0. Salir
    ========================================
    """

    submenu_ubicaciones = """
    1. Añadir Ubicación
    2. Eliminar ubicación
    0. Volver
    """

    current_locations = locations.copy()

    while True:
        print(menu_principal)
        opcion = input("Seleccione una opción: ")

        if opcion == "0":
            print("¡Hasta pronto!")
            break
            
        elif opcion == "1":
            warehouse.status(current_locations)
            
        elif opcion == "2":
            while True:
                print(submenu_ubicaciones)
                sub_opcion = input("Seleccione una opción: ")
                
                if sub_opcion == "0":
                    break
                elif sub_opcion in ["1", "2"]:
                    action = "add" if sub_opcion == "1" else "remove"
                    current_locations = warehouse.ubicacion(action, current_locations)
                else:
                    print("Opción no válida")
                    
        elif opcion == "3":
            order_system.list_orders()
        
        elif opcion == "4":
            order_system.create(current_locations)
        
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()