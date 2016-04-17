from genetic import *
from image import *
from snn import *
import math, random

def convert_binary(data, w, h, t):
	ans = [[0 for x in xrange(w)] for x in xrange(h)]
	for x in xrange(h):
		for y in xrange(w):
			if data[x][y] > t:
				ans[x][y] = 1
			else:
				ans[x][y] = 0
	return ans

def shenon_entropy(data, w, h):
	black, white = 0,0
	for x in xrange(h):
		for y in xrange(w):
			if data[x][y]:
				white += 1
			else:
				black += 1

	total = w*h
	prob_white = white / (total*1.0)
	prob_black = black / (total*1.0)

	formula = - (prob_black * math.log(prob_black,2) + prob_white * math.log(prob_white, 2))

	return formula

def fitness(population, data, w, h):
	fitness_dict = {}
	for x in population:
		ans = convert_binary(data, w, h, x)
		entropy = shenon_entropy(ans, w, h)
		if entropy in fitness_dict:
			entropy = entropy + random.random()/1000
		fitness_dict[entropy] = x
		# imagewrite(ans, w, h)
		# print entropy, x
	return fitness_dict


# read image
pixel, w, h = imageread('cameraman.png')

# convert to snn
pixel_mat = snn_response(pixel, w, h, 10, 0.05)


# imagewrite(ans, w, h)

# initialize population
population1 = init_num(20)
# print len(population1)
# print population

for x in xrange(11):
	a = fitness(population1, pixel_mat, w, h)
	population1, m, max = crossover_num( a )

	if x % 5 == 0:
		ans = convert_binary(pixel_mat, w, h, m)
		imagewrite(ans, w, h)
		imagesave(ans, w, h, 'gen ' + str(x) + ' fit ' + str(m))
		print "==========="

	print max