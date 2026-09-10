import random
def ahocados():
    
    palabras = ["mundou","pythony","ala"]
    palabra_random = random.choice(palabras)
    numero_de_letras = len(palabra_random )
    lista_de_letras = list(palabra_random)

    def iniciar():
        lista_palabrita = []
        vidas = 6
        for i in range(numero_de_letras):
            lista_palabrita.append("-")
                    
        while vidas > 0:
            
            print(f"Tu palabra tiene {numero_de_letras} letras")
            print(lista_palabrita)
           
            letra_del_jugador = input("Tu letra es: ")
            if letra_del_jugador in lista_de_letras:
                if lista_de_letras.count(letra_del_jugador) == 1:
                    indice = lista_de_letras.index(letra_del_jugador)
                    lista_palabrita[indice] = letra_del_jugador
                else:
                    for i in range(lista_de_letras.count(letra_del_jugador)):
                        indice = lista_de_letras.index(letra_del_jugador)
                        lista_palabrita[indice] = letra_del_jugador
                        lista_de_letras[indice] = "$$"
                        
            else:
                print(F"Te equivocaste, te quedan {vidas}")
                vidas -= 1

            
        else:
            print("Te quedaste sin vidas")
            

    iniciar()


