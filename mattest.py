def crossover_splice_mat(fitness_dict, w, h):
	keys = fitness_dict.keys()
	keys.sort(reverse=True)
	print keys[:3]
	children = []
	for x in xrange(0, len(keys)-1, 2):
		parent1 = fitness_dict[keys[x]]
		parent2 = fitness_dict[keys[x+1]]
		

		child1 = parent1[:2] + parent2[2:]
		child2 = parent2[:2] + parent1[2:]
		# for x in xrange(h/2):
		# 	for y in xrange(w/2):

		# 		child1[x][y] = parent1[x][y] 
		# 		child2[-x-1][-y-1] = parent1[-x-1][-y-1]
		# 		child1[h-x-1][w-y-1]=parent2[h/2+x][w-y-1]

		# 		child1[-x-1][-y-1] = parent2[-x-1][-y-1]
		# 		child2[x][y] = parent2[x][y]
		# 		child2[h-x-1][w-y-1]=parent1[h-x-1][w-y-1]

		children.append(child1)
		children.append(child2)
	return children, fitness_dict[keys[0]], keys[0]

def print_mat(m):
	for x in xrange(4):
		print m[x]

a = [[1,2,3,1],
	[4,5,6,4],
	[5,6,7,8],
	[4,7,8,0]]
b = [[65,76,87,98],
	[43,65,98,12],
	[10,20,30,40],
	[54,67,98,109]]
d = {
	1:a,
	2:b
}
print_mat(a)
print_mat(b)
x,y,z = crossover_splice_mat(d, 4,4)
for m in x:
	print '=='
	print_mat(m)