# ListaSonora — diseño previo (B3)

Borrador de inicio. Quedan por completar los TAD, los diagramas, el pseudocódigo, el análisis de costes y el plan de pruebas antes de preparar el PDF de entrega.

## 1. Qué tiene que hacer el programa

ListaSonora es un reproductor de música por consola para la cafetería. Al arrancar lee un catálogo de canciones desde un CSV y después ejecuta los comandos de otro fichero. El catálogo no cambia durante la sesión, pero la lista de reproducción sí: se pueden añadir y quitar canciones, avanzar, retroceder, ordenar e invertir.

Además, hay que recordar las canciones que han sonado, permitir deshacer eliminaciones y atender las peticiones del público por orden de llegada. Una misma canción puede aparecer varias veces en la lista.

La canción actual se identifica por su posición en la lista. Si la lista se ordena o invierte, la referencia actual debe seguir apuntando al mismo nodo, aunque este cambie de lugar. Cuando se añade la primera canción, pasa a ser la actual, pero todavía no se guarda en el historial.

## 2. Estructuras elegidas

| Datos | Estructura | Por qué | Alternativa descartada |
|---|---|---|---|
| Lista de reproducción | Lista doblemente enlazada | Desde la canción actual se puede avanzar o retroceder y, teniendo su nodo, insertar después o eliminarlo en O(1). | Una lista simplemente enlazada facilita avanzar, pero para encontrar el anterior hay que recorrer desde el principio, O(n). |
| Historial | Pila enlazada | La última canción que ha sonado es la primera que se consulta: orden LIFO. Apilar y desapilar cuestan O(1). | Una cola sacaría primero la canción más antigua, justo el orden contrario. |
| Eliminaciones | Otra pila enlazada | Permite recuperar primero la última eliminación. Se guarda la canción y su posición anterior. | Una cola recuperaría primero la eliminación más antigua. |
| Peticiones | Cola enlazada con frente y final | Se atienden en orden de llegada (FIFO). Con ambas referencias se puede encolar y desencolar en O(1). | Una pila atendería antes la última petición recibida. |
| Catálogo | Array (`list` de Python) ordenado por id | Como no cambia durante la sesión, se ordena al cargar y se consulta mediante búsqueda binaria, O(log m). | En una lista enlazada acceder al elemento central cuesta O(m), por lo que no se aprovecha igual la búsqueda binaria. |

Aquí **n** es el número de canciones en la lista y **m** el del catálogo. La ordenación inicial por inserción del catálogo puede costar O(m²); se hace una vez al arrancar.

## 3. Primeros diagramas de la lista doble

Cada nodo tiene un dato (canción), una referencia `ant` y otra `sig`. La lista guarda `primero`, `ultimo` y el número de elementos `n`. No es circular: el anterior del primero y el siguiente del último son `None`.

### Insertar X después de A, en medio

Antes (`n = 2`):

```text
primero                                ultimo
   |                                      |
   v                                      v
 None <- [ A ] <----------------------> [ B ] -> None
```

Asignaciones, suponiendo que `nuevo` ya es el nodo X:

```text
1. nuevo.ant = A
2. nuevo.sig = A.sig       # todavía apunta a B
3. A.sig.ant = nuevo       # B.ant pasa a apuntar a X
4. A.sig = nuevo
5. n = n + 1
```

Después (`n = 3`):

```text
primero                                           ultimo
   |                                                 |
   v                                                 v
 None <- [ A ] <--------> [ X ] <----------------> [ B ] -> None
```

El orden importa: antes de cambiar `A.sig` hay que conservar el acceso a B para actualizar su referencia `ant`.

### Insertar X después del último A

Antes (`n = 1`):

```text
primero, ultimo
       |
       v
 None <- [ A ] -> None
```

```text
1. nuevo.ant = A
2. nuevo.sig = None
3. A.sig = nuevo
4. ultimo = nuevo
5. n = n + 1
```

Después (`n = 2`):

```text
primero                    ultimo
   |                          |
   v                          v
 None <- [ A ] <----------> [ X ] -> None
```

**Pendiente:** dibujar la inserción en lista vacía; los cuatro casos de eliminación; la inversión de tres nodos; y los casos de la cola. Cada uno debe mostrar antes, después y orden de asignaciones.

## 4. Primeras preguntas para el equipo

- Confirmar con el profesorado el tamaño del grupo: el enunciado indica 3/4 personas, aunque más adelante menciona una pareja.
- Acordar cómo repartir los TAD, diagramas y pruebas. El reparto final debe reflejar el trabajo que haga cada integrante.
- Revisar juntos el ejemplo del anexo B, especialmente qué canciones entran en el historial y en qué posición se restaura una eliminación.

## Pendiente para la entrega

- Especificación completa de los cuatro TAD, con precondiciones, postcondiciones y errores.
- Resto de diagramas y pseudocódigo solicitado.
- Casos base, pasos recursivos, terminación y profundidad de D1–D5.
- Costes de cada comando, en mejor y peor caso.
- Al menos 12 pruebas con comandos y salida esperada escrita a mano.
- Reparto y calendario; preparar el PDF final de máximo cinco páginas, sin contar anexos de pseudocódigo.
