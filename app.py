import pandas as pd

def aprobados(notes):
    note = pd.Series(notes)
    return note[note >= 5].sort_values(ascending=False)

notas = {
    'Juan': 9,
    'María': 6.5,
    'Pedro': 4,
    'Carmen': 8.5,
    'Luis': 5
}

print(f"""
1.- ¿Qué esta se está haciendo en estas líneas de código?

{aprobados(notas)}

R= Están creando una función llamada aprobados que toma un diccionario de notas como entrada y devuelve una serie de pandas 
   con las notas de los estudiantes que han aprobado (es decir, tienen una nota igual o superior a 5).
   La serie se ordena en orden descendente.

3.- ¿Cuál es la diferencia entre una función y un método en Python?
R= Una función es un bloque de código que se puede llamar varias veces desde diferentes partes de un programa. Se define utilizando la palabra clave def seguida del nombre de la función y sus parámetros entre paréntesis.
   Un método es una función que se define dentro de una clase y está asociada con un objeto de esa clase. Se utilizan para realizar acciones específicas en un objeto o para acceder a sus atributos.
""")
