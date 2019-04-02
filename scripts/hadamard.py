'''
Script to create the images of the Hadamard transformation on the Bloch sphere
'''

import scipy
import numpy as np
from qutip import *

b = Bloch()
b.vector_color = ['r']
b.point_marker = ['o']
b.point_color = ['b']
b.point_size = [32]
b.view = [-40,30]

hadamard = qutip.qip.hadamard_transform()
H = Qobj(scipy.linalg.logm(hadamard.data.todense()), dims=hadamard.dims) / np.pi * 1.j
psi0 = basis(2,0)

sm = destroy(2)
sx=sigmax();
sy=sigmay()
sz=sigmaz()
expt_ops = [sm.dag() * sm,sx,sy,sz]

tlist = np.linspace(0, -2*np.pi, 21)
expt_list = sesolve(H, psi0, tlist, expt_ops).expect

points_history = []

for i in range(len(expt_list[1])):
    b.clear()
    b.add_vectors([expt_list[1][i], expt_list[2][i], expt_list[3][i]])
    points_history.append([expt_list[1][i-1], expt_list[2][i-1], expt_list[3][i-1]])

    for p in points_history:
        b.add_points(p)

    b.save(dirc='hadamard')

