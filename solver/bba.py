#  swarm.py
#
#  Created: 03-12-18 18:57
#  Author: Qazwer - Franco Ardiles

import bat


class BBA(object):

	def __init__(self, population, problem, history=False):
		self.bestBat = None					# MEJOR MURCIELAGO ENCONTRADO
		self.population = population		# TAMANNO POBLACION MURCIELAGOS
		self.dim = problem.dim				# DIMENSION DE LA RESPUESTA
		self.bats = None
		self.problem = problem
		if history:
			self.history = {
				"solution": None,
				"fitness": None,
				"objective": None,
				"mean_loudness": None,
				"mean_rate": None,
			}
		else:
			self.history = None

	# Inicia la busqueda de Bat Algorithm
	def search(self, iterations):
		# Estos valores son modificados si se desea guardar la historia de
		# avance durante las iteraciones
		sol = []
		fit = []
		obj = []
		loud = []
		rate = []
		mean_loudness = 0
		mean_rate = 0

		self.create_bats()

		for it in range(iterations):
			for b in self.bats:
				while True:
					b.update_position(self.bestBat)
					b.local_to_best(self.bestBat)
					if self.problem.hard_restriction(b.solution):
						break
				b.test_new_solution(self.problem.evaluate(b.solution), it)

			for b in self.bats:
				if b.fitness < self.bestBat.fitness:
					self.bestBat = b
					# print "NUEVO: ", self.problem.objectivef(self.bestBat.bestSolution)
	#  ^^^^^^^^^^^^^^^^^^^^^FIN DE BAT ALGORITHM^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

	#  DESDE AQUI ES PRINCIPALMENTE RECOLECCION DE INFORMACION PARA GRAFICAR

				if self.history is not None:
					mean_loudness += b.loudness
					mean_rate += b.rate
			if self.history is not None:
				rate.append(mean_rate/self.population)
				loud.append(mean_loudness/self.population)
				obj.append(self.problem.objectivef(self.bestBat.bestSolution))
				fit.append(self.bestBat.fitness)
				sol.append(self.bestBat.bestSolution)
				mean_loudness = 0
				mean_rate = 0
		if self.history is not None:
			self.history["solution"] = sol
			self.history["fitness"] = fit
			self.history["objective"] = obj
			self.history["mean_loudness"] = loud
			self.history["mean_rate"] = rate
		return self.problem.objectivef(self.bestBat.bestSolution)

	# Inicializacion de los murcielagos en una posicion aleatoria
	def create_bats(self):
		self.bats = []
		self.bestBat = None
		for i in range(self.population):
			b = bat.Bat(self.dim)
			b.fitness = self.problem.evaluate(b.bestSolution)
			self.bats.append(b)
			if self.bestBat is None or self.bestBat.fitness > b.fitness:
				self.bestBat = b
