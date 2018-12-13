#  bat.py
#
#  Created: 07-12-18 20:02
#  Author: Qazwer - Franco Ardiles

#  bat.py
#
#  Created: 03-12-18 18:57
#  Author: Qazwer - Franco Ardiles

import random as rnd
import math
import parameters as p
import copy


def rnd_binary_list(n):
	return [rnd.randint(0, 1) for b in range(1, n + 1)]


def v_transform2(value):
	return abs(2 / math.pi) * math.atan((math.pi / 2) * value)


# Funcion sigmoide para transformacion de la velocidad a una probabilidad
def v_transform(value):
	ans = 1 / (1 + math.exp(-2 * value))
	""""
		try:
		except:
			ans = 1
	"""
	return ans


class Bat(object):

	def __init__(self, dim):
		self.f_min = p.f_min  # FRECUENCIA MINIMA
		self.f_max = p.f_max  # FRECUENCIA MAXIMA
		self.a_min = p.a_min  # LOUDNESS MINIMA
		self.a_max = p.a_max  # LOUDNESS MAXIMO
		self.r_max = p.r_max  # RATIO MAXIMO
		self.r_min = p.r_min  # RATIO#  MINIMO
		self.alpha = p.alpha  # CTE DE MODIFICACION DE LOUDNESS
		self.gamma = p.gamma  # CTE DE MODIFICACIONE DE RATIO

		self.v = [0.0] * dim
		self.bestSolution = rnd_binary_list(dim)
		self.freq = 0.0
		self.rate = p.r_0
		self.loudness = self.a_max
		self.fitness = 0.0
		self.solution = [0] * dim
		self.vars = dim
		self.quantity = 0

	def redo_rand_solution(self, dim):
		self.bestSolution = rnd_binary_list(dim)

	def update_position(self, best_bat):
		# Generacion de frecuencia aleatoria
		self.freq = self.f_min + (self.f_max - self.f_min) * rnd.uniform(0, 1)

		for i in range(self.vars):
			# Actualizacion de la velocidad del murcielago
			self.v[i] = self.v[i] + \
						(self.bestSolution[i] - best_bat.bestSolution[
							i]) * self.freq

			# Generacion de una nueva posicion para el murcielago
			rand = self.r_min + rnd.random() * (self.r_max - self.r_min)
			vtrans = v_transform(self.v[i])
			if rand < vtrans:
				if self.bestSolution[i] != 0:
					self.solution[i] = 0
				else:
					self.solution[i] = 1

	def local_to_best(self, best_bat):
		for i in range(self.vars):
			rand = rnd.random()
			if rand > self.rate:
				self.solution[i] = best_bat.bestSolution[i]

	def test_new_solution(self, fitness, i):
		rand = self.a_min + rnd.random() * (self.a_max - self.a_min)
		if rand < self.loudness and fitness < self.fitness:
			self.fitness = fitness
			self.bestSolution = copy.deepcopy(self.solution)
			self.loudness = self.alpha * self.loudness
			self.rate = self.r_max * (1 - math.exp(-self.gamma * i))
			self.quantity = 0
			for i in range(len(self.bestSolution)):
				self.quantity += self.bestSolution[i]
