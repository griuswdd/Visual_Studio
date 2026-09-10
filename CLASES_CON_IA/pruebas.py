def es_palindromo(texto):
    if texto == texto[::-1]:
        return True
    else:
        return False
    
texto = "Ana, Luis, Eva, Marco"
list_texto = texto.split(", ")
print(list_texto)
