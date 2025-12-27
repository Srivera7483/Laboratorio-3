# ==========================
# Ejercicio 4
# Crear un iterador que recorra una lista de cadenas y devuelva cada cadena en mayúsculas
# ==========================
palabras = ["python", "java", "ruby", "go"]
iterador = iter(palabras)

try:
    while True:
        palabra = next(iterador)
        print(palabra.upper())
except StopIteration:
    pass