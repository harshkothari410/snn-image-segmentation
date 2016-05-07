import math
import random
import numpy
from numpy import *
# dt = 0.001       # simulation time step  
# t_rc = 0.02      # membrane RC time constant
# t_ref = 0.002    # refractory period
# t_pstc = 0.1     # post-synaptic time constant
# N_A = 50         # number of neurons in first population
# N_B = 40         # number of neurons in second population
# N_samples = 100  # number of sample points to use when finding decoders
# rate_A = 25, 75  # range of maximum firing rates for population A
# rate_B = 50, 100 # range of maximum firing rates for population B

# def generate_gain_and_bias(count, intercept_low, intercept_high, rate_low, rate_high):
# 	import random
# 	gain = []
# 	bias = []
# 	for i in range(count):
# 		# desired intercept (x value for which the neuron starts firing
# 		intercept = random.uniform(intercept_low, intercept_high)
# 		# desired maximum rate (firing rate when x is maximum)
# 		rate = random.uniform(rate_low, rate_high)

# 		# this algorithm is specific to LIF neurons, but should
# 		#  generate gain and bias values to produce the desired
# 		#  intercept and rate
# 		z = 1.0 / (1-math.exp((t_ref-(1.0/rate))/t_rc))
# 		g = (1 - z)/(intercept - 1.0)
# 		b = 1 - g*intercept
# 		gain.append(g)
# 		bias.append(b)
# 	return gain,bias

# def run_neurons(input,v,ref, spike_train):
# 	print spike_train
# 	spikes=[]
# 	for i in range(len(v)):
# 		# print input[i], v[i], spike_train[i]
# 		if i == 0:
# 			dV = (spike_train[i]/1000.0) * (input[i]-v[i]) / t_rc    # the LIF voltage change equation	
# 		else:
# 			print (spike_train[i]-spike_train[i-1])/1000.0 
# 			dV = ((spike_train[i]-spike_train[i-1])/1000.0 ) * (input[i]-v[i]) / t_rc    # the LIF voltage change equation
# 		# print "dv : ", dV
# 		v[i] += dV  

# 		print "voltage : ", v[i]                 
# 		if v[i]<0: v[i]=0                   # don't allow voltage to go below 0
        
# 		if ref[i]>0:                        # if we are in our refractory period
# 			v[i]=0                          #   keep voltage at zero and
# 			ref[i]-=dt                      #   decrease the refractory period

# 		if v[i]>1:
# 			return i 
            
# 			v[i] = 0
# 			ref[i] = t_ref
# 		else:
# 			spikes.append(False)
# 	return -1

def snn_response(data, w, h, t, sigma):
	import random
	res = [[0 for x in xrange(w)] for x in xrange(h)]
	for x in xrange(h):
		for y in xrange(w):
			p = data[x][y]
			formula = t / (1 + math.exp( sigma  * (128 - p) ))
			res[x][y] = formula
	# math.exp(x)
	return res


# formula V = Vo * e ^ (-t/T)
def weight(x1,y1,x,y):
	w = 10*math.exp(- (  ( math.pow((x1-x),2)+math.pow((y1-y),2) + math.pow(pixel[x1][y1]-pixel[x][y],2 )/d  ) ) )
	# print w
	return w

def formula(v, t, T):
	return v * math.exp(-t/T) 


# ============================ LIF Implementation ===============================
def spike(input):
	pre_v = 0
	for x in xrange(100):

		v = input[x] + formula(pre_v, x / 10.0, 20)
		# print 'v : ', v 
		if v >= 1:
			# print "spike : ", x/10.0, v 
			return x
		pre_v = v
	return 120

def response_time(pixel_data_dict):
	b = [0 for x in xrange(101)]
	# for x in a:
	# 	b[x*10] += 0.5 
	# float("{0:.2f}".format(
	for x in sorted(pixel_data_dict):
		val = int(round(x*10))
		# weight = float("{0:.2f}".format(pixel_data_dict[x]))
		weight = pixel_data_dict[x]
		b[val] = b[val] + (0.5*weight)


	index = spike(b)
	return (index/10.0)

# print second_layer
#print ('after:',len(second_layer))
#print ('after:',len(second_layer[0]))
# for x in xrange(h):
# 		for y in xrange(w):
# 			if second_layer[x][y] < numpy.median(second_layer):
# 				second_layer[x][y]=0

# print pixel_mat


