import math

def snn_response(data, w, h, t, sigma):
	res = [[0 for x in xrange(w)] for x in xrange(h)]
	for x in xrange(h):
		for y in xrange(w):
			p = data[x][y]
			formula = t / (1 + math.exp( sigma  * (128 - p) ))
			res[x][y] = formula
	# math.exp(x)
	return res