from math import *



def pregunta_1(radio: float, angulo: float) -> float:

    formula = round(radio*angulo*(pi/180),2)
    return formula





def pregunta_2(vx: float, vy: float, vz: float) -> float:
    """
    Parametros:
        vx (float):  Es la coordenada en x
        vy (float):  Es la coordenada en y
        vz (float):  Es la coordenada en z
    Retorna:    
        float : es el modulo
    """
    formula = sqrt(vx**2 + vy**2 + vz**2)
    return round(formula,2)


def pregunta_3(edad: int) -> str:
    """
    Parametros:
        edad (int): Edad de la persona.
    Retorna:
        str: Clasificacion de la edad.
    """
    if edad < 13:
        return "Menor"
    elif edad < 18:
        return "Adolescente"
    elif edad < 65:
        return "Adulto"
    else:
        return "Adulto Mayor"




def pregunta_4(peso: int, altura: float) -> str:
    """
    Parametros:
      peso (float): Peso en kilogramos (kg).
      altura (float): Altura en metros (m).
    Retorna:
        str : La categoria del IMC segun la OMS.
    """
    IMC = peso/(altura*altura)
    if IMC < 18.5:
        return "Bajo peso"
    elif IMC < 25:
        return "Normal"
    elif IMC < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"


