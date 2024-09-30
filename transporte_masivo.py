import heapq

# Base de conocimiento: mapa del sistema de transporte con tiempos entre estaciones
transporte_masivo = {
    "A": {"B": 10, "C": 15},
    "B": {"A": 10, "D": 5, "E": 7},
    "C": {"A": 15, "F": 10},
    "D": {"B": 5, "E": 3, "G": 12},
    "E": {"B": 7, "D": 3, "F": 4, "G": 10},
    "F": {"C": 10, "E": 4, "H": 8},
    "G": {"D": 12, "E": 10, "H": 7},
    "H": {"F": 8, "G": 7}
}

# Función para encontrar la mejor ruta usando el algoritmo de Dijkstra
def dijkstra(transporte, inicio, destino):
    cola = [(0, inicio)]  # Cola de prioridad (tiempo, nodo actual)
    visitados = set()
    costos = {inicio: 0}  # Diccionario de costos mínimos
    rutas = {inicio: [inicio]}  # Rutas mínimas desde el inicio

    while cola:
        costo_actual, nodo_actual = heapq.heappop(cola)

        if nodo_actual in visitados:
            continue

        visitados.add(nodo_actual)

        if nodo_actual == destino:
            return costo_actual, rutas[nodo_actual]

        for vecino, tiempo in transporte[nodo_actual].items():
            nuevo_costo = costo_actual + tiempo
            if vecino not in costos or nuevo_costo < costos[vecino]:
                costos[vecino] = nuevo_costo
                heapq.heappush(cola, (nuevo_costo, vecino))
                rutas[vecino] = rutas[nodo_actual] + [vecino]

    return float('inf'), []

# Ejecución de la búsqueda de la mejor ruta entre dos estaciones
if __name__ == "__main__":
    print("El programa ha comenzado...")
    inicio = input("Ingrese la estación de inicio: ")
    destino = input("Ingrese la estación de destino: ")
    
    if inicio in transporte_masivo and destino in transporte_masivo:
        costo, ruta = dijkstra(transporte_masivo, inicio, destino)
        if ruta:
            print(f"La mejor ruta de {inicio} a {destino} es: {ruta} con un costo de {costo} minutos")
        else:
            print(f"No existe una ruta desde {inicio} hasta {destino}.")
    else:
        print("Estación de inicio o destino no válida.")