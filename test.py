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

#plt.plot(x,y)

def oscar_mata_a_miyagui(miyagui):
    return 50000*miyagui

plt.plot(x,oscar_mata_a_miyagui(x))
plt.savefig("hola.pdf")