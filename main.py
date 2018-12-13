#  main.py
#
#  Created: 03-12-18 18:57
#  Author: Qazwer - Franco Ardiles

import matplotlib.pyplot as plt
import argparse
import random
import sys
import os
sys.path.append(os.getcwd()+"\\solver")
sys.path.append(os.getcwd()+"\\problem")
try:
	import problem
	import bba
except ImportError:
	raise

problema = problem.SCP()
plotmap = False


def plot(population, iterations):
	bats = bba.BBA(population, problema, True)
	sol = bats.search(iterations)
	print "objetivo\t=\t", sol
	x = []
	for i in range(iterations):
		x.append(i)
	plt.figure(1)
	plt.suptitle("SCP")
	plt.subplot(221)
	plt.title("Convergencia")
	plt.xlabel("iteracion")
	plt.ylabel("fitness")
	plt.plot(x, bats.history.get("fitness"), marker='', color='green', linewidth=1)

	plt.subplot(222)
	plt.title("Funcion objetivo")
	plt.xlabel("iteracion")
	plt.ylabel("valor")

	plt.plot(x, bats.history.get("objective"), marker='', color='red', linewidth=1)

	plt.subplot(223)
	plt.title("Amplitud media")
	plt.xlabel("iteracion")
	plt.ylabel("amplitud")
	plt.plot(
		x, bats.history.get("mean_loudness"), marker='', color='blue', linewidth=1)

	plt.subplot(224)
	plt.title("Tasa de emision media")
	plt.xlabel("iteracion")
	plt.ylabel("rate")
	plt.plot(
		x, bats.history.get("mean_rate"), marker='', color='red',
		linewidth=1)
	print "fitness\t=\t", bats.bestBat.fitness
	print "best s.\t=\t", bats.bestBat.bestSolution
	print "antenas\t=\t", bats.bestBat.quantity
	if args.plotmap:
		print "comunas\t=\t",
		plt.figure(2)
		plt.title("comunas")
		im = plt.imread("problem\\comunas.PNG")
		plt.imshow(im)

		for i in range(len(bats.bestBat.bestSolution)):
			if bats.bestBat.bestSolution[i] == 1:
				par = problema.variables.get(i+1)[2]
				plt.scatter(par[0], par[1], c="blue")
				print i+1,
	plt.show()


def estimar(population, iterations, sample):
	bats = bba.BBA(population, problema)
	x = []
	var = 0
	bat = []
	for i in range(sample):
		x.append(bats.search(iterations))
		bat.append(bats.bestBat)
		print x[i]
	print
	mean = sum(x) / len(x)
	for i in range(len(x)):
		var += (x[i] - mean) ** 2
	var /= (len(x) - 1)
	print "media\t=\t",   mean
	print "desv E.\t=\t", var ** 0.5
	print "best s.\t=\t", bat[x.index(min(x))].bestSolution,  min(x)
	print "comunas\t=\t",
	if args.plotmap:
		plt.title("comunas")
		im = plt.imread("problem\\comunas.PNG")
		plt.imshow(im)
		for i in range(len(bat[x.index(min(x))].bestSolution)):
			if bat[x.index(min(x))].bestSolution[i] == 1:
				par = problema.variables.get(i + 1)[2]
				plt.scatter(par[0], par[1], c="blue")
				print i+1,
		print
	print "antenas\t=\t", bat[x.index(min(x))].quantity
	plt.show()


parser = argparse.ArgumentParser(
	formatter_class=argparse.ArgumentDefaultsHelpFormatter,
	description=
	"Resuelve una instancia de SCP utilizando Binary Bat Algorithm.")
parser.add_argument(
	"-p", "--poblacion", metavar='', default=60, type=int,
	help="Poblacion de murcielagos que utilizara el algoritmo"
)
parser.add_argument(
	"-i", "--iteracion", metavar='', default=600, type=int,
	help="Numero de iteraciones que realizara el algoritmo"
)
parser.add_argument(
	"-s", "--sample", metavar='', default=10, type=int,
	help="Tamanno de la muestra para obtencion de media y desv. estandar"
)
parser.add_argument(
	"-g", "--graficar", action='store_true',
	help="Permite graficar una busqueda, no se realiza una muestra de ejecuciones"
)

parser.add_argument(
	"--seed", metavar='', default=None, type=int, help=
	"Recibe una semilla para iniciar la funcion random de manera determinada."
	" La mejor encontrada hasta ahora es: 1586"
)

parser.add_argument(
	"--plotmap", metavar='', default=False, type=int, help=
	"Dibuja el mapa e indicia las ciudades que tienen antenas en el problema "
	"SCP de ejemplo"
)

if __name__ == '__main__':
	args = parser.parse_args()
	if args.seed is not None:
		random.seed(args.seed)
	if args.graficar:
		plot(args.poblacion, args.iteracion)
	else:
		estimar(args.poblacion, args.iteracion, args.sample)
