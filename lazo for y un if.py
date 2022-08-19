#Realizar un ejercicio de un programa con un lazo for y un if. 
#1.Ejercicio con una función logaritmica y sinusoidal
''
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace (0, 30, 11)
x_l = len(x)
g = np.zeros(x_l)

for i in range(x_l):
    if 0 < i < 45:
        g[i] = x[i]+ np.log(x[i])+ np.sin(x[i])
print (g)

plt.plot(x,g)
plt.show()
'''

#2.Ejercicio para encontrar el error maximo y la norma

'''
import numpy as np

sol_num= np.linspace (0, 30, 11)
x_l = len(sol_num)
error=np.zeros(x_l)

sum_absoluto=0.0

error_max=-1.0

for i in range (len(sol_num)):
    sol_exacta=np.exp(sol_num[i])
    if sol_exacta == 0.0:
        error[i]=0.0
    else:
        error[i]=abs((sol_exacta-sol_num[i])/sol_exacta)
        if error[i] > error_max: error_max = error[i]

    sum_absoluto= sum_absoluto + abs((sol_num[i] - sol_exacta)/sol_exacta)

norma=sum_absoluto
print("error_max: ",error_max)
print ('norma: ',norma)
