import numpy as np
from qnn import qnns
import time


s1 = time.time()
def sigmoid(x, m, b, c):
    return (m / (1 + np.exp(- 4.5 * (x / c)))) - b

def run_nn(inputs, weights, bias, updater=False):
    final1 = []
    weights_changed = False
    bias_changed = False
    if len(weights) < 1:
        weights_changed = True
        weights.append([]);weights.append([])
    if len(bias) < 1:
        bias.append([]); bias.append([])
    while len(weights[0]) < 100:
        weights_changed = True
        weights[0].append(np.random.uniform(-10.0, 10.0, len(inputs)))
    for i in weights[0]:
        if len(i) < len(inputs):
            weights_changed = True
            weights[0][weights[0].index(i)].extend(np.random.uniform(-10.0, 10.0, len(inputs) - len(i)))
    if len(bias[0]) < 100:
        bias[0].extend(np.random.uniform(-10.0, 10.0, 100 - len(bias[0])))
    final1 = np.sum((np.array(inputs) * np.array(weights[0])), axis=1) + np.array(bias[0])
    final2 = np.where(final1, sigmoid(final1, 20, 10, (len(inputs) * 90)), final1)
    return ([float(i) for i in final2], weights_changed, bias_changed, weights, bias) if updater else [float(i) for i in final2]
weights = open('weights.txt', 'r').read().split('\n')
if weights != ['']:
    weights = [i.split(',') for i in weights]
    for i in range(0, len(weights)):
        for b in range(0, len(weights[i])):
            weights[i][b] = [float(item) for item in weights[i][b].split('/')]
else:
    weights = []
first_output, update_weights, update_bias, weights, bias = run_nn([9, 5, 2, 3, 1], weights, [], True)
weights = [[list([float(g) for g in i]) for i in b] for b in weights]
if update_weights:
    file = open('weights.txt', 'w')
    for i in weights:
        adder = []
        for b in i:
            b = [str(n) for n in b]
            adder.append('/'.join(b) if '/'.join(b)[0] != '/' else ('/'.join(b))[1:])
        file.write(','.join(adder))
manage = qnns()
branches = manage.next_branch([2, 1, 0, -5, 2, 3, [2, 6, 1, [3, 1]]])
#[[outputs]]
quantum_inputs = [[first_output]]
quantum_outputs = []
#[neuron [quantum states [state 1], [state 2]]] the output
#[parent neurons[neurons connected to parent[#quantum states for the neuron[#2d quantum state]]]]
"""
for parent_neuron in range(0, len(branches)):
    for neuron in range(0, len(branches[parent_neuron])):
        quantum_outputs.append([]) #[[]]
        for quantum_state in range(0, len(branches[parent_neuron][neuron])):
            for super_state in range(0, len(branches[parent_neuron][neuron][quantum_state])):
                for real_qni in quantum_inputs[parent_neuron]:
                    quantum_outputs[neuron].append(run_nn(real_qni[:5] + [super_state] + real_qni[6:], weights, []))
print(time.time() - s1); s1 = time.time()
quantum_outputs = []
"""
s1 = time.time()
[[([quantum_outputs.append([]), [[[quantum_outputs[neuron].append(run_nn(real_qni[:5] + [super_state] + real_qni[6:], weights, [])) for real_qni in quantum_inputs[parent_neuron]] for super_state in range(0, len(branches[parent_neuron][neuron][quantum_state]))] for quantum_state in range(0, len(branches[parent_neuron][neuron]))]]) for neuron in range(0, len(branches[parent_neuron]))] for parent_neuron in range(0, len(branches))]

print('end in ' + str(time.time() - s1))
nn = []

