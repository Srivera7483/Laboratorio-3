# ==========================
# Ejercicio 1
# Sumar todos los elementos de la lista [5,10,15,20] usando reduce()
# ==========================
from functools import reduce

numeros = [5, 10, 15, 20]
suma_total = reduce(lambda x, y: x + y, numeros)
print(suma_total)