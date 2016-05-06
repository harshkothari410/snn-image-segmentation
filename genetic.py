import random

def init_num(size):
	population = []
	for x in xrange(size):
		population.append(random.random()*10)
		# population.append( random.randint(1,10)*random.random() )
	return population

def init_bin(size):
	pass

def init_mat(size, w, h):
	population = []
	temp = [ [0 for x in xrange(w)] for x in xrange(h)]
	for z in xrange(size):	
		for x in xrange(h):
			for y in xrange(w):
				temp[x][y] = random.random()*10

		population.append(temp)
	# print len(population[1])
	# print population[1]
	return population

def crossover_mat(fitness_dict, w, h):
	keys = fitness_dict.keys()
	keys.sort(reverse=True)
	print keys[:3]
	children = []
	for x in xrange(0, len(keys)-1, 2):
		parent1 = fitness_dict[keys[x]]
		parent2 = fitness_dict[keys[x+1]]
		child1 = [ [0 for x in xrange(w)] for x in xrange(h)]
		child2 = [ [0 for x in xrange(w)] for x in xrange(h)]

		for x in xrange(h):
			for y in xrange(w):
				child1[x][y] = 0.75 * parent1[x][y] + 0.25 * parent2[x][y]
				child2[x][y] = 0.25 * parent1[x][y] + 0.75 * parent2[x][y]
		children.append(child1)
		children.append(child2)
	return children, fitness_dict[keys[0]], keys[0]

def crossover_num(fitness_dict):
	keys = fitness_dict.keys()
	keys.sort(reverse=True)
	# print len(keys)
	print keys[:3]
	children = []
	for x in xrange(0, len(keys)-1, 2):
		# print x
		parent1 = fitness_dict[keys[x]]
		parent2 = fitness_dict[keys[x+1]]

		child1 = 0.75 * parent1 + 0.25 * parent2
		child2 = 0.25 * parent1 + 0.75 * parent2

		children.append(child1)
		children.append(child2)

	return children, fitness_dict[keys[0]], keys[0]

def fitness_shenon():
	pass

def mutation():
	pass


# size = 20

# print init_num(size)