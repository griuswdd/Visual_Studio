# # try:
#     # numero = int(input("Ingresa un número: "))
# # except ValueError:
#     # print("Eso no es un número válido")
# # except KeyboardInterrupt:
#     # print("Cancelado por el usuario")


# # try:
# #     numero = int(input("Ingresar número: "))

# # except ValueError:
# #     print("Número no encontrado")

# # else:
# #     print("Número encontrado")

# # finally:
# #     print("Siempre se ejecutara aunque haya except o else")


# # def convertir_a_numero(texto):
# #     try:
# #         return int(texto)
# #     except ValueError:
# #         print(f"{texto} no es un número valido")
# #         return None

# # print(convertir_a_numero("6767676")) # 6767676

# # print(convertir_a_numero("hola")) #hola no es número valido --> None

# # datos = {"nombre":"Vicotr","Edad":18}
# # try:
# #     print(datos["ciudad"])
# # except KeyError:
# #     print(" Esa llave no existe para ese diccionario ")

# def dividir_seguro(a,b):
#     try:
#         resultado = a/b
#         return resultado
#     except ZeroDivisionError:
#         print("Error: no se puede dividir por cero")
#         return None

# Edades = [23,45,12,67,34]

# try:
#     Edades[10]
# except IndexError:
#     print(" Ese índice no existe 😅 ")

# finally:
#     print(" Intento de acceso finalizado ")