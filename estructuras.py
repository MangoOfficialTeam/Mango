class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.ant = None
        self.sig = None


class ListaDoble:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.n = 0

    def es_vacia(self):
        return self.n == 0

    def __len__(self):
        return self.n

    def insertar_final(self, dato):
        nuevo = Nodo(dato)
        nuevo.ant = self.ultimo
        if self.ultimo is None:
            self.primero = nuevo
        else:
            self.ultimo.sig = nuevo
        self.ultimo = nuevo
        self.n += 1
        return nuevo

    def insertar_despues(self, nodo, dato):
        if self.es_vacia() and nodo is None:
            return self.insertar_final(dato)
        if nodo is None:
            raise ValueError("Se necesita un nodo de la lista")
        nuevo = Nodo(dato)
        nuevo.ant = nodo
        nuevo.sig = nodo.sig
        if nodo.sig is None:
            self.ultimo = nuevo
        else:
            nodo.sig.ant = nuevo
        nodo.sig = nuevo
        self.n += 1
        return nuevo

    def buscar(self, id):
        actual = self.primero
        while actual is not None:
            if actual.dato.id == id:
                return actual
            actual = actual.sig
        return None
