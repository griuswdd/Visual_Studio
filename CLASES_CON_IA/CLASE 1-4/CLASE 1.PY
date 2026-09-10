#list comprehension
numeros_producto_2 = [a*2 for a in range(10)] # número del 0 al 9 multiplicados x2
# print(numeros_producto_2)

#dict comprehension
# diccionario con el número de letras
cantidad_de_letras = {palabra : len(palabra) for palabra in ["python", "es", "genial", "para", "datos"] if len(palabra) > 2} #imprimir palabra:len(palabras)) en un diccionario solo si tiene más de 2 letras
# print(cantidad_de_letras)

#generador comprehension
cuadrados_gen = (n**2 for n in range(3)) #generar el número de cuadrado dependiendo de la vuelta al cuadrado, SOLO se imprimira el valor de la vuelta al cuadrado
# print(next(cuadrados_gen)) #0
# print(next(cuadrados_gen)) #1
# print(next(cuadrados_gen)) #2

# for a in cuadrados_gen:
    # print(a) # muestra todos los valores de arriba para abajo tabulado

#EJERCICIOS
#E1
lista = [-5,0,10,22,-3,30,15]

Resolución_E1 = [c*(9/5) + 32 for c in lista if c > 0]
#print(Resolución_E1)

#E2
gen = (x for x in range(3))

#print(next(gen))
#print(next(gen))
#print(next(gen))
#print(next(gen))

