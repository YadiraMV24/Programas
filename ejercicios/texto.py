texto = input("Introduce un texto: ")

numero_letras = len([letra for letra in texto if letra.isalpha()])

print(f"El texto tiene {numero_letras} letras. ")

