# ==========================
# Ejercicio 2
# Multiplicar todos los elementos de la lista [2,3,4] usando reduce()
# ==========================
from functools import reduce

numeros = [2, 3, 4]
producto = reduce(lambda x, y: x * y, numeros)
print(producto)
