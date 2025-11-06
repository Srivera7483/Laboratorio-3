# ==========================
# Ejercicio 2
# Filtrar las palabras que empiezan con “p” de la lista ["perro","gato","pato","hamster"]
# ==========================
animales = ["perro", "gato", "pato", "hamster"]
empiezan_con_p = list(filter(lambda x: x.startswith("p"), animales))
print(empiezan_con_p)