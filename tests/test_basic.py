# -*- coding: utf-8 -*-

"""
python3 -m tests.test_basic
"""

from . import context

from . import test_functions

import numpy as np
import matplotlib.pyplot as plt


from source.pso import PSO

# import unittest

# cd /Users/amorymartin/Documents/Github/psopy

if __name__ == '__main__':
    

	objective = lambda x:test_functions.rosenbrock(x)
	

	X, Y  = np.meshgrid(np.linspace(-5, 5, 1000), np.linspace(-5, 5, 1000))
	Z = objective([X, Y])

	plt.ion()
	plt.figure()
	fig, ax = plt.subplots()
	cs = ax.contour(X, Y, 10+np.log(Z), cmap='jet')
	ax.clabel(cs, inline=1, fontsize=10)

	opt = PSO(objective, lb=np.array([-3, -3]), ub=np.array([3, 3]), max_iter=50,ax=ax)
	xopt = opt.optimize()
	print('Local minimum: %.2f %.2f' %(xopt[0], xopt[1]))