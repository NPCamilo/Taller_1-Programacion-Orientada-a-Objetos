"""
Elabore un programa para ingresar la siguiente lista.
Lista= [“casa”, “programación”, “utp”, “universidad”, “utp, “casa”,
“casa”,” thj”, “vbh”, “456”, “987”]
a. Borre los elementos repetidos que tengamos en la lista
b. Borre las cadenas que NO contengan vocales.
c. Ordene la lista en orden alfabético respecto al primer
elemento de la cadena.

"""

Base_List = ["casa", "programación", "utp", "universidad", "utp", "casa", "casa", "thj", "vbh", "456", "987"]

# a. Borrar elementos repetidos
Base_List = list(set(Base_List))

# b. Borrar cadenas que no contengan vocales
Vocals = ["a", "e", "i", "o", "u"]
Base_List = [cadena for cadena in Base_List if any(vocal in cadena for vocal in Vocals)]

# c. Ordenar la lista en orden alfabético desde el primer elemento de la cadena
Base_List.sort()

print(f'La lista final es: {Base_List}')