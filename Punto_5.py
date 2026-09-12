"""
Realice un programa que almacene una cantidad de cadenas
dictaminadas por el usuario, en pantalla se debe mostrar la
cadena que más caracteres contenga y la cadena que menos
caracteres contenga.
Ejemplo:
Lista= [“oso”, “casa”, “murciélago”, “ventana”, “programación”]
Cadena mayor = programación.
Cadena menor = oso

"""

List_Size = int(input("Ingrese la cantidad de cadenas que desea en la lista: "))
User_List = []

for word in range(List_Size):
    User_List.append(input("Ingrese una cadena: "))
    
Greater_String = max(User_List, key=len)
Lesser_String = min(User_List, key=len)

print(f"\nCadena mayor = {Greater_String} ({len(Greater_String)} caracteres).")
print(f"\nCadena menor = {Lesser_String} ({len(Lesser_String)} caracteres).\n")