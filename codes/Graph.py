
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10 ,11)
y = np.linspace(0,1,11)

plt.xlabel('Random varaibles')
plt.ylabel('F(x)')
plt.axhline(y = 1, color = 'r', linestyle = '--')
plt.axvline(x = 5.5,ymin=0.5,ymax=0.6, color = 'b', linestyle = '--')
plt.axvline(x = 4.5,ymin=0,ymax=0.5, color = 'b', linestyle = '--')
plt.annotate('$P_i$',(5.7,0.54),size=12,color='red')
plt.annotate('$x_i$',(4.7,-0.04),size=12,color='red')   
plt.step(x, y)
plt.show()