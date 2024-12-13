import matplotlib.pyplot as plt

# Datos de la gráfica
plt.plot([0, 1, 2, 3, 4, 5], [5, 10, 6, -10, 15, 1], 'r--o', label="Partícula 1")

# Título de la gráfica
plt.title("Una primera aproximación")

# Etiquetas de los ejes
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

# Etiqueta para pintar el punto P1
plt.scatter(2, 6, color='blue', label="P1(2,6)")
plt.text(2, 6, "P1(2,6)", fontsize=10, ha='left', va='bottom', color='blue')

# Leyenda, rejilla y mostrar gráfica
plt.legend()
plt.grid(ls="--", color="#dadada")
plt.show()
