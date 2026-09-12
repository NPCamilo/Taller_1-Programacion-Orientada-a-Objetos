"""
Realizar un programa que haga conteo de todos los caracteres
que no sean vocales en una lista de 10 cadenas.

"""
List_Size = 10
User_List = []
Vocals = ["a", "e", "i", "o", "u"]
Counter = 0

for word in range(List_Size):
    User_List.append(input("Ingrese una cadena: "))
    if len(User_List[word]) == 0:
        print("\nDebe ingresar al menos un carácter.\n")
        User_List.pop()
        word -= 1
    else:
        for character in User_List[word]:
            if character.lower() not in Vocals:
                Counter += 1
                
print(f"\nLas cadenas ingresadas por el usuario tienen {Counter} caracteres que no son vocales.\n")