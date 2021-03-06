"""
This Python script is designed to plot the sawtooth input and output for the integrator example in lecture
"""

import matplotlib.pyplot as plt
import numpy as np

numPlot=1000 #number of points to plot
nFourier=20; #number of terms to include in Fourier sum 
T=1 # wave period
omega_o=(2*np.pi)/T # wave fundamental frequency
tmin=-T*2 #min time
tmax=T*2 #max time
Vo_in=0 #constant term in input sum 
tau=1 #RC time constant
v0 = 1

#This defines the amplitude of transfer function (|H(omega)|):
ampTransfer=lambda n, omega_o, tau: omega_o*n*tau/np.sqrt(1+(omega_o*n*tau)**2)
#do not use **(1/2) to take square-root, use np.sqrt()!

#This defines the phase shft phi:
phaseShift=lambda n, omega_o, tau: np.arctan(1/(omega_o*n*tau))

#amp:  amplitude of input function--currently set to plot sawtooth function from lecture
amp=lambda n: (-v0*(-1)**n/(n*np.pi))
#np.pi:  pi=3.14159. . .
#** is Python syntax for exponentiation, e.g. 2**2=4, 2**3=8

#This defines a Fourier component with amplitude amp1(n) and a Fourier component with amplitude amp2(n)
fourierComponent1=lambda t, n, omega_o: amp(n)*np.sin(omega_o*n*t)
fourierComponent2=lambda t, n, omega_o, tau: amp(n)*ampTransfer(n, omega_o, tau)*np.sin(omega_o*n*t+phaseShift(n, omega_o, tau))
#np.sin is sine; np.cos is cosine

"""
No need to modify anything below this line if only desire to plot two series
"""

#This sums Fourier components including nFourier terms: in sum n ranges from 1 to nFourier
def fourierSum1(t, Vo_in, omega_o, nFourier):
  series=np.array([fourierComponent1(t, n, omega_o) for n in range(1, (nFourier+1))])
  return Vo_in+series.sum()

def fourierSum2(t, Vo_in, omega_o, tau, nFourier):
  series=np.array([fourierComponent2(t, n, omega_o, tau) for n in range(1, (nFourier+1))])
  return Vo_in*ampTransfer(0, omega_o, tau)+series.sum()
#Vo_in*ampTransfer(0, omega_o, tau)
#Defines time-values
t=np.linspace(tmin, tmax, numPlot)

#Defines and computes corresponding voltage values
V1=np.zeros(numPlot)
V2=np.zeros(numPlot)
for i in range(numPlot):
   V1[i]=fourierSum1(t[i], Vo_in, omega_o, nFourier)
   V2[i]=fourierSum2(t[i], Vo_in, omega_o, tau, nFourier)

#blue shows input; red gives output
plt.figure()
plt.plot(t, V1, 'b', label='$V_{in}$')
plt.plot(t, V2, 'r', label='$V_{out}$')
plt.xlabel('t')
plt.ylabel('V(t)')
plt.title('T={} ms'.format(T))
plt.legend()
plt.savefig('q4t{}.png'.format(T), bbox='tight')
plt.show()