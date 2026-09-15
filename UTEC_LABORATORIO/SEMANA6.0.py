def Leer_Dato(n):
    while n > 10 or n < 0:
        n = int(input(""))

    for i in range(1,n+1):
        if n % 2== 0:
            for j in range(1,11):
                if i % 2 == 0:
                    print(f"{i} * {j} = {i*j}")

        else:
            for j in range(1,11):
                if i % 2 != 0:
                    print(f"{i} * {j} = {i*j}")


        
from random import *
def planeta_Gorinki():
    n_g = int(input("Numero de gorinkis: "))
    while n_g < 3:
        n_g = int(input("Numero de gorinkis: "))
    
    for j in range(n_g):
        suma = 0
        for i in range(5):
            a = int(input(f"Presion sistólica {i+1}: "))
            suma += a

        promedio = suma/5
        print("Ud." + (promedio <= 130)*"No" + " es hipertenso el promedio de su presión sistólica es: ",promedio)


