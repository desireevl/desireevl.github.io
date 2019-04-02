'''
Script to create the images of the unitary transformations on the Bloch Sphere

To generate mp4 using ffmpeg:
ffmpeg -r 5 -i bloch_%01d.png -b 2048k -r 5 animation.mp4

To generate gif using GIMP:
- Open as Layers (each image)
- Image -> Mode -> switch from RGB to Indexed, max color palette 127
- If layers aren't in correct order Layer -> Stack -> Reverse Order
- Export as GIF
'''

import numpy as np
from qutip import *
from scipy import *

transform = 'Y'

b = Bloch()
b.vector_color = ['r']
b.point_marker = ['o']
b.point_color = ['b']
b.point_size = [32]
b.view = [-40,30]


if transform == 'X':
    xz = np.zeros(20)
    yz = [np.sin(th) for th in np.linspace(0, -np.pi, 20)]
    zz = [np.cos(th) for th in np.linspace(0, -np.pi, 20)]

if transform == 'Z_one':
    xz = [np.cos(th) for th in np.linspace(0, np.pi, 20)]
    yz = [np.sin(th) for th in np.linspace(0, np.pi, 20)]
    zz = np.zeros(20)

if transform == 'Y':
    xz = [np.cos(th) for th in np.linspace(0, -np.pi, 20)]
    zz = [np.sin(th) for th in np.linspace(0, -np.pi, 20)]
    yz = np.zeros(20)

points_history = []

for i in range(len(xz)):
    b.clear()
    b.add_vectors([xz[i], yz[i], zz[i]])
    points_history.append([xz[i-1], yz[i-1], zz[i-1]])

    for p in points_history:
        b.add_points(p)

    b.save(dirc=transform)