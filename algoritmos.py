def ordenar_insercion_array(v, clave):
    for i in range(1, len(v)):
        elemento = v[i]
        j = i - 1
        while j >= 0 and clave(v[j]) > clave(elemento):
            v[j + 1] = v[j]
            j -= 1
        v[j + 1] = elemento


def busqueda_binaria_iter(v, id):
    inicio, fin = 0, len(v) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if v[medio].id == id:
            return v[medio]
        if v[medio].id < id:
            inicio = medio + 1
        else:
            fin = medio - 1
    return None
