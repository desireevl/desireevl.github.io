---
layout: post
title:  "Introduction to Quantum Unitary Operations WIP"
date:   2019-01-06
categories: archive
---


### What is a unitary matrix?
A matrix is unitary if its conjugate transpose is equal to its inverse, also written in the following form where I is the identity matrix:
<p align="center">
<a><img src="/images/intro_unitary/unitary.png" title="Unitary" width="80.4" height="31.2" /></a> 
</p>

<!-- what are the gates how do they link to these matrix -->

Here I will introduce the basic unitary operators used in quantum computing, outlining the mathematical operations, visualisation of their effect on the Bloch sphere as well as how they can be implemented on a quantum computer.

### Pauli X 
The X gate is a bit flip operator, similar to the classical NOT gate. Its matrix representation is as follows:

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

This gate performs a rotation about the x axis by &#960; which is seen on the following Bloch sphere when applied to 0 basis state.

<p align="center">
<a><img src="/images/intro_unitary/X.gif" title="X Bloch Sphere" width="400" height="400" /></a> 
</p>

The circuit to implement the X transform consists of only the gate itself and a measurement gate. The hyperlink in the image will take you to the IBM Q composer where you can run the circuit on a quantum computer/simluator and view the results.

<p align="center">
<a href="https://quantumexperience.ng.bluemix.net/share/code/5c3202c3a5a3280056c8a791"><img src="/images/intro_unitary/X_circuit.png" title="X gate circuit" width="500" height="150" /></a> 
</p>



### Pauli Z

In contrast to the X gate, the Z gate is a phase flip operator, with no corresponding classical gate.

<p align="center">
<a><img src="/images/intro_unitary/Z.png" title="Z Matrix" width="108" height="57.3" /></a> 
</p>

<p align="center">
<a><img src="/images/intro_unitary/Z0.png" title="Z0 Matrix" width="286.5" height="57.3" /></a> 
</p>

<p align="center">
<a><img src="/images/intro_unitary/Z1.png" title="Z1 Matrix" width="326.7" height="57.3" /></a> 
</p>

<p align="center">
<a><img src="/images/intro_unitary/Z_one.gif" title="Z Bloch Sphere" width="400" height="400" /></a> 
</p>

<p align="center">
<a href="https://quantumexperience.ng.bluemix.net/share/code/5c328b1e997f7c00550401bd"><img src="/images/intro_unitary/Z_circ.png" title="Z gate circuit" width="500" height="150" /></a> 
</p>

<p align="center">
<a href="https://quantumexperience.ng.bluemix.net/share/code/5c328c1b9d99af00561fe1b9"><img src="/images/intro_unitary/Z_circ2.png" title="Z gate circuit" width="500" height="150" /></a> 
</p>

### Pauli Y

The X and Z gate can be applied to a state consecutively

<p align="center">
<a><img src="/images/intro_unitary/Y.png" title="Y Matrix" width="173.7" height="57.3" /></a> 
</p>

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

<p align="center">
<a><img src="/images/intro_unitary/Y.gif" title="Y Bloch Sphere" width="400" height="400" /></a> 
</p>


### Hadamard

Animations were made using <a href="http://qutip.org/">Qutip</a>, circuits using <a href="https://quantumexperience.ng.bluemix.net/qx/editor">IBM Q Experience</a> and equations using <a href="https://www.mathcha.io/editor">Mathcha</a>.
