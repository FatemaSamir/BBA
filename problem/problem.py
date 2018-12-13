#  problem.py
#
#  Created: 03-12-18 18:57
#  Author: Qazwer - Franco Ardiles

"""
EJEMPLO DE CLASE PROBLEMA
UTILIZADO PARA LA RESOLUCION DE PROBLEMAS DE LA METAHEURISTICA DE BAT ALGORITHM
"""


class KnapSack(object):
	"""
	DEFINICION DE VARIABLES Y LIMITES
	"""

	def __init__(self, max_cost=220):
		# MATRIZ: [ [COSTO, VALOR] ]
		self.variables = [
			[52, 100],
			[23, 80],
			[35, 45],
			[15, 36],
			[10, 26],
			[71, 120],
			[30, 65],
			[24, 100],
			[16, 45],
			[78, 89],
			[34, 48],
			[23, 45],
			[28, 49],
			[34, 48],
			[13, 18],
		]
		# LIMITE PESO MAXIMO
		self.max_cost = max_cost
		self.dim = 15

	# METODOS PARA LA RESOLUCION DEL PROBLEMA

	"""
	FUNCIONES ESENCIALES PARA LA RESOLUCION DE UN PROBLEMA
	"""
	# FUNCION OBJETIVO: RESULTADO DEL VALOR OBTENIDO DE ACUERDO A UNA SOLUCION
	# ENTREGADA POR LA METAHEURISTICA
	def objectivef(self, lista):
		total = 0
		for i in range(len(lista)):
			if lista[i] != 0:
				total += self.variables[i][1]
		return total

	# EVALUA LA SOLUCION DE LA METAHEURISTICA Y RETORNA UN FITNESS CALCULADO
	# A BASE DE CONDICIONES DADAS
	def evaluate(self, lista):
		delta = self.max_cost - self.costo(lista)
		value = self.objectivef(lista)
		if delta > 0:
			return -1 * value
		return abs(delta*100)**4 - 1 * value

	# FUNCION PARA DELIMITAR EL RANGO A SOLO RESPUESTAS VALIDAS CUANDO HAY
	# RESTRICCIONES DURAS, RETORNA FALSE SI LA RESPUESTA NO ES SATISFACTORIA Y
	# HACE QUE SE RECALCULE LA RESPUESTA OBTENIDA
	def hard_restriction(self, lista):
		# DO SOMETHING OR NOTHING
		# EJEMPLO: TABOO LIST
		return True

	"""
	FUNCIONES DE APOYO PARA CALCULO DE FITNESS Y OBJETIVO
	"""

	# CALCULA EL COSTO DE UNA RESPUESTA DETERMINADA
	def costo(self, lista):
		cost = 0
		for i in range(len(lista)):
			if lista[i] != 0:
				cost += self.variables[i][0]
		return cost


