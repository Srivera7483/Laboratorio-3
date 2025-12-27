# ==========================
# Ejercicio 1
# Crear un contador del 10 al 15 usando iter() y recorrerlo con next()
# ==========================
contador = iter(range(10, 16))

try:
    while True:
        print(next(contador))
except StopIteration:
    pass  # cuando se acaban los elementos, el iterador lanza StopIteration