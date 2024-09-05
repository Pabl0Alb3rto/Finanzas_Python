import matplotlib.pyplot as plt

""" El número de años debe ser un array desde 1 a n porque me pasan el entero por pantalla
 El valor de capital en un momento determinado debe calcularse igual, con la misma fórmula,
 por lo que debería poder calcularlo siendo n un array desde 1 a n años que me pasen"""


# Datos
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Crear gráfico de líneas
plt.plot(x, y, marker='o')

# Añadir título y etiquetas
plt.title('Gráfico de Línea')
plt.xlabel('X')
plt.ylabel('Y')

# Mostrar gráfico
plt.show()
