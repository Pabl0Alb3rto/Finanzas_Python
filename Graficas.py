import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg


                    #CALCULADORA DE INTERÉS COMPUESTO

# Pido los datos necesarios

Co = int(input("Capital inicial de su inversión:")) 
d =  int(input("Aportación mensual que desea realizar:"))
i =  float(input("Tipo de interés esperado anual (%):"))
m =  int(input("Número de subperíodos de capitalización:"))
n =  int(input("Duración en años de su inversión:"))
 
# Aquí podría sacar una tabla como los datos que han sido introducidos, con el print así se imprimen todos de golpe y se piden de golp

print(Co)    
print(d)
print("{} %".format(i))
print(m)
print (n)

# Pongo i como decimal porque me lo dan por pantalla como porcentaje (%)
i = i/100
# Calcular el valor futuro con interés compuesto y aportaciones periódicas
Cn = Co * (1 + i/m)**(m*n) + d * (((1 + i/m)**(m*n) - 1) / (i/m))
print(f"El valor futuro de la inversión con aportaciones periódicas es: ${Cn:.2f}")

""" Voy a intentar sacar estos datos que he pedido y el resultado en formato de tabla:"""


import matplotlib.pyplot as plt
import pandas as pd

# Crear un DataFrame
data = {
    'Variables ': ['Capital Inicial', 'Aportación Mensual', 'Tipo Anualizado', 'Nº de Subperíodos', 'Nº Años', 'CAPITAL FINAL'],
    'Tus datos':  [Co, d, i, m, n, Cn],
}
df = pd.DataFrame(data)

# Crear una figura y una subgráfica
fig, ax = plt.subplots()

# Ocultar los ejes
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.set_frame_on(False)

# Crear la tabla
tabla = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

# Ajustar el tamaño de la figura

fig.tight_layout()

# Mostrar la figura en una ventana
plt.show()

             # DEBERÍA SER CAPAZ DE GRAFICAR LA EVOLUCIÓN SEGÚN EL AÑO DE ESE CAPITAL
             


# Datos: en el eje vertical pongo la evolución del capital, en el eje horizontal los años 



             