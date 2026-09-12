# Taller 1 · Programación Orientada a Objetos (Python)

> **Asignatura:** Programación IV · Universidad Tecnológica de Pereira
> **Tema:** Listas y su manipulación en Python (acercamiento a la POO)

Ejercicios de práctica con **listas en Python**: recorridos, comprensión de listas, funciones internas, conteo de caracteres, manejo de datos mixtos y promedios. Este taller es el primer escalón antes de profundizar en clases y objetos.

---

## 📋 Requisitos

- Python 3.10 o superior.
- Solo el punto 9 necesita una librería externa. Instálala así:

```bash
pip install tabulate
```

---

## 🗂️ Estructura del proyecto

| Archivo        | Descripción |
|----------------|-------------|
| `Punto_1.py`   | Suma los valores numéricos de una lista que contiene números y cadenas. |
| `Punto_2.py`   | Une todas las palabras de una lista en una sola cadena separada por espacios. |
| `Punto_3.py`   | Calcula el promedio de 3 asignaturas y el promedio general del semestre. |
| `Punto_4.py`   | Pide números al usuario y muestra cada uno con su cuadrado y su cubo. |
| `Punto_5.py`   | Encuentra la cadena con más y con menos caracteres de una lista. |
| `Punto_6.py`   | Muestra las cadenas cuya longitud coincide con un número dado. |
| `Punto_7.py`   | Muestra las cadenas que contienen un carácter y si son pares o impares. |
| `Punto_8.py`   | Cuenta los caracteres que **no** son vocales en 10 cadenas. |
| `Punto_9.py`   | Genera 15 números aleatorios y los muestra en una tabla con su cuadrado y cubo. |
| `Punto_10.py`  | Elimina repetidos, borra cadenas sin vocales y ordena alfabéticamente. |

---

## 🚀 Cómo ejecutar

Cada punto es independiente. Ejecuta uno a la vez:

```bash
# Desde dentro de la carpeta del taller
python Punto_1.py
python Punto_3.py      # Este punto pide datos por teclado
python Punto_9.py      # Necesita la librería 'tabulate'
```

> **Nota:** los puntos que piden datos al usuario (`Punto_3`, `Punto_4`, `Punto_5`, `Punto_6`, `Punto_7`, `Punto_8`) son interactivos: debes escribir la información cuando Python la solicite.

---

## 📝 Explicación de cada punto

### Punto 1 — Suma de valores numéricos
Lista mixta con enteros y cadenas. Se recorre con un `for` y solo se suman los elementos que son números usando `isinstance(element, int)`.

**Conceptos:** bucle `for`, `isinstance()`, acumulador.

```python
Base_List = [2, 8, "hola", "programacion", 10, "utp", 85, 82, 100, "mundo"]
Result = 0
for element in Base_List:
    if isinstance(element, int):
        Result += element
```

### Punto 2 — Unir palabras en una cadena
Usa el método `join()` de las cadenas para concatenar todos los elementos separados por un espacio.

**Conceptos:** método `join()`, f-strings.

```python
Result = " ".join(["Hola", "mundo", "esto", "es", "Python"])
```

### Punto 3 — Promedio de asignaturas
Pide 3 asignaturas y 4 notas por cada una. Si el promedio de una asignatura es menor a 3 imprime `asignatura perdida`; luego calcula el promedio general con los mismos criterios (`semestre perdido`, `buen trabajo`, `felicidades serás becado`).

**Conceptos:** bucles anidados, `sum()`, `len()`, condicionales, listas acumuladoras.

### Punto 4 — Cuadrado y cubo
El usuario indica cuántos números quiere, los ingresa, y el programa construye dos listas nuevas: una con los cuadrados y otra con los cubos. Finalmente imprime las tres juntas.

**Conceptos:** `append()`, operador de potencia `**`, recorrido con índice (`range`).

### Punto 5 — Cadena mayor y menor
De una lista de cadenas ingresadas por el usuario, busca la más larga y la más corta usando la clave `key=len` de `max()` y `min()`.

**Conceptos:** `max()` / `min()` con `key`, `len()`.

### Punto 6 — Cadenas según longitud
Pide un entero y muestra todas las cadenas de la lista base cuya longitud coincida con ese número. Si ninguna coincide, avisa al usuario.

**Conceptos:** `len()`, bucle `for`, variable "bandera" (`Switch`).

### Punto 7 — Contiene un carácter
Pide un solo carácter y recorre la lista mostrando qué cadenas lo contienen y si su longitud es par o impar.

**Conceptos:** operador `in`, módulo `%`, validación `isinstance()` + `len()`.

### Punto 8 — Conteo de no vocales
Ingresa 10 cadenas y cuenta cuántos caracteres **no** son vocales (a, e, i, o, u), usando `not in` y `.lower()`.

**Conceptos:** bucles anidados, comparación contra vocales, contador acumulador.

### Punto 9 — Tabla de aleatorios (con `tabulate`)
Genera 15 números aleatorios, calcula su cuadrado y cubo, y los muestra en una tabla formateada con la librería `tabulate`.

**Conceptos:** `random.randint()`, matrices (listas de listas), `tabulate()`. **Requiere `pip install tabulate`.**

### Punto 10 — Depuración de la lista
Con **comprensión de listas** y `set()` elimina los elementos repetidos, conserva solo las cadenas que contienen vocales y por último ordena alfabéticamente con `sort()`.

**Conceptos:** `set()`, comprensión de listas, `any()`, `sort()`.

```python
Base_List = list(set(Base_List))
Base_List = [cadena for cadena in Base_List if any(vocal in cadena for vocal in Vocals)]
Base_List.sort()
```

---

## 🧠 Conceptos repasados

- Listas: creación, `append()`, `pop()`, `index`, recorrido y modificación.
- Bucle `for` y bucles anidados.
- Comprensión de listas.
- Funciones y métodos: `len()`, `sum()`, `max()`, `min()`, `join()`, `sort()`, `count()`.
- Selección condicional con `if` / `elif` / `else`.
- Validación de tipos con `isinstance()`.
- Librerías: `random` y `tabulate`.

---

## 📚 Fuentes oficiales

- [Documentación de estructuras de datos de Python](https://docs.python.org/3/tutorial/datastructures.html)
- [El tipo `list`](https://docs.python.org/3/library/stdtypes.html#lists)
- [Librería `tabulate`](https://pypi.org/project/tabulate/)