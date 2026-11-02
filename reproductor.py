from algoritmos import busqueda_binaria_iter
from estructuras import ListaDoble


class Reproductor:
    def __init__(self, catalogo):
        self.catalogo = catalogo
        self.lista = ListaDoble()
        self.actual = None

    def ejecutar(self, linea):
        partes = linea.split(maxsplit=1)
        comando = partes[0]
        argumento = partes[1] if len(partes) > 1 else ""

        if comando in ("AGREGAR", "INSERTAR"):
            cancion = busqueda_binaria_iter(self.catalogo, argumento)
            if cancion is None:
                print(f"Error: {argumento} no existe en el catálogo")
                return
            if comando == "AGREGAR":
                nodo = self.lista.insertar_final(cancion)
                print(f"Añadida: {cancion}")
            else:
                nodo = self.lista.insertar_despues(self.actual, cancion)
                print(f"Insertada tras la actual: {cancion}")
            if self.actual is None:
                self.actual = nodo
        elif comando == "MOSTRAR":
            if self.lista.es_vacia():
                print("(lista vacía)")
                return
            print(f"Lista ({len(self.lista)} canciones):")
            nodo = self.lista.primero
            posicion = 1
            while nodo is not None:
                marca = "*" if nodo is self.actual else " "
                print(f"{marca} {posicion}. {nodo.dato}")
                nodo = nodo.sig
                posicion += 1
        else:
            print(f"Comando desconocido: {comando}")
