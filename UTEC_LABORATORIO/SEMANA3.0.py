def verificarNota(nota:float|int) -> str: 
    if nota >= 10.5:
        return "Aprobo"
    else:
        return "No aprobo"

# nota = float(input("Nota:"))

# print(verificarNota(nota))


def hallaEstacion(n:int) -> str:
    if n == 1:
        return "Verano"
    elif n == 2:
        return "Otonno"
    elif n == 3:
        return "Invierno"
    elif n == 4:
        return "Primavera"
    else:
        return "NO CORRESPONDE"

#n = int(input("Numero: "))
#print(hallaEstacion(n))

def hallaPrecio(edad:int) -> int:
    if edad >= 46:
        return 10
    elif edad >= 31:
        return 30
    elif edad >= 18:
        return 25
    elif edad >= 0:
        return 15
    else:
        return 0
# edad = int(input("Ingresar edad: "))
# print(hallaPrecio(edad))




def hallaMensaje(denominacion: int) -> str:
    if denominacion == 1:
        return "George Washington"
    elif denominacion == 2:
        return "Thomas Jefferson"
    elif denominacion == 5:
        return "Abraham Lincoln"
    elif denominacion == 10:
        return "Alexander Hamilton"
    elif denominacion == 20:
        return "Andrew Jackson"
    elif denominacion == 50:
        return "Ulysses S. Grant"
    elif denominacion == 100:
        return "Benjamin Franklin"
    elif denominacion == 500 or denominacion ==  1000 or denominacion == 5000 or denominacion == 10000:
        return "Denominación descontinuada"
    else:
        return "No existe esa denominación"

# denominacion = int(input("Ingressar denominación: "))
# print(hallaMensaje(denominacion))




def validar(longDeOnda: int) -> str:
    if longDeOnda > 780:
        return "No corresponde al espectro visible"
    elif longDeOnda >= 619:
        return "Rojo"
    elif longDeOnda >= 582:
        return "Naranja"
    elif longDeOnda >= 571:
        return "Amarillo"
    elif longDeOnda >= 498:
        return "Verde"
    elif longDeOnda >= 477:
        return "Cian"
    elif longDeOnda >= 428:
        return "Azul"
    elif longDeOnda >= 380:
        return "Violoeta" 
    else:
        return "No corresponde al espectro visible"

    


