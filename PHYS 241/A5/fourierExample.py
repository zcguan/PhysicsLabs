#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This Python script is designed to compute a single Fourier series expansion and plot it as a function of time.
"""

import matplotlib.pyplot as plt
import numpy as np

numPlot=1000 #number of points to plot
nFourier=4; #number of terms to include in Fourier sum 
T=1 # wave period
omega_o=(2*np.pi)/T # wave fundamental frequency
tmin=-2 #min time
tmax=2 #max time
Vo=.5 #constant term in Fourier sum 

#In order to change the Fourier series, you need to modify the amplitude function and possibly Vo
#(currently set to plot sawtooth function from lecture)
amp=lambda n: 4.0/(np.pi**2*n**2)
#VERY IMPORTANT:  write all numbers in amp function with an extra zero decimal, e.g. instead of 2*n-1 write 2.0*n-1--this will avoid problems with python rounding to nearest integer
#np.pi:  pi=3.14159. . .
#** is Python syntax for exponentiation, e.g. 2**2=4, 2**3=8, x**a=x^a

#This defines one Fourier component with amplitude amp(n); may also need to modify
fourierComponent=lambda t, n, omega_o: amp(n)*np.cos(omega_o*n*t)
#np.sin is sine; np.cos is cosine

"""
No need to modify anything below this line if only desire to plot a single series
"""

#This sums Fourier components including nFourier terms: in sum n ranges from 1 to nFourier
def fourierSum(t, Vo, omega_o, nFourier):
  series=np.array([fourierComponent(t, n, omega_o) for n in range(1, (nFourier+1),2)])
  return Vo+series.sum()

#Defines time-values
t=np.linspace(tmin, tmax, numPlot)

#Defines and computes corresponding voltage values
# V=np.zeros(numPlot)
# for i in range(numPlot):
#    V[i]=fourierSum(t[i], Vo, omega_o, nFourier)




f,axs = plt.subplots(2,2, sharex = True, sharey = True, gridspec_kw={'hspace': 0, 'wspace': 0})
ax = list(axs[0]) + list(axs[1])
plt.ylim(-.2,1.3)
for j in range(1,nFourier + 1):
	V=np.zeros(numPlot)
	for i in range(numPlot):
	   V[i]=fourierSum(t[i], Vo, omega_o, j)

	ax[j-1].plot(t, V, label=str(j)+' terms')
	ax[j-1].legend()


f.text(0.5, 0.04, 't', ha='center', va='center')
f.text(0.05, 0.5, 'V(t)', ha='center', va='center', rotation='vertical')

for ax in axs.flat:
    ax.label_outer()

plt.savefig('q3.png', bbox_inches='tight')
plt.show()
