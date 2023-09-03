# COMPLEX DATA TYPES / COMPUND DATA STRUCTURES

tupla = (4, "5", 6.2, True, 6.2)
# elementos: ordenados(index) - repetibles - cualquier tipo
# tupla = tuple(objeto_iterable)
# objeto_iterable -> lista, tupla, conjunto, string, diccionarios (keys)
print(dir(tupla))
# 'count', 'index'

lista = [7, "8", 9.2]
# elementos: ordenados(index) - repetibles - cualquier tipo
# lista = list(objeto_iterable)
# objeto_iterable -> lista, tupla, conjunto, string, diccionarios (keys)
print(dir(lista))
# 'append', 'clear', 'copy', 'count', 'extend', 'index',
# 'insert', 'pop', 'remove', 'reverse', 'sort'

conjunto = {1, "2", 3.2}
# elementos: desordenados(no index) - irrepetibles - no booleanos
# conjunto = set(objeto_iterable)
# objeto_iterable -> lista, tupla, conjunto, string, diccionarios (keys)
print(dir(conjunto))
# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection',
# 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove',
# 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

diccionario = {
    "nombre": "martin",
    "edad": 22,
    "altura": 1.69,
    "donante": True,
}
# elementos: ordenados(keys) - irrepetibles - cualquier tipo (keys y values)
# diccionario = dict(secuencia_pares)
# secuencia_pares -> tupla_tuplas, tupla_listas, lista_tuplas, lista_listas
print(dir(diccionario))
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys',
# 'pop', 'popitem','setdefault', 'update', 'values'
















