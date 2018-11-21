# Ejercicio5
# imprima el mensaje: "hola mundo!" 
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
print("hola mundo!")

# Algo mas
x = np.linspace(0,10,100)
y = np.linspace(0,10,100)

print(x)
print(y)

plt.plot(x,y)
plt.savefig("hola1.pdf")

def oscar(miyagui):
    return 50000*miyagui

plt.plot(x,oscar(x))
plt.savefig("hola.pdf")

#slicing

goku = np.array(["ssj1","ssj2","ssj3","God","ssjBlue","UltraInstinct"])
print(goku)
print(goku[2:5])

