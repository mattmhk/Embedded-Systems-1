import matplotlib.pyplot as plt
import math

step_size= (2* math.pi)/36
ax=[]
ay=[]

for i in range(0,36):
    y_value=math.sin(i*step_size)
    ax.append(i)
    ay.append(y_value)
    
plt.plot(ax,ay, 'ro', label='sin(x)')
plt.legend()
plt.show()