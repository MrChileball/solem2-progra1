from datetime import datetime
import heapq

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
        print("\n  Puntos de distribución:")
        for i, punto in enumerate(locations, 1):
            disponibles = sum(b.disponible for b in punto.bicicletas)
            print(f"{i}. {punto.nombre} (Bicis: {disponibles}/{len(punto.bicicletas)})")
    
    def ubicacion(self, action, locations):
        if action == "add":
            from utils.data import tiempoEstimado
            nombre = input("Nombre del nuevo punto: ")
            bicis = int(input("Número de bicicletas: "))
            conexiones = {}
            print("\nConfigurar conexiones directas (ingresa 'fin' para terminar):")
            while True:
                comuna_vecina = input("  - Nombre de comuna conectada: ").strip().lower()
                if comuna_vecina == "fin":
                    break
                if comuna_vecina not in tiempoEstimado:
                    print(f"    ¡Error: '{comuna_vecina}' no existe en el sistema!")
                    continue
                tiempo = int(input(f"  - Tiempo de viaje a {comuna_vecina} (min): "))
                conexiones[comuna_vecina] = tiempo
            
            # Paso 2: Crear el punto y actualizar el grafo
            nuevo_punto = PuntoDistribucion(nombre, f"loc{len(locations)+1:03d}", bicis, 0)
            locations.append(nuevo_punto)
            
            # Actualizar tiempoEstimado (bidireccional)
            tiempoEstimado[nombre] = conexiones
            for vecino, tiempo in conexiones.items():
                tiempoEstimado[vecino][nombre] = tiempo  # Conexión inversa
            
            print(f"\n  Punto '{nombre}' añadido con éxito!")
            print(f"  Conexiones: {conexiones}")
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
        comuna= input("Comuna de entrega: ")
        
        punto = self._seleccionar_punto(locations, comuna)
        if not punto:
            print(" No hay puntos de distribución disponibles.")
            return
        
        bicicleta = self._asignar_bicicleta(punto)
        if not bicicleta:
            print(" No hay bicicletas disponibles en este punto.")
            # Buscar comuna cercana con bicis disponibles
            punto_alternativo = self._buscar_comuna_cercana(locations, comuna)
            if punto_alternativo:
                print(f" Asignando bicicleta desde {punto_alternativo.nombre} (comuna cercana)")
                bicicleta = self._asignar_bicicleta(punto_alternativo)
                if bicicleta:
                    punto = punto_alternativo
                else:
                    print(" No hay bicicletas disponibles en comunas cercanas.")
                    return
            else:
                print(" No hay comunas cercanas con bicicletas disponibles.")
                return
        
        pedido = {
            'id': len(pedidos) + 1,
            'cliente': nombre,
            'rut': f"{rut}-{dv}",
            'direccion': direccion,
            'descripcion': descripcion,
            'prioridad': prioridad,
            'punto_distribucion': punto.nombre,
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
    
 
    def _seleccionar_punto(self, locations, comuna):
        for p in locations:
            if p.nombre == comuna:
                return p
        return None
    
    def _buscar_comuna_cercana(self, locations, comuna_objetivo):
    
        from utils.data import tiempoEstimado
    
        # 1. Identificar puntos con bicicletas disponibles
        puntos_con_bicis = [
            p for p in locations 
            if any(b.disponible for b in p.bicicletas)
        ]
    
        if not puntos_con_bicis:
            return None
    
        # 2. Inicializar estructuras para Dijkstra
        distancias = {comuna: float('inf') for comuna in tiempoEstimado}
        distancias[comuna_objetivo] = 0
        cola = [(0, comuna_objetivo)]
        visitados = set()

        # 3. Diccionario para reconstruir rutas (opcional)
        previos = {comuna: None for comuna in tiempoEstimado}

        while cola:
            tiempo_actual, comuna_actual = heapq.heappop(cola)
        
            # Si encontramos una comuna con bicis, la retornamos inmediatamente
            # (gracias a la cola de prioridad, será la de menor distancia)
            for p in puntos_con_bicis:
                if p.nombre == comuna_actual:
                    return p
        
            if comuna_actual in visitados:
                continue
            visitados.add(comuna_actual)

            # Explorar vecinos
            for vecino, tiempo in tiempoEstimado[comuna_actual].items():
                tiempo_nuevo = tiempo_actual + tiempo
                if tiempo_nuevo < distancias[vecino]:
                    distancias[vecino] = tiempo_nuevo
                    previos[vecino] = comuna_actual
                    heapq.heappush(cola, (tiempo_nuevo, vecino))
    
    # Si no se encontró ninguna comuna accesible con bicis
        return None
    
    def _asignar_bicicleta(self, punto):
        return next((b for b in punto.bicicletas if b.disponible), None)
    
    def list_orders(self):
        from utils.data import pedidos
        
        if not pedidos:
            print(" No hay pedidos registrados.")
            return
        
        print("\n Lista de Pedidos ")
        for pedido in pedidos:
            print(f"   | PEDIDO {pedido['id']}: \n "
                  f"Cliente: {pedido['cliente']}, RUT: {pedido['rut']}, \n "
                  f"Dirección: {pedido['direccion']}, Descripción: {pedido['descripcion']}, \n "
                  f"Prioridad: {pedido['prioridad']}, Comuna bodega: {pedido['punto_distribucion']},\n "
                  f"Bicicleta: {pedido['bicicleta']}, Estado: {pedido['estado']}, Fecha: {pedido['fecha']}")

def validar_rut(rut, dv):
    rut_limpio = ''.join(filter(str.isdigit, rut))
    dv_limpio = dv.upper().strip()

    if not rut_limpio or not dv_limpio or len(rut_limpio) < 7 or dv_limpio not in '0123456789K':
        return False

    factores = [2, 3, 4, 5, 6, 7, 2, 3]
    suma = sum(int(d) * factores[i % 8] for i, d in enumerate(rut_limpio[::-1]))
    dv_calculado = {10: 'K', 11: '0'}.get(11 - (suma % 11), str(11 - (suma % 11)))

    return dv_limpio == dv_calculado