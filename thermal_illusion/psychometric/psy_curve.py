# https://psychology.stackexchange.com/questions/13347/how-can-i-fit-a-psychometric-function-such-that-the-minimum-is-50-chance-level
# chance = 0.5  # between 0 and 1
# y = chance + (1-chance) / (1 + np.exp(-k*(x-x0)))

import numpy as np
import pylab
from scipy.optimize import curve_fit

def sigmoid(x, x0, k):
     y = 1 / (1 + np.exp(-k*(x-x0)))
     return y

xdata = np.array([0.0,1.0,3.0,5.0,7.0,9.0])
ydata = np.array([0.6,0.875,0.9,0.925,0.925,0.925])

popt, pcov = curve_fit(sigmoid, xdata, ydata)
print (popt)

x = np.linspace(-10, 10, 50)
y = sigmoid(x, *popt)

pylab.plot(xdata, ydata, 'o', label='data')
pylab.plot(x,y, label='fit')
pylab.ylim(0, 1.00)
pylab.legend(loc='best')
pylab.show()