def pregunta_1(distancia_km: int, ritmo_segundos_km: int, pausa_minutos: int) -> int:
    tiempo_corriendo = distancia_km * ritmo_segundos_km
    pausa_minutos = pausa_minutos * 60
    repuesta = tiempo_corriendo + pausa_minutos


    return repuesta


def pregunta_2(ritmo_segundos_km: int) -> str:
    if ritmo_segundos_km > 420:
        return "En entrenamiento"
    elif ritmo_segundos_km >= 301:
        return "Recreativo"
    elif ritmo_segundos_km >= 241:
        return "Competitivo"
    else:
        return "Elite"




def pregunta_3(edad: int, kilometros_semana: int) -> str:

    if edad < 18:
        return "No puede inscribirse: edad insuficiente"
    if edad >= 18 and kilometros_semana < 30:
        return "No puede inscribirse: preparación insuficiente"
    elif edad >= 18 and kilometros_semana >= 30:
        return "Inscripción aprobada"


def pregunta_4(distancia_km: int, intervalo_km: int) -> int:

    distancia_recorrida = intervalo_km
    puntos = 0
    while distancia_km > distancia_recorrida:
        distancia_recorrida += intervalo_km
        puntos += 1
        
    return puntos
