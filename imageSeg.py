from genetic import *
from image import *
from snn import *
import math, random
import numpy

def convert_binary(data, w, h, t):
	ans = [[0 for x in xrange(w)] for x in xrange(h)]
	for x in xrange(h):
		for y in xrange(w):
			if data[x][y] > t:
				ans[x][y] = 1
			else:
				ans[x][y] = 0
	return ans


def convert_mat(data, w, h, thresh):
	ans = [[0 for x in xrange(w)] for x in xrange(h)]
	for x in xrange(h):
		for y in xrange(w):
			if data[x][y] > thresh[x][y]:
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

def fitness_mat(population, data, w, h):
	fitness_dict = {}
	for x in population:
		ans = convert_mat(data, w, h, x)
		entropy = shenon_entropy( ans , w, h)
		if entropy in fitness_dict:
			entropy = entropy + random.random()/1000
		fitness_dict[entropy] = x
	return fitness_dict
# read image
pixel, w, h = imageread('cameraman.png')

# convert to snn
pixel_mat = snn_response(pixel, w, h, 10, 0.05)

d=3
def weight(x1,y1,x,y):
	w = 10*math.exp(- (  ( math.pow((x1-x),2)+math.pow((y1-y),2) + math.pow(pixel[x1][y1]-pixel[x][y],2 )/d  ) ) )
	# print w
	return w

second_layer=[[0 for x in xrange(w+2)] for x in xrange(h+2)]
#second_layer=[[pixel[x][y] for x in xrange(w)] for y in xrange(h)]

#print ('before:',len(second_layer))
#print ('before:',len(second_layer[0]))
for x in xrange(1,h-1):
	for y in xrange(1,w-1):
		second_layer[x][y]=	weight(x-1,y-1,x,y)*pixel_mat[x-1][y-1]+weight(x-1,y,x,y)*pixel_mat[x-1][y]+weight(x-1,y+1,x,y)*pixel_mat[x-1][y+1]+weight(x,y-1,x,y)*pixel_mat[x][y-1]+weight(x,y,x,y)*pixel_mat[x][y]+weight(x,y+1,x,y)*pixel_mat[x][y+1]+weight(x+1,y-1,x,y)*pixel_mat[x+1][y-1]+weight(x+1,y,x,y)*pixel_mat[x+1][y]+weight(x+1,y+1,x,y)*pixel_mat[x+1][y+1]

second_layer = numpy.delete(second_layer, (0), axis=0)
second_layer = numpy.delete(second_layer, len(second_layer)-1, axis=0)
second_layer = numpy.delete(second_layer, (0), axis=1)
second_layer = numpy.delete(second_layer, len(second_layer[0])-1, axis=1)

#print ('after:',len(second_layer))
#print ('after:',len(second_layer[0]))
# for x in xrange(h):
# 		for y in xrange(w):
# 			if second_layer[x][y] < numpy.median(second_layer):
# 				second_layer[x][y]=0

# print pixel_mat

# ==================== SNN Matrix ====================
population1 = init_mat(20,w,h)

for x in xrange(11):
	# a = fitness_mat(population1, pixel_mat, w, h)
	a = fitness_mat(population1, second_layer, w, h)
	population1, m, max = crossover_mat( a, w, h )
	print max
	if x % 5 == 0:
		# ans = convert_mat(pixel_mat, w, h, m)
		ans = convert_mat(second_layer, w, h, m)
		imagewrite(ans, w, h)
		imagesave(ans, w, h, 'gen ' + str(x) + ' fit ' )
		print "==========="
# ==================== SNN Int =======================
# imagewrite(ans, w, h)

# initialize population
# population1 = init_num(8)
# print population1
# print len(population1)
# print population

# for x in xrange(11):
# 	a = fitness(population1, pixel_mat, w, h)
# 	population1, m, max = crossover_num( a )

# 	if x % 5 == 0:
# 		ans = convert_binary(pixel_mat, w, h, m)
# 		imagewrite(ans, w, h)
# 		imagesave(ans, w, h, 'gen ' + str(x) + ' fit ' + str(m))
# 		print "==========="

# 	print max