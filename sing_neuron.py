
# coding: utf-8

# # Nengo Example: A Single Neuron
# This demo shows you how to construct and manipulate a single leaky integrate-and-fire (LIF) neuron. The LIF neuron is a simple, standard neuron model, and here it resides inside a neural population, even though there is only one neuron.

# In[ ]:

import numpy as np
import matplotlib.pyplot as plt

import nengo


# ##Step 1: Create the Neuron

# In[ ]:

from nengo.dists import Uniform

model = nengo.Network(label='A Single Neuron')
with model:
    neuron = nengo.Ensemble(1, dimensions=1, # Represent a scalar
                            intercepts=Uniform(-.5, -.5),  # Set intercept to 0.5
                            max_rates=Uniform(100, 100),  # Set the maximum firing rate of the neuron to 100hz
                            encoders=[[1]])  # Sets the neurons firing rate to increase for positive input


# ## Step 2: Provide Input to the Model
# Create an input node generating a cosine wave.

# In[ ]:

with model:
    cos = nengo.Node(240)#lambda t: np.cos(8 * t))


# ##Step 3: Connect the Network Elements

# In[ ]:

with model:
    # Connect the input signal to the neuron
    nengo.Connection(cos, neuron)


# ##Step 4: Add Probes
# Anything that is probed will collect the data it produces over time, allowing us to analyze and visualize it later.

# In[ ]:

with model:
    cos_probe = nengo.Probe(cos)  # The original input
    spikes = nengo.Probe(neuron.neurons)  # The raw spikes from the neuron
    voltage = nengo.Probe(neuron.neurons, 'voltage')  # Subthreshold soma voltage of the neuron
    filtered = nengo.Probe(neuron, synapse=0.01) # Spikes filtered by a 10ms post-synaptic filter


# ## Step 5: Run the Model

# In[ ]:

sim = nengo.Simulator(model) # Create the simulator
sim.run(1) # Run it for 1 seconds


# ##Step 6: Plot the Results

# In[ ]:

# Plot the decoded output of the ensemble
plt.plot(sim.trange(), sim.data[filtered])
plt.plot(sim.trange(), sim.data[cos_probe])
plt.xlim(0, 1)

# Plot the spiking output of the ensemble
from nengo.utils.matplotlib import rasterplot
plt.figure(figsize=(10, 8))
plt.subplot(221)
rasterplot(sim.trange(), sim.data[spikes])
plt.ylabel("Neuron")
plt.xlim(0, 1)

# Plot the soma voltages of the neurons
plt.subplot(222)
plt.plot(sim.trange(), sim.data[voltage][:,0], 'r')
plt.xlim(0, 1);


# The top graph shows that the input signal in green and the filtered output spikes from the single neuron population in blue. The spikes (that are filtered) from the neuron are shown in the bottom graph on the left. On the right is the subthreshold voltages for the neuron.
import pylab
pylab.show()