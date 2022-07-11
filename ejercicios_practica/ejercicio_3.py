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
    print("Scatter Plot")

    # NOTA: aproveche los ejemplos "scatter_plot" de clase

    # Se desea graficar la función tanh para el siguiente
    # intervalor de valores de "X"
    x = np.arange(-np.pi, np.pi, 0.1)

    # Función y = tanh(x) --> tangente hiperbólica
    y = np.tanh(x)

    # Alumno: Graficar la función utilizando "scatter"
    # utilizando "x" e "y" ya disponible
    fig= plt.figure()
    ax= fig.add_subplot()
   
    ax.scatter(x, y, color="r", label="tangente", marker="<")
    ax.set_xlabel("EJE X",color="r")
    ax.set_ylabel("EJE Y", color="g")
    plt.suptitle("ejercicio 3")

    ax.legend()
    
    

    # Colocar la leyenda y el label con el nombre de la función

    # Elegir un marker a elección

    # Crear acá su gráfico
    plt.show()
    
    print("terminamos")
