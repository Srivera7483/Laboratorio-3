# ==========================
# Ejercicio 2
# Recibir una lista de números y devolver solo los impares con yield
# ==========================
def impares(lista):
    for num in lista:
        if num % 2 != 0:
            yield num

numeros = [1, 2, 3, 4, 5, 6, 7]
for n in impares(numeros):
    print(n)