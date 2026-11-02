# Mango

**ListaSonora** — caso final de Programación con Estructuras Lineales (B3 + B4), Ingeniería Informática, Universidad Europea. Reproductor de música por consola con lista doblemente enlazada, pila, cola y catálogo con búsqueda binaria, todo implementado a mano.

Equipo: [@marcosdeaza](https://github.com/marcosdeaza) · [@Alvaro-Rovira](https://github.com/Alvaro-Rovira) · [@dreyaaaaaaaaaaaaa](https://github.com/dreyaaaaaaaaaaaaa)

## Roadmap

### Fase 0 — Setup
- [x] Repo creado, equipo con acceso
- [x] `datos/catalogo_rap.csv` de prueba (Carti, Kendrick, Drake y compañía)
- [x] Archivos iniciales: `cancion.py`, `estructuras.py`, `algoritmos.py`, `reproductor.py`, `main.py`

### Fase 1 — Diseño (entrega B3, semana 1 dic)
- [ ] TADs: Cancion, ListaReproduccion, Pila, Cola (operaciones + pre/postcondiciones)
- [ ] Diagramas de punteros: insertar_despues (3 casos), eliminar (4 casos), invertir (3 nodos), encolar/desencolar
- [ ] Pseudocódigo: insertar_despues, eliminar, invertir, búsqueda binaria recursiva, inserción y mergesort sobre lista
- [ ] Diseño recursivo D1–D5 (caso base / caso general / profundidad)
- [ ] Previsión de costes por comando
- [ ] Plan de pruebas: 12+ casos con comandos y salida esperada a mano
- [ ] PDF final: `B3_deAza_Rovira_Benoit.pdf` (máx. 5 páginas)

### Fase 2 — Estructuras base
- [ ] `Nodo`, `ListaDoble` (insertar_final, insertar_despues, insertar_en, eliminar, buscar, indice)
- [ ] `Pila`, `Cola` enlazadas (nada de `list`/`deque`)
- [ ] `ordenar_insercion_array` sobre el catálogo + `busqueda_binaria_iter`/`_rec`
- [ ] Tests unitarios de todos los casos borde (Parte B)

### Fase 3 — El reproductor
- [ ] Las 9 reglas del apartado C.1
- [ ] Los 15 comandos con mensajes exactos (C.2)
- [ ] `main.py` reproduce el ejemplo del Anexo B carácter a carácter

### Fase 4 — Recursividad, búsqueda y orden
- [ ] D1 (duracion_total rec/iter), D2 (canciones_de), D3 (invertir), D4 (binaria rec), D5 (mergesort)
- [ ] `ordenar_insercion` y `ordenar_merge` sobre la lista — estables, reenlazando nodos

### Fase 5 — Eficiencia + informe (entrega B4, semana 21 dic)
- [ ] `eficiencia/experimentos.py`: secuencial vs binaria, inserción vs mergesort, recursiva vs iterativa, insertar en medio vs `list.insert`
- [ ] Gráficas reales en `eficiencia/graficas/`
- [ ] `informe.pdf`: cambios vs B3, costes revisados, experimentos, respuestas D/E/F/G, resultado de pruebas, limitaciones

### Fase 6 — Pulido (lo que lo hace de 10)
- [ ] Código modular, nombres claros, sin dead code
- [ ] Cobertura de tests real, no solo el ejemplo del Anexo B
- [ ] Alguna ampliación opcional si sobra tiempo (ALEATORIO, REPETIR, quicksort...)
- [ ] Revisar que nada usa `sorted()`, `list.sort()`, `bisect`, `list.index()` ni `in` sobre el catálogo — es 0 automático si se cuela

## Reglas que no se pueden romper

- `ListaDoble`, `Pila`, `Cola`: implementación propia con nodos, nada de `list`/`deque`/`dict` para guardar sus elementos.
- Catálogo: sí es `list` de Python (el array permitido).
- Prohibido `sorted()`, `list.sort()`, `bisect`, `list.index()`, `in` sobre el catálogo.
- Ordenar la lista enlazada = reenlazar nodos, nunca intercambiar datos ni volcar a un array.
- Módulos permitidos: `sys`, `time`, `random`, `csv`, `unittest`, y solo para gráficas `matplotlib`.

## Estado actual

Primera versión en construcción: carga el catálogo CSV, lo ordena por inserción y permite probar `AGREGAR`, `INSERTAR` y `MOSTRAR`. Los demás comandos, la pila, la cola, las pruebas completas y el diseño B3 están pendientes. No es todavía la entrega final.

```text
Mango/
├── main.py             # lectura de archivos y ejecución
├── cancion.py          # datos y formato de una canción
├── estructuras.py      # nodos y lista doble (parcial)
├── algoritmos.py       # inserción y búsqueda del catálogo
├── reproductor.py      # estado y primeros comandos
├── datos/              # catálogo y comandos de ejemplo
└── pruebas/            # pruebas iniciales
```

## Ejecutar

```bash
python3 main.py datos/catalogo_rap.csv datos/comandos_ejemplo.txt
python3 -m unittest discover -s pruebas
```
