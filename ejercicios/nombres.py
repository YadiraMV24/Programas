nombres = []

contador = 0
while contador < 5:
    nombre = input(f"Introduce el nombre {contador + 1}: ")
    nombres.append(nombre)
    contador += 1

print("\nNombres en orden inverso:")
for nombre in reversed (nombres):
    print(nombre)

