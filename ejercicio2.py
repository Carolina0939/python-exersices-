numero = int(input("Ingrese un número: "))
contador = 0
for i in range(0, numero):
    contador += i + 1
print(f"La suma de los números asta {numero} es: {contador}")

frutas = ["lechuga", "tomate", "cebolla"]
for fruta in frutas:
    print(fruta)

palabra = 'Hola'
print(palabra[0], palabra [3])