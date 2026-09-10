# parametro = 0
# while parametro < 7:
#     parametro += 1
    # print("UTEC")

# contador  = 0
# variable = 7

# while 15 > contador:
#     contador += 1
#     print(f"{contador}-{variable*contador}")


# variable = int(input("Numero: "))
# print("")
# contador = 0
# while 10>contador:
#     contador+=1
#     print(f"{variable} x {contador} = {variable*contador}")


# n = int(input("Numero[1-500]: "))
# contador = 0
# db = True
# while db == True:
#     if n <= 500 and n>=1:
#         db = False
#     else:
#         n = int(input("Numero[1-500]: "))
      
# while n > contador:
#     contador += 1

#     if contador % 4 == 0 and contador%6 == 0:
#             print(f"{contador} Tictac")
#     elif contador % 4 == 0:
#             print(f"{contador} Tic")
#     elif contador % 6 == 0:
#             print(f"{contador} Tac")
#     else:
#         print(contador)


# print("Fin")

# def hallarFactorial(num:int)->int:
#     resultado = 1
#     contador = 0
#     while num > contador:
#         contador += 1
#         resultado *= contador

#     return resultado

def esPerfecto(numero:int)->str:
    numero_maximo = numero // 2
    contador = 0
    suma = 0
    

    while numero <= 2:
        numero = int(input("Numero[ mayor a 1]:"))
         

    
    while contador <= numero_maximo:
        contador += 1
        if numero % contador == 0:
            suma += contador

    if numero == suma:
            return "Es perfecto"
    else:
        return "No es perfecto"



numero = int(input("Numero[ mayor a 1]: "))
print(esPerfecto(numero))






