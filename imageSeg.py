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

def fitness_weight(population, w, h, t, ind):
	fitness_dict = {}
	for y, x in enumerate(population):
		ans = convert_binary(x, w, h, t)
		entropy = shenon_entropy(ans, w, h)

		if entropy in fitness_dict:
			entropy = entropy + random.random()/1000

		fitness_dict[entropy] = ind[y]
	return fitness_dict

# read image
pixel, w, h = imageread('test1.jpg')

# convert to snn
pixel_mat = snn_response(pixel, w, h, 10, 0.05)

d=3
def weight(x1,y1,x,y):
	w = 10*math.exp(- (  ( math.pow((x1-x),2)+math.pow((y1-y),2) + math.pow(pixel[x1][y1]-pixel[x][y],2 )/d  ) ) )
	return w


def second_layer_locality():
	second_layer = [[0 for x in xrange(w+2)] for x in xrange(h+2)]
	for x in xrange(1,h-1):
		for y in xrange(1,w-1):
			temp = {}
			for i in xrange(x-1, x+1):
				for j in xrange(y-1, y+1):
					temp[pixel_mat[i][j]] = weight(x,y,i,j)

			second_layer[x][y] = response_time(temp)



	second_layer = numpy.delete(second_layer, (0), axis=0)
	second_layer = numpy.delete(second_layer, len(second_layer)-1, axis=0)
	second_layer = numpy.delete(second_layer, (0), axis=1)
	second_layer = numpy.delete(second_layer, len(second_layer[0])-1, axis=1)
	return second_layer

def second_layer(w_mat):
	second_layer = [[0 for x in xrange(w+2)] for x in xrange(h+2)]
	for x in xrange(h):
		for y in xrange(w):
			second_layer[x][y] = response_time({pixel_mat[x][y]:w_mat[x][y]})

	return second_layer

def median_filter(mat, w, h):
	for x in xrange(h):
		for y in xrange(w):
			if mat[x][y] < numpy.median(mat):
				mat[x][y]=0

	return mat
# ==================== SNN Weight ====================
# print "Started "
# population1 = init_three_dim_mat(1, 3,3, 9)
# print population1





# ==================== SNN Matrix ====================
print "Starting GA ..."
population1 = init_mat(8,w,h)
print "Population created ..."
t = 5.0
final = []
for x in xrange(6):
	print "Performing Iteration :", x+1
	sl = []
	for pop in population1:
		temp = second_layer(pop)
		sl.append(temp)

	a = fitness_weight(sl, w, h, t , population1)
	population1, m, max = crossover_mat( a, w, h )
	print "Maximum fitness for this generation :",max
	print "======================================"

	sl = second_layer(m)
	ans = convert_binary(sl, w, h, t)
	final = ans
	imagewrite(ans, w, h)
print len(final)
x = median_filter(final, w, h)
print 'shannon entropy : ',shenon_entropy( x , w, h) 
imagewrite(x, w, h)
	# if x % 5 == 0:
	# 	# ans = convert_mat(pixel_mat, w, h, m)
	# 	imagesave(ans, w, h, 'gen ' + str(x) + ' fit ' )

# for x in xrange(11):
# 	# a = fitness_mat(population1, pixel_mat, w, h)
# 	a = fitness_mat(population1, second_layer, w, h)
# 	population1, m, max = crossover_mat( a, w, h )
# 	print max
# 	if x % 5 == 0:
# 		# ans = convert_mat(pixel_mat, w, h, m)
# 		ans = convert_mat(second_layer, w, h, m)
# 		imagewrite(ans, w, h)
# 		imagesave(ans, w, h, 'gen ' + str(x) + ' fit ' )
# 		print "==========="
# ==================== SNN Int =======================
# imagewrite(ans, w, h)

# initialize population
# population1 = init_num(8)


# for x in xrange(11):
# 	a = fitness(population1, second_layer, w, h)
# 	population1, m, max = crossover_num( a )

# 	if x % 5 == 0:
# 		ans = convert_binary(second_layer, w, h, m)
# 		imagewrite(ans, w, h)
# 		imagesave(ans, w, h, 'gen ' + str(x) + ' fit ' + str(m))
# 		print "==========="

# 	print max