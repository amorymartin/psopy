# -*- coding: utf-8 -*-
from . import helpers
import numpy as np
import matplotlib.pyplot as plt

# particle class
class Particle:
	pass

# pso class
class PSO:

	# -- Constructor
	def __init__(self, objective, lb, ub, max_iter=100, tol=1e-8,
		num_particles=20, c1=1, c2=2, w=0.6, ax=[]):
		
		self.objective = objective

		self.ub = ub
		self.lb = lb

		self.max_iter = max_iter
		self.tol = tol
		self.num_particles = num_particles
		self.c1 = c1
		self.c2 = c2
		self.w = w
		self.ax = ax

	# -- Public Methods

	# -- optimize Method
	def optimize(self):

		# 1 -- Initialization
		n = np.size(self.lb)
		particles = []
		lines = []
		for k in range(self.num_particles):
			p = Particle()
			p.x = self.lb + np.random.uniform(0, 1, n)*(self.ub - self.lb)
			p.v = self.lb + np.random.uniform(0, 1, n)*(self.ub - self.lb)
			p.best = p.x
			particles.append(p)
			l = self.ax.plot(p.x[0], p.x[1], 'k.')
			lines.append(l[0])
			# plot initil
		print(lines[0])

		swarm_best = particles[0].x
		for p in particles:
			if self.objective(p.x) < self.objective(swarm_best):
				swarm_best = p.x

		# 2 - Optimization Loop
		count = 0
		conv = np.inf
		while (count < self.max_iter and conv > self.tol):

			count = count+1
			print('It: %i f: %.2e' %(count, self.objective(swarm_best)))

			for li, p in zip(lines, particles):
				li.set_xdata(p.x[0])
				li.set_ydata(p.x[1])

			for p in particles:

				# 3 -- Evaluate fitness of particle
				if self.objective(p.x) < self.objective(p.best):
					p.best = p.x
				if self.objective(p.best) < self.objective(swarm_best):
					swarm_best = p.best

				# 4 -- Update particles
				r1 = np.random.uniform(0, 1, n)
				r2 = np.random.uniform(0, 1, n)
				p.x += p.v
				p.v = self.w*p.v + self.c1*r1*(p.best - p.x) + self.c2*r2*(swarm_best - p.x)

				# check bounds
				p.x = np.maximum(np.minimum(p.x, self.ub), self.lb)

				# conv = np.linalg.norm(x_new-p.x)
				
			plt.draw()
			plt.pause(0.2)

		return swarm_best




# def get_hmm():
#     """Get a thought."""
#     return 'hmmm...'


# def hmm():
#     """Contemplation..."""
#     if helpers.get_answer():
#         print(get_hmm())
