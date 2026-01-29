print("conversión de binario a decimal".upper())

binario = input("Ingrese el número binario: ")
suma = 0
decremento = len(binario)

for i in range(len(binario)):
    decremento -= 1
    suma = suma + (int(binario[decremento])) * 2**i

print(suma)