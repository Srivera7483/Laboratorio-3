# ==========================
# Ejercicio 3
# Dada la lista ["uno","dos","tres"], crear otra lista con la longitud de cada palabra usando map()
# ==========================
palabras = ["uno", "dos", "tres"]
longitudes = list(map(lambda x: len(x), palabras))
print(longitudes)