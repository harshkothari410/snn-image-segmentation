import random
from genetic import *
from snn import *
a = [1,5,5,5,5,5,6,6,6,7]
b = [0 for x in xrange(101)]
for x in a:
	b[x*10] += 0.5 
	# b.append(x)
# b = [0,4.5,0,0,0,0,0,0,0]
print b
print response_time(a, b)