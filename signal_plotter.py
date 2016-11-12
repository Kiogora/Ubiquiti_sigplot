import numpy as np
import matplotlib.pyplot as plt

#generate array from csv
csv=np.genfromtxt('signal.csv',delimiter=",")

x_spacing=50

#Choose dB values only and form an array
values=csv[:,0]

#form a running variable based on 'dBm' column size. 
t=np.arange(values.shape[0])

time=csv[:,2][np.arange(0,values.shape[0],x_spacing)]

print time

plt.plot(t,values)

plt.xticks(np.arange(0,values.shape[0],x_spacing),time.astype(int))

plt.show()
