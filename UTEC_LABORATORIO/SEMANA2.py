from math import *

#Ingresar cantidad de peso

#Ingresar cantidad de altura

#Calcular peso / (altura * altura)

#imprimir resultado

#programa 1----------------------------------

# peso = float(input("Ingresar cuantos gramos pesas; ")) / 1000
# altura = float(input("Ingresar altura en centímetros ")) / 100

# bmi = peso / (altura * altura)


# print("El indece de masa corporal (BMI) es: ", round(bmi,3))

#programa 2---------------------------------

# x1 = float(input("Ingrese la coordena x del primer punto")
# y1 = float(input("Ingrese la coordena y del primer punto"))
# x2 = float(input("Ingrese la coordena x del segundo punto"))
# y2 = float(input("Ingrese la coordena y del segundo punto"))

# respuesta = (sqrt((x2-x1)**2 + (y1-y2)**2))

# print(respuesta)


# PROGRAMA 3

# numero = input("Ingresar un número de 3 dígitos: ")
# primera_cifra = int(numero[0])
# segunda_cifra = int(numero[1]) * 10
# tercera_cifra = int(numero[2]) * 100
# print(primera_cifra+segunda_cifra+tercera_cifra) 

#otra forma
# a = input("Ingresar el valor de a: ")
# primera_cifra(int(a[::-1]))

# PROBLEMA 4

# cant_coleres_empaq = int(input("Colores: "))

# print(f"{cant_coleres_empaq//24} cajas de 24 colores")
# print(F"{(cant_coleres_empaq%24)//12} cajas de 12 colores")
# print(f"{((cant_coleres_empaq%24)%12)//6} cajas de 6 colores")
# print(f"{(((cant_coleres_empaq%24)%12)%6)} colores sobrarían")


# PROBLEMA 5
# segundos = int(input("Segundos: "))
# días = segundos // (3600 * 24)
# horas = (segundos % (3600 * 24)) // 3600
# minutos = ((segundos % (3600 * 24)) % 3600) // 60
# segundos = ((segundos % (3600 * 24)) % 3600) % 60 
# print(f"Equivale a: {días}:{horas}:{minutos}:{segundos}")

#PROBLEMA 6
# n = float(input("Ingresar la longitud de los lados: "))
# s = int(input("Ingresar número de lados: "))
# area = (n*s) / (4 * tan(pi/n))
# print(round(area,1))


#RESOLUCIÓN 1 ( REDONDEADA 3 

# kilos = float(input("Ingrese el peso en grs: "))/1000
# metros = float(input("Ingrese la altura en cms: "))/100

# respuesta = kilos/ (metros*metros)

# respuesta_4decimales = round(respuesta,4) #redondear a 4 para que el tercer decimal no cambie su valor orginal
# valores_enteros = int(respuesta)

# primera_resolucion = str(round(respuesta_4decimales - valores_enteros,4)) #hallamos solo la parte decimal ejemplo 5.4894 --> 0.4894
# print(primera_resolucion)
# r_3decimales = primera_resolucion[0:5] #si la parte decimal es 0.54678, solo toma los primeros 5 valores es decir "0",".","5","4","6"

# suma_final = valores_enteros + float(r_3decimales) #sumamos la parte entera + los primeros 3 decimales

# print(suma_final)

#-------------------------------------------PARTE 2----------------------------------------------------------------------------

# E1
# edad = int(input("Edad: "))

# valor = true = edad >=18
# segundo_valor = edad<18

# print(segundo_valor*"es menor de edad" + valor*"es mayor de edad")


# E2
# Kw = float(input("Kw: "))

# mayor_igual_a_100 = Kw >= 100
# menor_a_100 = Kw < 100


# print(f"el monto a pagar es: {menor_a_100*(str((Kw*0.4522))) + mayor_igual_a_100*(str(((100*0.4522)+(Kw-100)*0.7)))}" )


# E3

# numero = int(input("Numero: "))
# print(f"Es {((numero%2==0)*"par" + (numero%2!=0)*"impar")} ")

# E4


# l1 = float(input("Ingresar longitud del primer lado del triangulo: "))

# l2 = float(input("Ingresar longitud del segundo lado del triangulo: "))

# l3 = float(input("Ingresar longitud del tercer lado del triangulo: "))

# condicion1 = l1 + l2 > l3
# condicion2 = l2 + l3 > l1
# condicion3 = l1 + l3 > l2

# print((condicion1 and condicion2 and condicion3)*"ES TRIANGULO VALIDO" + (not(condicion1 and condicion2 and condicion3))*"NO ES TRIANGULO VALIDO")

# E5

# c = float(input("Consumo: "))
# print(f"El monto a pagar es {c * 123/100}")

# E6

# b_1l = int(input("Numero de botellas de hasta un litro: "))
# b_mas1l = int(input("Numero de botellas de mas de un litro: "))

# print(f"El monto a favor es de {b_1l*1.25 + b_mas1l * 3.75}")

# E7

# numero = int(input("Numero: "))
# numero_texto = str(numero)

# print(f"{numero_texto[0]}+{numero_texto[1]}+{numero_texto[2]}+{numero_texto[3]} = {numero_texto[0]+numero_texto[1]+numero_texto[2]+numero_texto[3]}")

#E8

# Numero1 = int(input("Numero 1: "))
# Numero2 = int(input("Numero 2: "))
# Numero3 = int(input("Numero 3: "))

# mayor = max(Numero1,Numero2,Numero3)
# menor = min(Numero3,Numero2,Numero1)
# print(f"{menor},{Numero1+Numero2+Numero3-menor-mayor},{mayor}")