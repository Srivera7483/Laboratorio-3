# ==========================
# Ejercicio 4
# Concatenar todas las cadenas de la lista ["Hola", " ", "Mundo", "!"] usando reduce()
# ==========================
from functools import reduce

palabras = ["Hola", " ", "Mundo", "!"]
frase = reduce(lambda x, y: x + y, palabras)
print(frase)