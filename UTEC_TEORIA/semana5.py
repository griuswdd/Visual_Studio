# for i in range (1,11,1):

#     for j in range(1,11,1):
#         mupltiplo = float(i*j)
#         bool_01 = 3 < len(str(mupltiplo))
        
#         if bool_01 == True:
#             print(mupltiplo,end = "    ")
#         else:
#             print(mupltiplo,end = "     ")          
#     print("")

# n = int(input("numero de filas: "))
# for i in range(n):
#     print(" "*(n-(i+1)),end="")
#     for j in range(i+1):
#         print("#",end= "")
#     print("")


# n = int(input("numero de filas: "))
# for i in range(n):
#     print(" "*(n-(i+1)),end="")
#     for j in range(i+1):
#         print(j+1,end= " ")
#     print("")   



# n = int(input("Numero: "))
# for i in range(1,n+1):
#     print(" "*(n-i)+ "#"*(i),end="")
#     print("")


def esPrimo(numero:int) -> bool:
    if numero <= 1:
        return False
    for i in range(2,numero):
        if numero % i == 0:
            return False
    return True


n = int(input("Ingresar un número: "))
while n < 10:
    print("Numero menor a 10 ")
    n = int(input("Ingresar un número: "))

def siguiente_primo(n):
    primo_dos = 0
    for i in range(n+1,2*n+2):
        if esPrimo(i) == True:
            primo_dos = i
            break
    return primo_dos

def anterior_primo(n):
    primo_anterior = 0
    for i in range(n-1,1,-1):
        if esPrimo(i) == True:
            primo_anterior = i
            break

    return primo_anterior

print(siguiente_primo(n))
print(anterior_primo(n))
