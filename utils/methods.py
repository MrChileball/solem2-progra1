from datetime import datetime

class Bicicleta:
    def __init__(self, id_bicicleta):
        self.id_bicicleta = id_bicicleta
        self.disponible = True
        self.pedido_asignado = None

class PuntoDistribucion:
    def __init__(self, nombre, id_punto, bicicletas, tiempo_reparto_por_bloque):
        self.nombre = nombre
        self.id_punto = id_punto
        self.bicicletas = [Bicicleta(i) for i in range(1, bicicletas+1)]
        self.tiempo_reparto_por_bloque = tiempo_reparto_por_bloque

class Warehouse:
    def __init__(self):
        pass
        
    def status(self, locations):
        print("\n Puntos de distribución:")
        for i, punto in enumerate(locations, 1):
            disponibles = sum(b.disponible for b in punto.bicicletas)
            print(f"{i}. {punto.nombre} (Bicis: {disponibles}/{len(punto.bicicletas)})")
    
    def ubicacion(self, action, locations):
        if action == "add":
            nombre = input("Nombre del nuevo punto: ")
            bicis = int(input("Número de bicicletas: "))
            tiempo = int(input("Tiempo de reparto por bloque (min): "))
            nuevo_punto = PuntoDistribucion(nombre, f"loc{len(locations)+1:03d}", bicis, tiempo)
            locations.append(nuevo_punto)
            print(f" Punto '{nombre}' añadido!")
        elif action == "remove":
            self.status(locations)
            idx = int(input("Número del punto a eliminar: ")) - 1
            if 0 <= idx < len(locations):
                eliminado = locations.pop(idx)
                print(f" Punto '{eliminado.nombre}' eliminado")
        return locations

class Order:
    def __init__(self, warehouse):
        self.warehouse = warehouse
    
    def create(self, locations):
        from utils.data import pedidos
        
        print("\n Crear nuevo pedido")
        
        rut = input("Ingrese RUT, sin dígito verificador (ej: 12.345.678): ")
        dv = input("Ingrese dígito verificador: ")
        
        if not validar_rut(rut, dv):
            print(" RUT inválido. Por favor ingrese un RUT válido.")
            return
        
        nombre = input("Nombre del cliente: ")
        direccion = input("Dirección de entrega: ")
        descripcion = input("Descripción del pedido: ")
        prioridad = input("Prioridad (normal/urgente): ").lower()
        
        punto = self._seleccionar_punto(locations)
        if not punto:
            print(" No hay puntos de distribución disponibles.")
            return
        
        bicicleta = self._asignar_bicicleta(punto)
        if not bicicleta:
            print(" No hay bicicletas disponibles en este punto.")
            return
        
        pedido = {
            'id': len(pedidos) + 1,
            'cliente': nombre,
            'rut': f"{rut}-{dv}",
            'direccion': direccion,
            'descripcion': descripcion,
            'prioridad': prioridad,
            'punto_distribucion': punto.id_punto,
            'bicicleta': bicicleta.id_bicicleta,
            'estado': 'asignado',
            'fecha': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        pedidos.append(pedido)
        bicicleta.disponible = False
        bicicleta.pedido_asignado = pedido['id']
        
        print(f"\n Pedido creado exitosamente! ID: {pedido['id']}")
        print(f" Bicicleta asignada: {bicicleta.id_bicicleta}")
        print(f" Punto de distribución: {punto.nombre}")
    
    def _seleccionar_punto(self, locations):
        puntos_disponibles = [p for p in locations if any(b.disponible for b in p.bicicletas)]
        return max(puntos_disponibles, key=lambda p: sum(b.disponible for b in p.bicicletas)) if puntos_disponibles else None
    
    def _asignar_bicicleta(self, punto):
        return next((b for b in punto.bicicletas if b.disponible), None)

def validar_rut(rut, dv):
    rut_limpio = ''.join(filter(str.isdigit, rut))
    dv_limpio = dv.upper().strip()

    if not rut_limpio or not dv_limpio or len(rut_limpio) < 7 or dv_limpio not in '0123456789K':
        return False

    factores = [2, 3, 4, 5, 6, 7, 2, 3]
    suma = sum(int(d) * factores[i % 8] for i, d in enumerate(rut_limpio[::-1]))
    dv_calculado = {10: 'K', 11: '0'}.get(11 - (suma % 11), str(11 - (suma % 11)))

    return dv_limpio == dv_calculado