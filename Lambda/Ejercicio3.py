# ==========================
# Ejercicio 3
# Crear una función lambda que reciba una lista y devuelva el primer elemento
# ==========================
primer_elemento = lambda lista: lista[0] if lista else None
print(primer_elemento([4, 8, 15, 16, 23, 42]))