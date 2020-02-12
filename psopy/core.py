# -*- coding: utf-8 -*-
from . import helpers
import numpy as np

# pso class
class pso:

	# -- Constructor
	def __init__(self, objective, lb, ub, max_iter=100, tol=1e-8):
		self.objective = objective

		self.max_iter = max_iter
		self.tol = tol
		self.delta = delta
		self.num_particles = num_particles
		self.c1 = c1

	# -- Public Methods

	# -- optimize Method
	def optimize():

		# 1 -- Initialization
		count = 0

		while (count < self.max_iter and conv < self.tol):

			# 2 -- Update 
			count = count+1
			r1 = np.random.uniform()
			r2 = np.random.uniform()

			v_new = w*v + self.c1*r1*(pi-x) + self.c2*r2*(pg-x)
			v_new =
			conv = nor

			# 3 -- Evaluate fitness of particle

			for particle in num_particles:
				if f[particle]<
					fbest = f[particle]

		return x, f




# def get_hmm():
#     """Get a thought."""
#     return 'hmmm...'


# def hmm():
#     """Contemplation..."""
#     if helpers.get_answer():
#         print(get_hmm())
