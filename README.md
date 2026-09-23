# Mango

**ListaSonora** — caso final de Programación con Estructuras Lineales (B3 + B4), Ingeniería Informática, Universidad Europea.

Reproductor de música por consola con lista de reproducción doblemente enlazada, pila (historial + deshacer), cola (peticiones) y catálogo ordenado con búsqueda binaria, todo implementado a mano según el enunciado del caso.

## Equipo

- Marcos de Aza — [@marcosdeaza](https://github.com/marcosdeaza)
- Álvaro Rovira — [@Alvaro-Rovira](https://github.com/Alvaro-Rovira)
- Ange Benoit — [@dreyaaaaaaaaaaaaa](https://github.com/dreyaaaaaaaaaaaaa)

## Entregables

- **B3** — documento de diseño (TADs, diagramas de punteros, pseudocódigo, previsión de costes, plan de pruebas).
- **B4** — implementación (`main.py`, `cancion.py`, `estructuras.py`, `algoritmos.py`, `reproductor.py`), pruebas unitarias, estudio de eficiencia con gráficas, e informe.

## Reglas clave del enunciado

- `ListaDoble`, `Pila`, `Cola`: implementación propia con nodos enlazados. Nada de `list`, `collections.deque` ni `dict` para guardar sus elementos.
- Catálogo: se guarda en una `list` de Python (el array permitido).
- Prohibido `sorted()`, `list.sort()`, `bisect`, `list.index()`, `in` sobre el catálogo.
- Ordenar la lista enlazada = reenlazar nodos, nunca intercambiar datos ni volcar a un array.
- Módulos permitidos: `sys`, `time`, `random`, `csv`, `unittest` y, solo para gráficas, `matplotlib`.

## Ejecutar (cuando haya código)

```bash
python3 main.py catalogo.csv comandos.txt
```

## Pruebas

```bash
python3 -m unittest discover -s pruebas
```
