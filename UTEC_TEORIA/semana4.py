# contandor = 1

# while contandor <= 5:
    # print(contandor, end=" ")
    # contandor += 1


# limite = int(input("Limite: "))
# suma = 0
# contador = 2
# while contador <= limite:
#     suma += contandor
#     contador += 2

# print(suma)




def hallarSuma(nter: int) -> int:
    suma = 0
    contador = 0
    

    while contador <= nter:
        
        suma += contador**5 
        contador += 1
        print(suma)
        print(contador)

    return suma

nter = int(input("Número de terminos "))
print(hallarSuma(nter))


