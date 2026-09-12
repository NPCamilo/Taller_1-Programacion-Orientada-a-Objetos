"""
Realizar un programa que inicialice una lista con 15 valores
aleatorios y posteriormente muestre en pantalla cada elemento
de la lista junto con su cuadrado y su cubo.

"""
import random
from tabulate import tabulate

List_Size = 15
User_List = []
Superior_Limit = int(input("Ingrese el límite superior de los números aleatorios: "))

for space in range(List_Size):
    User_List.append(random.randint(1, Superior_Limit))

Square_List = []
Cube_List = []
for number in User_List:
    Square_List.append(number ** 2)
    Cube_List.append(number ** 3)
 
# Definir los datos de la tabla
Main_List = []

for number in range(List_Size):
    Pivot_List = []
    Pivot_List.append(User_List[number])
    Pivot_List.append(Square_List[number])
    Pivot_List.append(Cube_List[number])
    Main_List.append(Pivot_List)

# Definir los encabezados
columnas = ["Número", "Cuadrado", "Cubo"]

# Generar e imprimir la tabla
print(tabulate(Main_List, headers=columnas, tablefmt="grid"))