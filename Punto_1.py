"""
Realice un algoritmo para sumar los valores numéricos de la
siguiente lista sin ordenarla:
Lista= [2, 8,” hola”, “programación”, 10, “utp”, 85, 82, 100,”mundo”]

"""

Base_List = [2, 8, "hola", "programacion", 10, "utp", 85, 82, 100, "mundo"]
Result = 0
for element in Base_List:
    if isinstance(element, int):
        Result += element
print(f'El resultado de la suma es: {Result}')