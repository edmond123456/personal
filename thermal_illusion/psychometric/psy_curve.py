# https://psychology.stackexchange.com/questions/13347/how-can-i-fit-a-psychometric-function-such-that-the-minimum-is-50-chance-level
# chance = 0.5  # between 0 and 1
# y = chance + (1-chance) / (1 + np.exp(-k*(x-x0)))

import numpy as np
import pylab
from scipy.optimize import curve_fit

def sigmoid(x, x0, k):
     # y = 0.5 + (1-0.5) / (1 + np.exp(-k*(x-x0)))
     y =  1 / (1 + np.exp(-k*(x-x0)))
     return y

xdata = np.array([0.0,1.0,3.0,5.0,7.0,9.0])
ydata = np.array([60,87.5,90,92.5,92.5,92.5])/100

popt, pcov = curve_fit(sigmoid, xdata, ydata)
print (popt)

x = np.linspace(0, 10, 50)
y = sigmoid(x, *popt)

pylab.plot(xdata, ydata, 'o', label='data')
pylab.plot(x,y, label='fit')
pylab.xlim(0, 10)
pylab.ylim(0, 1.00)
pylab.xlabel("Time Interval(s)")
pylab.ylabel("Hot Judgement")
#pylab.legend(loc='best')

# plot 75% threshold
datax1 = [0,0.3,0.4,0.5,0.52]
datay1 = [0.75,0.75,0.75,0.75,0.75]
plot1 = pylab.plot(datax1,datay1,'--g')
datax2 = [0.52,0.52]
datay2 = [0.0,0.75]
plot1 = pylab.plot(datax2,datay2,'--g')

pylab.show()