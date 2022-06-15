import numpy as np 
from bokeh.plotting import figure, show, output_notebook 
from bokeh.layouts import gridplot 
from bokeh.io import push_notebook 
def local_regression(x0, X, Y, tau): 
  x0 = np.r_[1, x0] 
  X = np.c_[np.ones(len(X)), X] 
  xw = X.T * radial_kernel(x0, X, tau)
  beta = np.linalg.pinv(xw @ X) @ xw @ Y
  return x0 @ beta
def radial_kernel(x0, X, tau): 
  return np.exp(np.sum((X - x0) ** 2, axis=1) / (-2 * tau * tau)) 
def plot_lwr(tau): 
  prediction = [local_regression(x0, X, Y, tau) for x0 in domain] 
  plot = figure(plot_width=400, plot_height=400) 
  plot.title.text='tau=%g' % tau 
  plot.scatter(X, Y, alpha=.3) 
  plot.line(domain, prediction, line_width=2, color='red') 
  return plot 
n = 1000 

X = np.linspace(-3, 3, num=n) 
print("The Data Set ( 10 Samples) X :\n",X[1:10]) 
Y = np.log(np.abs(X ** 2 - 1) + .5) 
print("The Fitting Curve Data Set (10 Samples) Y :\n",Y[1:10]) 

X += np.random.normal(scale=.1, size=n) 
print("Normalised (10 Samples) X :\n",X[1:10]) 
domain = np.linspace(-3, 3, num=300) 
print(" Xo Domain Space(10 Samples) :\n",domain[1:10]) 
show(gridplot([ 
[plot_lwr(10.), plot_lwr(1.)], 
[plot_lwr(0.1), plot_lwr(0.01)]
            ]))


'''

Output

The Data Set ( 10 Samples) X : 
[-2.99399399 -2.98798799 -2.98198198 -2.97597598 -2.96996997 -2.96396396 
-2.95795796 -2.95195195 -2.94594595] 
The Fitting Curve Data Set (10 Samples) Y : 
[2.13582188 2.13156806 2.12730467 2.12303166 2.11874898 2.11445659 
2.11015444 2.10584249 2.10152068] 
Normalised (10 Samples) X : 
[-3.10518137 -3.00247603 -2.9388515 -2.79373602 -2.84946247 -2.85313888 
-2.9622708 -3.09679502 -2.69778859] 
Xo Domain Space(10 Samples) : 
[-2.97993311 -2.95986622 -2.93979933 -2.91973244 -2.89966555 -2.87959866 
            -2.85953177 -2.83946488 -2.81939799]
'''
