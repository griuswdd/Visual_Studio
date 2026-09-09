
#E1
ventas = {"Laptop":3,"Mouse":15,"Teclado":8,"Monitor":2,"Teclado":8}

lc_01 = [nombre for nombre in ventas if ventas[nombre] >=5]
# print(lc_01)

#E2
def procesar_edad(edad):
    try:
        edad = int(edad)
        
    except ValueError:
        print("Edad invalida")
        return None

    try:
        if edad < 0:
            raise ValueError ("La edad no puede ser negativa")
    except ValueError as e:
        print(e)
        return None
# ed = input("ed: ")
# procesar_edad(ed)

#E3
class TERMOMETRO:
    def __init__(self,temperatura):
        self.temperatura = temperatura

    def es_valida(self):
    
        if self.temperatura <= 50 and self.temperatura >= -50:
            return True
        else:
            return False

    def convertir_a_fahrenheit(self):
        if self.es_valida() == True:
            far = (self.temperatura * 9/5) + 32
            return far
        else:
            return None

#E4
import numpy as np
ventas_semana = np.array([120,95,200,0,150,80,175])  
ventas_sin_cero = ventas_semana[ventas_semana != 0 ]
num_ventas_menor_prom = len(ventas_sin_cero[ventas_sin_cero < ventas_semana.mean()])


#E5
def filtrar_pares_positivos(elementos):
    return [x for x in elementos if x%2==0 and x>0]

#E6
class Pila:
    def __init__(self):
        self.elementos = []
    def aplilar(self,valor):
        self.elementos.append(valor)
    def despilar(self):
        try:
            return self.elementos.pop()
        except IndexError:
            print("La pila esta vacía")
            return None

    def esta_vacia(self):
        return len(self.elementos) == 0


#E7
empleados = [
    {"nombre": "Ana", "departamento": "Ventas", "salario": 3200},
    {"nombre": "Luis", "departamento": "IT", "salario": 4500},
    {"nombre": "Eva", "departamento": "Ventas", "salario": 2900},
    {"nombre": "Marco", "departamento": "IT", "salario": 5100},
]

#E8
def leer_archivo_seguro(nombre_archivo):
    try:
        with open(nombre_archivo) as e:
            contendio = e.read()
        return contendio
    except FileNotFoundError:
        print("El archivo no existe")
        return None
#9
notas = np.array([
    [15, 12, 18, 14],
    [10, 16, 13, 9],
    [17, 15, 19, 16]
])


#10
ventas = [
    {"producto": "Laptop", "cantidad": 3, "precio": 1200},
    {"producto": "Mouse", "cantidad": 10, "precio": 25},
    {"producto": "Teclado", "cantidad": 5, "precio": 45},
]


def resumen_ventas(ventas):
    if len(ventas) == 0:
        return ((None,0,0))
    precios = np.array([venta['precio'] for venta in ventas])
    cantidades = np.array([venta['cantidad'] for venta in ventas])
    producto_mas_vendido = [venta['producto'] for venta in ventas if venta['cantidad'] == np.max(cantidades)][0]
    total_facturado = int(sum(cantidades * precios))
    promedio_precio = float(np.mean(precios))
    return producto_mas_vendido,total_facturado,promedio_precio


print(resumen_ventas(ventas))

    