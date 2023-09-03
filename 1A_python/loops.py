# ITERAR LISTAS Y TUPLAS (funcionan igual)

animales = ["perro", "gato", "loro"]
numeros = [1, 2, 3, 4, 5]
diccionario = {
    "nombre": "martin",
    "edad": 22,
    "altura": 1.69
}

# continue y break
for i in numeros:
    if i == 2:
        continue
    if i == 4:
        break
    print(i)

# linkeados respectivamente
for animal, numero in zip(animales, numeros):
    print(f"animal: {animal}")
    print(f"numero: {numero}")
else: # siempre se muestra una vez y el "break" saltea el "else"
    print("fin")

# forma incorrecta de recorrer por index
for i in range(len(animales)):
    print(animales[i])

# forma eficiente de recorrer por index (enumerate -> tuplas pares)
for animal in enumerate(animales):
    print(f"indice: {animal[0]}")
    print(f"valor: {animal[1]}")

# recorrer diccionario (items -> tuplas -> key-value)
for data in diccionario.items():
    print(f"key: {data[0]}")
    print(f"value: {data[1]}")

# "for" en una linea
numeros_doble = [i*2 for i in numeros]
print(numeros_doble)