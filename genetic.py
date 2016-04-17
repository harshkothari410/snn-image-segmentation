import random

def init_num(size):
	population = []
	for x in xrange(size):
		population.append(random.random()*10)
	return population

def init_bin(size):
	pass

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

		child1 = 0.5 * parent1 + 0.5 * parent2
		child2 = 0.5 * parent1 + 0.5 * parent2

		children.append(child1)
		children.append(child2)

	return children, fitness_dict[keys[0]], keys[0]

def fitness_shenon():
	pass

def mutation():
	pass

# size = 20

# print init_num(size)