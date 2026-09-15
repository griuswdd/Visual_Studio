def pregunta_1(nivel_inicial_cm: int, aumento_diario_cm: int, dias: int, zonas: int) -> int:


    contador = 0
    for i in range(1,dias+1):
        nivel_inicial_cm += aumento_diario_cm
        for j in range(1,zonas+1):
            limite = 200 + (j-1)*20
            
            if nivel_inicial_cm >= limite:
                contador += 1
    return contador


def pregunta_2(nivel_inicial_cm: int, aumento_diario_cm: int, dias: int) -> int:
    contador = 0
    for i in range(1,dias+1):
        nivel_inicial_cm += aumento_diario_cm
        if 250 <= nivel_inicial_cm:
            contador += 1
    
    return contador


def pregunta_3(personas: int, capacidad_bote: int, nivel_rio_cm: int) -> int:
    if nivel_rio_cm >= 300:
        capacidad_bote -= 1
    contador = 0

    if personas == 0:
        return 0
    while personas > 0:
        contador += 1
        personas -= capacidad_bote
    return contador



def pregunta_4(dias: int, nivel_inicial_cm: int, lluvia_diaria_mm: int) -> int:
    contador = 0
    while dias > 0:
        dias -= 1
        
        if 50 <= lluvia_diaria_mm:
            nivel_inicial_cm += 20
        elif 25 <= lluvia_diaria_mm:
            nivel_inicial_cm += 10
        else:
            nivel_inicial_cm += 2
        if nivel_inicial_cm >= 250:
            contador += 1

    return contador

