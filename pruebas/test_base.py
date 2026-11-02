import unittest

from algoritmos import busqueda_binaria_iter, ordenar_insercion_array
from cancion import Cancion
from estructuras import ListaDoble


class PruebasBase(unittest.TestCase):
    def test_lista_inserta_en_vacia_medio_y_final(self):
        lista = ListaDoble()
        primero = lista.insertar_despues(None, "primero")
        ultimo = lista.insertar_final("último")
        medio = lista.insertar_despues(primero, "medio")
        self.assertEqual(len(lista), 3)
        self.assertIs(lista.primero, primero)
        self.assertIs(lista.ultimo, ultimo)
        self.assertIs(primero.sig, medio)
        self.assertIs(medio.ant, primero)
        self.assertIs(medio.sig, ultimo)
        self.assertIs(ultimo.ant, medio)
        nuevo_ultimo = lista.insertar_despues(ultimo, "nuevo")
        self.assertIs(lista.ultimo, nuevo_ultimo)
        self.assertIsNone(nuevo_ultimo.sig)

    def test_catalogo_ordenado_y_busqueda(self):
        canciones = [Cancion("C3", "t", "a", 1), Cancion("C1", "t", "a", 1), Cancion("C2", "t", "a", 1)]
        ordenar_insercion_array(canciones, lambda c: c.id)
        self.assertEqual([c.id for c in canciones], ["C1", "C2", "C3"])
        self.assertEqual(busqueda_binaria_iter(canciones, "C2").id, "C2")
        self.assertIsNone(busqueda_binaria_iter(canciones, "C4"))
        self.assertIsNone(busqueda_binaria_iter([], "C1"))

    def test_formato_de_duracion(self):
        self.assertEqual(str(Cancion("C1", "Tema", "Artista", 65)), "C1 Tema - Artista (1:05)")
        self.assertEqual(str(Cancion("C2", "Tema", "Artista", 3661)), "C2 Tema - Artista (1:01:01)")


if __name__ == "__main__":
    unittest.main()
