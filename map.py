import numpy as np
import matplotlib.pyplot as plot
x = np.linspace(-np.pi, np.pi, 50)
y1 = np.sin(x)
y2 = np.cos(x)

plot.plot(x,y1, color = 'blue', marker = "s" , label="Sin(x)")
plot.plot(x,y2, color = 'red', marker = "s" , label="Cos(x)")
plot.legend()
plot.show()