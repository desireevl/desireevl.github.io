---
layout: post
title:  "Introduction to Quantum Unitary Operators"
description: "Visualisations and mathematical representations of the Pauli and Hadamard gates."
date:   2019-04-03
categories: archive
---

Simply explained, quantum computing consists of manipulating qubits and then measuring the outcome after applying gate transformations to them. Any manipulation of a qubit must be performed by a unitary operator in order for it to be implemented on a quantum computer. 

### What is a unitary operator?
A unitary operator can be represented as a matrix, in which its conjugate transpose is equal to its inverse, also written in the following form where I is the identity matrix:
<p align="center">
<a><img src="/images/intro_unitary/unitary.png" title="Unitary" width="80.4" height="31.2" /></a> 
</p>

The quantum gates must be unitary as these kinds of operations are reversible and preserve normalisation of the quantum states, allowing the states to remain on the surface of the Bloch sphere after the transformation (which we'll see shortly).

Here, I will introduce the basic unitary operators used in quantum computing, outlining the mathematical operations, visualisation of their effect on the Bloch sphere as well as how they can be implemented on a quantum computer. 

### Pauli X
The simplest unitary gate is the Pauli X gate, which performs a bit flip operation, similar to the classical NOT gate. Its matrix representation is as follows:

<p align="center">
<a><img src="/images/intro_unitary/X.png" title="X Matrix" width="108" height="57.3" /></a> 
</p>

When the X transform is applied to the standard basis, the results are simply the inverse of what was input.

<p align="center">
<a><img src="/images/intro_unitary/X0.png" title="X0 Matrix" width="276.3" height="57.3" /></a> 
</p>

<p align="center">
<a><img src="/images/intro_unitary/X1.png" title="X1 Matrix" width="276.3" height="57.3" /></a> 
</p>

This gate performs a rotation about the x axis by &#960; radians, which is seen on the following Bloch sphere when applied to 0 basis state.

<p align="center">
<a><img src="/images/intro_unitary/X.gif" title="X Bloch Sphere" width="400" height="400" /></a> 
</p>

The circuit to implement the X transform consists of only the gate itself and a measurement gate. You can click on the circuit to go to the IBM Q composer where you can run the circuit on a quantum computer/simluator and view the results.

<p align="center">
<a href="https://quantumexperience.ng.bluemix.net/share/code/5c3202c3a5a3280056c8a791"><img src="/images/intro_unitary/X_circuit.png" title="X gate circuit" width="500" height="150" /></a> 
</p>


### Pauli Z

In contrast to the X gate, the Z gate is a phase flip operator, with no corresponding classical gate. It is represented in matrix form as:

<p align="center">
<a><img src="/images/intro_unitary/Z.png" title="Z Matrix" width="108" height="57.3" /></a> 
</p>

Applying the Z gate to &#124;0&#9002; and &#124;1&#9002;, we see that the gate has no effect on the &#124;0&#9002; state and simply adds a negative sign in front of the &#124;1&#9002; state:

<p align="center">
<a><img src="/images/intro_unitary/Z0.png" title="Z0 Matrix" width="286.5" height="57.3" /></a> 
</p>

<p align="center">
<a><img src="/images/intro_unitary/Z1.png" title="Z1 Matrix" width="326.7" height="57.3" /></a> 
</p>

The effects of the Z gate can be seen when applied to the &#124;+&#9002; state in the following visualisation, where a rotation of  &#960; about the z axis occurs. After the transformation, the final state is &#124;-&#9002;, and when measured, still has an equal probability of being 0 or 1. The Z gate performs a rotation of &#960; radians around the z axis. 

<p align="center">
<a><img src="/images/intro_unitary/Z_one.gif" title="Z Bloch Sphere" width="400" height="400" /></a> 
</p>

The first circuit below executes the Z gate on a &#124;0&#9002; state, and the second circuit on the superposition &#124;+&#9002; state:
<p align="center">
<a href="https://quantumexperience.ng.bluemix.net/share/code/5c328b1e997f7c00550401bd"><img src="/images/intro_unitary/Z_circ.png" title="Z gate circuit" width="500" height="150" /></a> 
</p>

<p align="center">
<a href="https://quantumexperience.ng.bluemix.net/share/code/5c328c1b9d99af00561fe1b9"><img src="/images/intro_unitary/Z_circ2.png" title="Z gate circuit" width="500" height="150" /></a> 
</p>

### Pauli Y
The Y gate can be written as the following matrix however can also be thought of as an execution of the X and Z gates consecutively. 

<p align="center">
<a><img src="/images/intro_unitary/Y.png" title="Y Matrix" width="173.7" height="57.3" /></a> 
</p>

Below, we apply the matrix representation as well as the X and Z combination to the &#124;0&#9002; and &#124;1&#9002; states to demonstrate that they yield the same result. 

<p align="center">
<a><img src="/images/intro_unitary/Y0.png" title="Y Matrix" width="294.9" height="57.3" /></a> 
</p>

<p align="center">
<a><img src="/images/intro_unitary/Y0_nomat.png" title="Y Matrix" width="253.5" height="30" /></a> 
</p>

<p align="center">
<a><img src="/images/intro_unitary/Y1.png" title="Y Matrix" width="335.1" height="57.3" /></a> 
</p>

<p align="center">
<a><img src="/images/intro_unitary/Y1_nomat.png" title="Y Matrix" width="288.3" height="30" /></a> 
</p>

As implied in these calculations, the difference between the X and Y operations is simply just the phase (an additional Z transformation). The Y gate performs a &#960; radian rotation about the Y axis.

<p align="center">
<a><img src="/images/intro_unitary/Y.gif" title="Y Bloch Sphere" width="400" height="400" /></a> 
</p>

The first circuit below is simply the Y gate operation and the second corresponds to the rotation witnessed in the animation above, where there is a 50/50 split of 0 and 1 recordings.

<p align="center">
<a href="https://quantumexperience.ng.bluemix.net/qx/display/code?id=5c7419f4f1c054005789102f&idExecution=5c7419f54d992d00518d9774"><img src="/images/intro_unitary/Y_circ.png" title="Y gate circuit" width="500" height="150" /></a> 
</p>

<p align="center">
<a href="https://quantumexperience.ng.bluemix.net/qx/display/code?id=5c32c32a7f17bc005eeb44f7&idExecution=5c32c32a7f17bc005eeb44f8"><img src="/images/intro_unitary/Y_circ2.png" title="Y gate circuit" width="500" height="150" /></a> 
</p>


### Hadamard
The Hadamard gate is extremely important as it is used to create states of superposition and is represented by the following matrix:

<p align="center">
<a><img src="/images/intro_unitary/H.png" title="H Matrix" width="160.2" height="66.6" /></a> 
</p>

Performing a Hadamard transformation on a qubit creates a state of equal superposition between the two basis states, meaning that only when you choose to measure the qubit will its state be determined. This can be seen in the results from the circuit below: half of the shots will measure 0 and the other half as 1. 

<p align="center">
<a href="https://quantumexperience.ng.bluemix.net/share/code/5c741f68f55271005b90d36f"><img src="/images/intro_unitary/H_circ.png" title="H gate circuit" width="500" height="165" /></a> 
</p>

Applying the Hadamard operation on the &#124;0&#9002; and &#124;1&#9002; states result in the formation of a new superposition basis: &#124;+&#9002; and &#124;-&#9002;.

<p align="center">
<a><img src="/images/intro_unitary/H0.png" title="H Matrix" width="366.6" height="66.6" /></a> 
</p>

<p align="center">
<a><img src="/images/intro_unitary/H1.png" title="H Matrix" width="376.8" height="66.6" /></a> 
</p>

The following animation illustrates two consecutive Hadamard transformations which equates to two rotations about the <sup>(x+z)</sup>&frasl;<sub>&#8730;2</sub> axis by &#960; radians. After the first, the position of the vector lies along the x axis at &#124;+&#9002; and after the second transformation, the vector is back to where it started, which is what we expect. 

<p align="center">
<a><img src="/images/intro_unitary/hadamard.gif" title="Hadamard Bloch Sphere" width="400" height="400" /></a> 
</p>


This introduction has only scratched the surface of unitary operations used in quantum computing. There exists a plethora of gates that are far more complex or operate on multiple qubits at once, and altogether these allow for the development of many incredibly useful algorithms.

<br>For more learning and developing resources for quantum computing see the [awesome list](
http://github.com/desireevl/awesome-quantum-computing).

Animations were made using <a href="http://qutip.org/">Qutip</a>, circuits using <a href="https://quantumexperience.ng.bluemix.net/qx/editor">IBM Q Experience</a> and equations using <a href="https://www.mathcha.io/editor">Mathcha</a>.
