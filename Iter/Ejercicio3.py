# ==========================
# Ejercicio 3
# Clase que genera cuadrados del 1 al 10 sin usar iter(), pero devuelve la lista completa
# ==========================
class Cuadrados:
    def obtener_lista(self):
        lista = []
        for i in range(1, 11):
            lista.append(i ** 2)
        return lista

cuadrados = Cuadrados().obtener_lista()
print(cuadrados)