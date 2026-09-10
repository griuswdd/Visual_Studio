from math import *

def pregunta_1(I: float) -> float:
    resultado = 10*log10(I/(10**-12))
    return round(resultado,3)


def pregunta_2(re: float) -> str:



    if re > 4000:
        return "Turbulento"
    elif re >= 2000:
        return "Transicional"
    else:
        return "Laminar"



def pregunta_3(presion_entrada: float, presion_vapor: float) -> str:

    margen = presion_entrada - presion_vapor
    if margen >= 5:
        return "Operacion estable"
    elif margen >= 2:
        return "Riesgo de cavitacion"
    else:
        return "Cavitacion severa"
    


def pregunta_4(N: float, lam: float, umbral: float) -> int:

    parametro = 0
    while N > umbral:
        parametro += 1
        N = N * (1-lam)

    return parametro

