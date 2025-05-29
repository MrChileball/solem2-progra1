class Bicicleta:
    def __init__(self, id_bicicleta):
        self.id_bicicleta = id_bicicleta

class PuntoDistribucion:
    def __init__(self, nombre, id_punto, bicicletas, tiempo_reparto_por_bloque):
        self.nombre = nombre
        self.id_punto = id_punto
        self.bicicletas = bicicletas
        self.tiempo_reparto_por_bloque = tiempo_reparto_por_bloque


#Clase warehouse, permite acceder a funciones que añaden o eliminan ubicaciones/bicicletas
class Warehouse:
    def status(self, locations):
        if not locations:
            print("No hay puntos de distribución registrados.")
            return
        
        for punto in locations:
            print(f"\n📍 Punto: {punto.nombre} (ID: {punto.id_punto})")
            print(f"🚲 Bicicletas disponibles: {len(punto.bicicletas)}")
            print(f"⏱ Tiempo de reparto: {punto.tiempo_reparto_por_bloque} minutos")
            
            for bici in punto.bicicletas:
                print(f"   - ID Bicicleta: {bici.id_bicicleta}")
        print("\nFin del reporte")

    def ubicacion(self, value, locations):
        if value == "add":
            print("\n🆕 Añadir nuevo punto de distribución")
            nombre = input("Nombre del punto: ")
            id_punto = input("ID del punto (ej: loc004): ")
            tiempo = int(input("Tiempo de reparto por bloque (minutos): "))
            
            nuevo_punto = PuntoDistribucion(
                nombre=nombre,
                id_punto=id_punto,
                bicicletas=[],
                tiempo_reparto_por_bloque=tiempo
            )
            locations.append(nuevo_punto)
            print(f"✅ Punto {nombre} ({id_punto}) añadido exitosamente!")
            return locations
            
        elif value == "remove":
            print("\n🗑 Eliminar punto de distribución")
            id_punto = input("ID del punto a eliminar: ")
            
            for punto in locations:
                if punto.id_punto == id_punto:
                    locations.remove(punto)
                    print(f"✅ Punto {id_punto} eliminado exitosamente!")
                    return locations
            
            print(f"❌ No se encontró el punto con ID {id_punto}")
            return locations

    def bicicleta(self, value, locations):
        if value == "add":
            print("\n➕ Añadir bicicleta")
            id_punto = input("ID del punto destino: ")
            id_bici = input("ID de la bicicleta (ej: B0P9999): ")
            
            for punto in locations:
                if punto.id_punto == id_punto:
                    nueva_bici = Bicicleta(id_bici)
                    punto.bicicletas.append(nueva_bici)
                    print(f"✅ Bicicleta {id_bici} añadida a {punto.nombre}!")
                    return locations
            
            print(f"❌ No se encontró el punto con ID {id_punto}")
            return locations
            
        elif value == "remove":
            print("\n➖ Eliminar bicicleta")
            id_punto = input("ID del punto: ")
            id_bici = input("ID de la bicicleta a eliminar: ")
            
            for punto in locations:
                if punto.id_punto == id_punto:
                    for bici in punto.bicicletas:
                        if bici.id_bicicleta == id_bici:
                            punto.bicicletas.remove(bici)
                            print(f"✅ Bicicleta {id_bici} eliminada de {punto.nombre}!")
                            return locations
                    print(f"❌ No se encontró la bicicleta con ID {id_bici}")
                    return locations
            
            print(f"❌ No se encontró el punto con ID {id_punto}")
            return locations

class Order:
    def create(self):
        #Hay que añadir para el usuario ingrese nombre, pedido, lugar, prioridad y peso, entre otros
        #Además, debe pedir rut para comprobarlo+
        print("Oli")