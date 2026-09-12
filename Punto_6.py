"""
Realice un programa en el que el usuario ingrese un valor
entero, luego debe mostrar en pantalla las cadenas cuya longitud
sea igual al número ingresado, puede usar la lista del ejercicio 5
o 7.

"""

Base_List = ["oso", "casa", "murciélago", "ventana", "programación", "objetos", "listas", "métodos", "utp"]
User_Input = int(input("Ingrese un valor entero: "))

Switch = False
for word in Base_List:
    if len(word) == User_Input:
        print(f"\nLa cadena {word} tiene una longitud igual a {User_Input} caracteres.\n")
        Switch = True

if Switch == False:
    print(f"\nNo hay cadenas con una longitud de {User_Input} caracteres.\n")