class SCP(object):
	"""
	DEFINICION DE VARIABLES Y LIMITES
	"""

	def __init__(self):
		# VARIABLES: [[vecinos], costo ,[coordenadas]]
		self.variables = {
			1: [[], 100, [0, 0]],
			2: [[3, 4, 28], 1, [263, 241]],
			3: [[2, 5, 28, 29], 2, [325, 245]],
			4: [[2, 3, 25, 26, 28, 29], 1.2, [234, 220]],
			5: [[3, 27, 29], 1.5, [302, 182]],
			6: [[7, 9, 15, 24, 27], 3, [190, 123]],
			7: [[6, 8, 9, 10, 15], 2, [121, 98]],
			8: [[7, 10], 1, [92, 123]],
			9: [[6, 7], 1, [195, 49]],
			10: [[7, 8, 15, 33], 3, [102, 159]],
			11: [[12, 13, 15, 16, 17, 24, 25], 4, [156, 223]],
			12: [[11, 13, 15], 3, [133, 202]],
			13: [[11, 12, 15, 17, 33], 3, [116, 207]],
			14: [[16, 17, 31, 34, 37], 2, [107, 249]],
			15: [[6, 7, 10, 11, 12, 13, 24, 33], 2.5, [132, 179]],
			16: [[11, 14, 17, 34], 1.5, [152, 263]],
			17: [[11, 13, 14, 16, 31, 33, 35], 2, [107, 230]],
			18: [[20, 30, 36], 2, [46, 331]],
			19: [[21, 22, 30], 3, [80, 386]],
			20: [[18, 21, 30], 2, [34, 356]],
			21: [[19, 20, 30], 2, [49, 372]],
			22: [[19, 23], 3, [75, 419]],
			23: [[22], 2, [31, 451]],
			24: [[6, 11, 15, 25, 26, 27, 28], 3, [184, 184]],
			25: [[4, 11, 24, 26], 3, [187, 223]],
			26: [[4, 24, 25, 28], 1, [208, 202]],
			27: [[5, 6, 28, 29], 2.5, [267, 126]],
			28: [[2, 3, 4, 24, 26, 27, 29], 2, [218, 182]],
			29: [[3, 5, 27, 28], 3.5, [253, 178]],
			30: [[18, 19, 20, 21, 34, 36], 3, [83, 328]],
			31: [[14, 17, 34, 35, 38], 1.5, [74, 240]],
			32: [[], 100, [0, 0]],
			33: [[10, 13, 15, 17, 35], 2, [89, 186]],
			34: [[14, 16, 30, 31, 36, 37, 38], 2, [115, 297]],
			35: [[17, 31, 33], 3.5, [77, 217]],
			36: [[30, 34, 38], 2, [50, 283]],
			37: [[14, 34], 2.5, [108, 274]],
			38: [[31, 34, 36], 1.5, [66, 262]],
		}

		self.dim = 38

	# METODOS PARA LA RESOLUCION DEL PROBLEMA

	"""
	FUNCIONES ESENCIALES PARA LA RESOLUCION DE UN PROBLEMA
	"""
	# FUNCION OBJETIVO: RESULTADO DEL VALOR OBTENIDO DE ACUERDO A UNA SOLUCION
	# ENTREGADA POR LA METAHEURISTICA
	def objectivef(self, lista):
		total = self.costo(lista)
		return total

	# EVALUA LA SOLUCION DE LA METAHEURISTICA Y RETORNA UN FITNESS CALCULADO
	# A BASE DE CONDICIONES DADAS
	def evaluate(self, lista):
		value = self.objectivef(lista)
		penal, antennas = self.penalization(lista)
		alfa = 0.0
		# COMPLETAR
		return value + penal + (antennas - 1)*alfa

	# FUNCION PARA DELIMITAR EL RANGO A SOLO RESPUESTAS VALIDAS CUANDO HAY
	# RESTRICCIONES DURAS, RETORNA FALSE SI LA RESPUESTA NO ES SATISFACTORIA Y
	# HACE QUE SE RECALCULE LA RESPUESTA OBTENIDA
	def hard_restriction(self, lista):
		# DO SOMETHING OR NOTHING
		return True

	"""
	FUNCIONES DE APOYO PARA CALCULO DE FITNESS Y OBJETIVO
	"""
	def costo(self, lista):
		total = 0
		for i in range(len(lista)):
			if lista[i] != 0:
				total += self.variables.get(i+1)[1]
		return total

	def penalization(self, lista):
		n = 0
		antenna = 0
		covering_area = [0]*38
		for i in range(len(lista)):
			if lista[i] != 0:
				covering_area[i] = 1
				covered = self.variables.get(i+1)[0]
				for comuna in covered:
					covering_area[comuna-1] = 1

		for i in range(len(covering_area)):
			if i == 0 or i == 31:
				continue
			elif covering_area[i] == 0:
				n += 1
			else:
				antenna += 1

		return n*100, antenna
