class Perro:
    def __init__(self, nombre , edad ):
        self.nombre = nombre
        self.edad = edad
    def ladrar(self):
        print(f"{self.nombre} dice ¡Guau!")

""" En cada clase se debe utilizar _init_ y el primer parametro será self , el segundo y el tercero son opcionales
    Si se crea una función el primer parametro será la función _init_
"""

mi_perro = Perro("Ostin",3)
# mi_perro.ladrar() -> Ostin dice ¡Guau!
# print(mi_perro.nombre) -> Ostin
# print(mi_perro.edad ) -> 3

otro_perro = Perro("luana",5)
# otro_perro.ladrar() -> Luana dice ¡Guau!


class Rectangulo:
    def __init__(self,base,altura):
        self.base = base
        self.alutra = altura

    def area(self):
        return self.base * self.alutra

r1 = Rectangulo(4,5)
# print(r1.area())

class CuentaBancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo
    def depositar(self,monto):
        self.saldo += monto
        print(f"Deposito exitoso {self.titular}. Nuevo saldo: {self.saldo}")

cuenta = CuentaBancaria("Victor",300)
cuenta.depositar(100)
# print(cuenta.saldo)



class Estudiante:
    
    def __init__(self,nombre):
        self.notas = []
        self.nombre = nombre
        
    def agregar_nota(self,nota):
        self.notas.append(nota)

    def promedio(self):
        try:
            return sum(self.notas)/len(self.notas)

        except ZeroDivisionError:
            return 0

reporte = Estudiante("Victor")
# print(reporte.promedio())
reporte.agregar_nota(15)
reporte.agregar_nota(17)
# print(reporte.promedio())

class Rectangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura =   altura

    def perimetro(self):
        return 2*(self.base + self.altura)

r1 = Rectangulo(6,3)
# print(r1.perimetro())
        

        
