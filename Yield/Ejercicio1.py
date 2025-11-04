# ==========================
# Ejercicio 1
# Generar los primeros 10 números pares usando yield
# ==========================
def generar_pares():
    for i in range(10):
        yield i * 2

for numero in generar_pares():
    print(numero)
