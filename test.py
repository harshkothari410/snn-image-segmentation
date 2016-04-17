import numpy as np
import matplotlib.pyplot as plt

import nengo

from nengo.dists import Uniform

model = nengo.Network(label='A Single Neuron')

with model:
    neuron = nengo.Ensemble(1, dimensions=1, # Represent a scalar
                            intercepts=Uniform(-.5, -.5),  # Set intercept to 0.5
                            max_rates=[20],  # Set the maximum firing rate of the neuron to 100hz
                            encoders=[[1]])  # Sets the neurons firing rate to increase for positive input

with model:
    my_node = nengo.Node(output=680)

with model:
    nengo.Connection(my_node, neuron)

with model:
    cos_probe = nengo.Probe(my_node, synapse=0.01)  # The original input
    spikes = nengo.Probe(neuron.neurons, synapse=0.01)  # The raw spikes from the neuron
    voltage = nengo.Probe(neuron.neurons, 'voltage', synapse=0.01)  # Subthreshold soma voltage of the neuron
    filtered = nengo.Probe(neuron, synapse=0.01) # Spikes filtered by a 10ms post-synaptic filter

sim = nengo.Simulator(model)
sim.run(0.01)
# print sim.data
plt.plot(sim.trange(), sim.data[filtered])
plt.plot(sim.trange(), sim.data[cos_probe])
plt.xlim(0, 0.01)


# Plot the spiking output of the ensemble
from nengo.utils.matplotlib import rasterplot
plt.figure(figsize=(10, 8))
plt.subplot(221)
rasterplot(sim.trange(), sim.data[spikes])
plt.ylabel("Neuron")
plt.xlim(0, 0.01)

import pylab
pylab.show()