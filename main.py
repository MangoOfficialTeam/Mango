import csv
import sys

from algoritmos import ordenar_insercion_array
from cancion import Cancion
from reproductor import Reproductor


def cargar_catalogo(ruta):
    canciones = []
    with open(ruta, encoding="utf-8", newline="") as archivo:
        for fila in csv.DictReader(archivo, delimiter=";"):
            canciones.append(Cancion(fila["id"], fila["titulo"], fila["artista"], int(fila["duracion"])))
    ordenar_insercion_array(canciones, lambda cancion: cancion.id)
    return canciones


def main():
    if len(sys.argv) != 3:
        print("Uso: python main.py catalogo.csv comandos.txt")
        return 1
    try:
        catalogo = cargar_catalogo(sys.argv[1])
        with open(sys.argv[2], encoding="utf-8") as archivo:
            reproductor = Reproductor(catalogo)
            for linea in archivo:
                linea = linea.strip()
                if linea:
                    print(f"> {linea}")
                    reproductor.ejecutar(linea)
    except (OSError, ValueError, KeyError) as error:
        print(f"Error al leer los archivos: {error}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
