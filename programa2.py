import numpy as np
#Matplotlib tiene muchos módulos. importar un solo módulo
import matplotlib.pyplot as plt
#Dibujar una función seno
#CRear en ndarray de 1 dimensión 100 elementos equiespaciados, de 0 a 2*PI
x=np.linspace(0,2*np.pi, 100)
y=np.sin(x)
#Usar matplotlib
#Definir el tamaño de la figura a generar, comando figure
plt.figure(figsize=(8,4))
#Título a la grafica
plt.title("Mi primer gráfico científico en programación")
#plot->grafico
plt.plot(x,y)
#Nombre a los ejes
plt.xlabel("x")
plt.ylabel("seno de x")
#Grilla a la grafica
plt.grid(True)
#Mostrar el grafico->show
plt.show()



