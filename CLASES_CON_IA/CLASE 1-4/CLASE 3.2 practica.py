"""EJERCICIOS"""

#1
nombres = ["Ana","Victoria","Luis","Alejandro","Eva"]
diccionario1 = {nombre: True for nombre in nombres if len(nombre)>5 }


#2
generator = (n+1 for n in range(30) if (n+1)%3 == 0 and (n+1)%5 == 0)

#3
def obtener_elemento(lista:list,indice:int) ->str:
    try:
        return lista[indice]
    except:
        "Índice fuera de rango"
        return None

#E4
numeros = [1,2,3,4,5,6,7,8,9]
def dividir_lista(lista,divisor):
    try:
        
        return [numero/divisor for numero in lista]
    except:
        return []



#E5

class libro:
    def __init__(self,titulo,autor,paginas_leidas):
        libro.titulo = titulo
        libro.autor = autor
        libro.paginas_leidas = paginas_leidas
    def leer(self,pag):
        libro.paginas_leidas += pag

    def progreso_total(self,total_de_paginas):
        print(self.paginas_leidas)
        print(total_de_paginas)
        print(self.paginas_leidas/total_de_paginas)
        
        return (self.paginas_leidas/total_de_paginas)*100


class carrito:
    def __init__(self):
        self.lista = []
    def agregar_producto(self,nombre,precio):
        self.lista.append((nombre,precio))
    def total(self):
        return sum(n for _, n in self.lista)


carrito1= carrito()
carrito1.agregar_producto("AYA",50)
carrito1.agregar_producto("eye",100)
print(carrito1.total())



