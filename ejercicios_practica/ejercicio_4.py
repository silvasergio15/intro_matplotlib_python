# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
from turtle import color

import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Line Plot: Figura con múltiples gráficos")

    # NOTA: aproveche los ejemplos "line_plot" y "scatter_plot" de clase

    # Se desea graficar cuatro funciones en una misma figura
    # en cuatros gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de "X":
    x = np.linspace(0, 10, 40)

    # Realizar tres gráficos que representen
    # y1 = x^2 (X al cuadrado)
    # y2 = x^3 (X al cubo)
    # y3 = x^4 (X a la cuarta)
    # y4 = raiz_cuadrada(X)

    # Implementación:
    y1 = x**2
    y2 = x**3
    y3 = x**4
    y4 = np.sqrt(x)

    # Alumnos: Esos cuatro gráficos deben estar colocados
    # en la diposición de 2 filas y 2 columna:
    # ------
    #  graf1 | graf2
    # ------
    #  graf3 | graf4
    # Utilizar add_subplot para lograr este efecto
    # de "2 filas" "2 columna" de gráficos
    
    # y1 = []
    # for i in x:
    #     y1.append(i**2)
        
    fig = plt.figure()
    fig.suptitle('ejercicio 4', fontsize=22)

    ax1 = fig.add_subplot(2,2,1)  # 2 fila, 2 columnas, axes nº1
    ax1.set_xlabel("eje x")
    ax1.set_ylabel("eje y")
    ax1.set_title("y1")
    
    ax1.plot(x,y1, color="b")

    ax2= fig.add_subplot(2, 2, 2)  # 2 fila, 2 columnas, axes nº2
    ax2.plot(x,y2, color ="y") 
    ax2.set_xlabel("eje x")
    ax2.set_ylabel("eje y")
    ax2.set_title("y2")




    ax3= fig.add_subplot(2, 2, 3)  # 2 fila, 2 columnas, axes nº3
    ax3.scatter(x,y3 , color="r")
    ax3.set_xlabel("eje x")
    ax3.set_ylabel("eje y")
    ax3.set_title("y3")



    ax4=fig.add_subplot(2,2,4)      # 2 fila, 2 columnas, axes nº3
    ax4.plot(x,y4, color="k")
    ax4.set_xlabel("eje x")
    ax4.set_ylabel("eje y")
    ax4.set_title("y4")
        #ax3= fig.add_subplot(2, 2, 3)  # 2 fila, 2 columnas, axes nº1
        #ax4= fig.add_subplot(2, 2, 4)  # 2 fila, 2 columnas, axes nº2
    
    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un color distinto
    # a su elección

    # Colocar una grilla a elección
    ax1.grid(color="y")
    ax2.grid(color="r")
    ax3.grid(color="b")
    ax4.grid(color="c")

    # Crear acá su gráfico
    plt.tight_layout()
    plt.show()
    print("terminamos")
