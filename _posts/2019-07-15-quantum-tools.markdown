---
layout: post
title:  "Comparison of Quantum Development Tools WORK IN PROGRESS"
description: "Outline of some of the popular quantum development tools and when you should be using them."
date:   2019-07-15
---

WORK IN PROGRESS

There is an increasing amount of quantum development tools but what is the difference and in what situation should each be used? I'll only be covering a few of the well known ones which are a very small portion (mostly the ones I get asked about most frequently.) Each of these projects are open source.

## Full Stack Libraries

### [Q# (Microsoft)](https://github.com/microsoft/Quantum)
.NET language which can be used with other languages in the ecosystem easily. Also has Python interoperability with a Jupyter notebook kernal for a Pythonic programming experience. The Microsoft Quantum Development Kit has only recently become open source. Q# focuses on algorithmic thinking than low level implementation and as such is made to be easy to write applications from high order quantum algorithms and protocols. It was developed on fault tolerant regimes of the future. Designed to easily write large algorithms with many layers of abstraction easily with the help of the 

Personal experience: easy to get set up with and use for implementing quantum algorithms. Currently has a smaller amount of resources (tutorials, videos etc. ) than Qiskit. I believe it is growing. 

Does it run on a real QC?


Blog post on by Q# was built (https://devblogs.microsoft.com/qsharp/why-do-we-need-q/)

Focused on the far future fault tolerant regime. Scope mechanisms, RAII for qubits, automatic derivation of variants of operations, and other stuff useful for writing large algorithms with many layers of abstraction.


### [Qiskit (IBM)](https://github.com/qiskit)
Has a large number of tutorials 
Has online circuit
Access to simulators, 2qubit computers and 5 qubits computers -multiple available. 

Personal experience: extremely easy to get set up and use with a great community.

### [Cirq (Google)](https://github.com/quantumlib/Cirq)
A Python framework for creating and manipulating circuits
Logic and syntax of  Cirq is similar to Qiskit 

Designed to get the most out of NISQ architectures by allowing fine tune control on gate behaviour and timing gates with constraints of the hardware.
Still in alpha and warn that they make breaking changes. Used by the Google AI Quantum team to create circuits that run on Google's Bristlecone quantum processor (not available to the public) as well as locally on a simulator.

They also have [OpenFermion-Cirq](https://github.com/quantumlib/OpenFermion-Cirq) which is a library for obtaining and manipulating representations of fermionic systems for simluation on quantum computers.

Q#, Qiskit and Cirq are all very similar in what they do and user experience with the code

#### [Aqua](https://github.com/Qiskit/qiskit-aqua)
A library of cross domain quantum algorithms that works with Qiskit and is build for near term quantum computing. Some included applications are chemistry, artificial intelligence, optimisation and finance. This library is easy to use and has available the foundations that allow you to build more algorithms such as quantum Fourier transforms etc. Has the potential to be built up for lots of different applications.

### [Strawberry Fields (Xanadu)](https://github.com/XanaduAI/strawberryfields)
Python library for designing, simulating, and optimizing continuous variable quantum optical circuits. Currently can only be run on quantum simulators however no presently available quantum computer to run it on. The stack is ideal for simulating quantum photonics and continuous variable quantum computing with Tensorflow support. Heavy focus on machine learning.

Greater barrier to entry (?) as the code is less intuitive than qiskit and requires more background knowledge due to the greater level of control over the simulation type, type of output, cutoff dimensions etc. Different to the previously mentioned libraries

### Forest (Rigetti)? Grove?

#### [pyQuil (Rigetti)](https://github.com/rigetti/pyquil)
Able to easily use their cloud as you just SSH in to run your scripts.


### [Ocean (D-Wave)](https://github.com/dwavesystems/dwave-ocean-sdk)
Python development kit to program circuits on DWave 2000 qubit quatnum annealer. Very basic baseline - enough to be able to crate circuits and write programs with nothing too fancy. Tutorials and access is available through their [Leap](https://www.dwavesys.com/take-leap) cloud service.

## Algorithms
### [Pennylane Xanadu](https://github.com/XanaduAI/pennylane)
Dedicated machine learning software for quantum computers. Plugins that allow for your circuits to be run on devices not made by Xanadu - it is hardware agnostic - and compatible with PyTorch, Tensorflow etc. This is the differentiable between Aqua and Pennylane. External integration possible. Very comprehensive. Tutorials exist however don't go into detail about the underlying theory behind the quantum machine learning concepts. Hybrid quantum and classical computations.


Simulators

### Qutip
Python framework for 
Below the circuit level. Modelling physical systems and hardware.


Assembly

### OpenQASM



Summary
Most of these are based on Python and are very similar. The main differentiable between choosing which framework you wish to use would be what hardware do I want to run my program on. IMO the best one for a beginner would be Qiskit. 

For a more in depth list of open source development tools, check out the QOSF's [Open Source Quantum Software Projects List](https://github.com/qosf/os_quantum_software) as well as their evaluation on the state of [open source quantum projects](https://qosf.org/evaluation). For a list of general quantum computing resources check out my [awesome list](https://github.com/desireevl/awesome-quantum-computing).


<!-- LOOK AT ACTUAL CODE
MAYBE INCLUDE SOME EXAMPLES TO COMPARE EACH OF THEM -->

<!-- https://quantumcomputing.stackexchange.com/questions/1474/what-programming-languages-are-available-for-quantum-computers -->

<!-- https://en.wikipedia.org/wiki/Quantum_programming -->

<!-- https://medium.com/qiskit/qiskit-and-its-fundamental-elements-bcd7ead80492 -->

References
https://www.reddit.com/r/programming/comments/av018k/programming_a_quantum_computer_with_cirq/