def pregunta_1(horas_redes: float, horas_juegos: float, brillo: float) -> float:
    bateria_final = 100-((horas_redes*12)+(horas_juegos*20))*(brillo/10)**2
    return round(bateria_final,2) 


def pregunta_2(nivel: int, pm: int, escudo: bool) -> str:

    print(nivel,pm,escudo)
    print(type(escudo))

    if nivel >= 50 and pm >=80 and escudo == True:
        return "Ataque Lumina"
    elif nivel >= 30 and pm >= pm >= 50:
        return "Ataque Especial"
    elif pm >= 20:
        return "Ataque Basico"
    else:
        return "Descansar"


def pregunta_3(consultas_previas: int, precio: float) -> float:
    if consultas_previas >= 8 and precio > 100:
        return (precio*70)/100
    elif consultas_previas >= 8 and precio <= 100:
        return (precio*80)/100
    elif 4 <= consultas_previas and consultas_previas < 8 and precio > 80:
        return (precio*85)/100
    elif 4<= consultas_previas and consultas_previas < 8 and precio <= 80:
        return (precio*90)/100
    elif consultas_previas <4:
        return precio


def pregunta_4(combustible: float, consumo: float) -> int:
    horas = 0
    combustible_usado = 0
    while combustible_usado < combustible:
        combustible_usado += consumo
        horas += 1
        
    return horas

