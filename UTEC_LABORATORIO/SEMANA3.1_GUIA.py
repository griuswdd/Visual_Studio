from math import *

def pregunta_1(arista:  float) -> float: 
    """
    Halla el area de un cuadrilatero ciclico 
    Parametros:
    	arista (float) :  Es la arista
    Retorna:
    	float : el volumen, valor expresado con 3 cifras decimales
    """	
    volumen = round((1/4)*(15+(7*(sqrt(5))))*(arista**3),3)
    return volumen

    

def pregunta_2(lado1: float, lado2: float, lado3: float, lado4:float) ->float: 
    """
    Halla el area de un cuadrilatero ciclico 
    Parametros:
    	lado1 (float) :  El primer lado
            lado2 (float) :  El segundo lado
            lado3 (float) :  El tercer lado
            lado4 (float) :  El cuarto lado
    Retorna:
    	float : el area, valor expresado con 3 cifras decimales
    """
    semiperimetro = (lado1+lado2+lado3+lado4)/2
    area = sqrt((semiperimetro-lado1)*(semiperimetro-lado2)*(semiperimetro-lado3)*(semiperimetro-lado4))
    return round(area,3)

    


def pregunta_3(numero : int)->str:
    """
    Determina la cantidad de digitos iguales que tiene un numero
    Parametros:
        numero (int) : un entero de 3 digitos
    Retorna:
        Str : Es la cadena que contiene el mensaje
    """

    centenas = numero // 100
    decenas = (numero%100) // 10
    unidades = numero % 10

    if centenas == decenas and decenas == unidades:
        return "Tiene tres digitos iguales"
    if centenas == decenas or decenas == unidades or centenas == unidades:
        return  "Tiene solo dos digitos iguales"
    else:
        return "Tiene tres digitos diferentes"



    

def pregunta_4( rango :  int) -> str: 
    """
    Halla la clasificacion de IQ 
    Parametros:
    	rango (int) :  Es el rango de IQ
    Retorna:
    	Str :  Es la clasificacion que corresponde segun el rango IQ 
    """	

    if rango <= 69:
        return "Deficiente"
    elif rango <= 79:
        return "Inferior"
    elif rango <= 89:
        return "Abajo del Promedio"
    elif rango <=109:
        return "Promedio"
    elif rango <= 119:
        return "Arriba del Promedio"
    elif rango <= 129:
        return "Superior"
    else:
        return "Muy Superior"

