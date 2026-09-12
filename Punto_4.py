"""
Escriba un programa que pida al usuario la cantidad que desea
de la lista, luego el usuario debe ingresar valores numéricos
enteros hasta llenar la lista, luego de ingresarlos se debe
imprimir en pantalla cada número ingresado por el usuario y al
lado debe aparecer ese mismo número al cuadrado y al lado ese
mismo número al cubo, ejemplo:
L = [2,3]
Salida:
2 - 4 - 8
3 - 9 - 27

"""
List_Size = int(input("Ingrese la cantidad de números que desea en la lista: "))
User_List = []

for space in range(List_Size):
    User_List.append(int(input("Ingrese un número entero: ")))

Square_List = []
Cube_List = []
for number in User_List:
    Square_List.append(number ** 2)
    Cube_List.append(number ** 3)
    
for number in range(List_Size):
    print(f"{User_List[number]} __ {Square_List[number]} __ {Cube_List[number]}")