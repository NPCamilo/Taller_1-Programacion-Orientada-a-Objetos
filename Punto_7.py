"""
Realizar un programa que pida al usuario un carácter, luego se
debe mostrar las cadenas que contengan dicho carácter y debe
mostrar si dichas cadenas son pares o impares.
Lista= [“oso”, “casa”, “murciélago”, “ventana”, “programación”,”
objetos”, “listas”, “métodos”, “utp”]

"""
Base_List = ["oso", "casa", "murciélago", "ventana", "programación", "objetos", "listas", "métodos", "utp"]
User_Input = input("Ingrese un carácter: ")
Switch = False

if not(isinstance(User_Input, str) and len(User_Input) == 1):
    print("\nDebe ingresar un solo carácter.\n")
else:
    for word in Base_List:
        if User_Input in word:
            Switch = True
            if len(word) % 2 == 0:
                print(f"\nLa cadena {word} contiene el carácter {User_Input} y es par.")
            else:
                print(f"\nLa cadena {word} contiene el carácter {User_Input} y es impar.")

if Switch == False:
    print(f"\nNo hay cadenas que contengan el carácter {User_Input}.\n")
1