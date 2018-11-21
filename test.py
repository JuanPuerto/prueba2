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
plt.show()