# https://psychology.stackexchange.com/questions/13347/how-can-i-fit-a-psychometric-function-such-that-the-minimum-is-50-chance-level
# chance = 0.5  # between 0 and 1
# y = chance + (1-chance) / (1 + np.exp(-k*(x-x0)))
# plot standard deviation　https://stackoverflow.com/questions/22481854/plot-mean-and-standard-deviation


import numpy as np
import pylab
from scipy.optimize import curve_fit

def sigmoid(x, x0, k):
     # y = 0.5 + (1-0.5) / (1 + np.exp(-k*(x-x0)))
     y =  1 / (1 + np.exp(-k*(x-x0)))
     return y

xdata = np.array([0.0,1.0,3.0,5.0,7.0,9.0])
ydata = np.array([60,87.5,90,92.5,92.5,92.5])/100
edata = np.array([22.36,12.99,7.07,8.29,8.29,8.29])/100

popt, pcov = curve_fit(sigmoid, xdata, ydata)
print (popt)

x = np.linspace(0, 10, 50)
y = sigmoid(x, *popt)*100 # percentage

#pylab.plot(xdata, ydata*100, 'o', label='data')
pylab.errorbar(xdata,ydata*100,yerr=edata*100,fmt='o',ecolor='gray',color='black',elinewidth=1,capsize=4)

pylab.plot(x,y, 'r',label='fit')
pylab.xlim(0, 10)
pylab.ylim(0, 100)
pylab.xlabel("Time Interval(s)", fontsize = 16)
pylab.ylabel("% Hot Judgement", fontsize =16)
#pylab.legend(loc='best')

# plot 75% threshold
datax1 = [0,0.52]
datay1 = [75,75]
plot1 = pylab.plot(datax1,datay1,'--r')
datax2 = [0.52,0.52]
datay2 = [0.0,75]
plot1 = pylab.plot(datax2,datay2,'--r')

pylab.text(0.25, -5, 'Threshold', color="red")
pylab.text(0.4, -8, '0.52', color="red")
pylab.text(-0.5, 73, '75', color="red")
pylab.show()
