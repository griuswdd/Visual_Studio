def sumar_digitos(numero):
    numeros = list(str(numero))
    suma_pares = 0
    suma_impares = 0
    for i in numeros:
        if int(i) % 2 == 0:
            suma_pares += int(i)
        else:
            suma_impares += int(i)

    return (suma_pares,suma_impares)

def escalera_con_asterisco(numero):
    for i in range(1,numero+1):
        print(((numero)**2 - (i)*(numero))*" " + numero*"*")
    


def pregunta1_(tamanio):
    for  i in range(tamanio):
        if i % 2 == 0:
            for j in range(tamanio):
                if j % 2== 0:
                    print("#",end="")
                else:
                    print("0",end="")
        else:
            for j in range(tamanio):
                if j%2== 0:
                    print("0",end="")
                else:
                    print("#",end="")
        print("")

def pregunta_4(tam):
    if tam == 1:
        print("*")
    elif tam == 2:
        print(tam*"*")
        print(tam*"*")
    else:
        for i in range(1,tam+1):    
            if i == 1 or i == tam:
                print(tam*"*")
            else:
                
                print("*",end="")
                print((tam-2)*" ",end="")
                print("*",end="")
                print("")

def es_primo(num:int): 
    num = int(num)
    for i in range(2,num//2):
        if num%i == 0:
            return False
    return True

def numero_de_divisores(num:int):
    num = int(num)
    contandor = 0
    for i in range(2,num//2 + 1):
        if num % i == 0:
            contandor += 1
    return contandor

def codigo_barras(num):
    num = int(num)
    codigo_bar = ""
    texto_numero = str(num)
    for d in texto_numero:
        d = int(d)
        if numero_de_divisores(d) == 0:
            codigo_bar += " "
        else:
            codigo_bar += numero_de_divisores(d)*"|"
    return codigo_bar

def pregunta_67_1(monedas,precio):
    contador = 0
    while monedas >= precio:
        contador += 1
        monedas -= precio
    return contador


def pregunta_67_2(N):
    contador = 0
    for i in range(10,100):
        suma_de_cifras = int(str(i)[0]) + int(str(i)[1]) 
        if suma_de_cifras == N:
            contador += 1

    return contador

def pregunta_76_3(planes,N):
    contador = 0
    for i in range(1,N+1):
        if i % 3 == 0:
            contador += 1

    return contador * planes
    
print(pregunta_76_3(4,2))









        

