print("Conversión de decimal a hexadecimal".upper())

decimal = int(input("Ingresa el número: "))

lista = []

while decimal != 0:
    residuo = decimal % 16

    decimal = decimal // 16

    #---- condicion

    if residuo == 10:
        lista.insert(0,"A")
    elif residuo == 11:
        lista.insert(0, "B")
    elif residuo == 12:
        lista.insert(0, "C")
    elif residuo == 13:
        lista.insert(0, "D")
    elif residuo == 14:
        lista.insert(0, "E")
    elif residuo == 15:
        lista.insert(0, "F")

    else:
         lista.insert(0,residuo)  

print(*lista)
   