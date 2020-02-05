---
layout: slide
title: Introduction to Quantum Computing
description: University of Queensland Computing Society Talk
theme: white
custom_css: intro-to-qc
transition: slide
date: 2019-09-26
---

<!-- Title and About me slides -->
<section>
  <section>
    <h1>Introduction to Quantum Computing</h1>
    <br>
    <p>
      <small>Desiree Vogt-Lee</small>
    </p>
  </section>

  <section>
    <h2>About Me</h2>
    <br>
    <div class="left">
      <ul>
        <li class="fragment" data-autoslide="700">Physics student</li>
        <li class="fragment" data-autoslide="700">Data scientist at NTI</li>
        <li class="fragment">Recently returned from a quantum computing workshop and hackathon in
          Zurich</li>
      </ul>
    </div>
    <div class="right">
      <a href="http://www.desireevl.com/posts/qcamp-europe"><img width="450" height="300" src="/images/qcamp-europe/hack.jpg"></a>
    </div>
  </section>
</section>

<!-- Classical and quantum bits intro (exponential increase) -->
<section>
  <section>
    <div class="left">
      <h3 align="center">Classical Bits</h3>
      <br>
      <br>
      <a><img class="plain" width="80%" height="80%" src="/images/intro-qc/classical.png"></a>
    </div>
    <div class="right">
      <h3>Quantum Bits (qubits)</h3>
      <br>
      <img class="plain" align="center" width="350" height="350" src="https://upload.wikimedia.org/wikipedia/commons/6/6b/Bloch_sphere.svg">
      <p>$| \psi \rangle = \alpha | 0 \rangle + \beta | 1 \rangle$</p>
      <p class="cite">
          From <a href="https://commons.wikimedia.org/wiki/File:Bloch_sphere.svg">Wikicommons</a> (2009).
      </p>
    </div>
  </section>
  <section>
    <p>Classical Computation: checking all possibilities in rapid succession</p>
    <p>Quantum Computation: checking all possibilities in parallel</p>
    <br>
    <table style="background-color:rgba(241, 192, 192, 0.25);">
      <thead>
        <tr>
        <th>Qubits</th>
        <th>Possibilities</th>
        <th>Power $(2^N)$</th>
        </tr>
      </thead>
      <tbody>
        <tr>
        <td>1</td>
        <td>0, 1</td>
        <td>2</td>
        </tr>
        <tr>
        <td>2</td>
        <td>00, 10, 01, 11</td>
        <td>4</td>
        </tr>
        <tr>
        <td>3</td>
        <td>000, 001, 011, 110, 010, 100, 101, 111</td>
        <td>8</td>
        </tr>
      </tbody>
    </table>
    <br>
    <p>For each qubit added, the compute power doubles.</p>
  </section>
      <section>
            <h2>Quantum Computers</h2>
            <p align="left">Computers that use qubits instead of bits.</p>
            <p align="left">Quantum properties: superposition, entanglement, interference</p>            
            <p align="left">Different types of QCs: annealers, adiabatic, universal, Noisy Intermediate Scale Quantum (NISQ)</p>
            <p align="left">Usually when we refer to QCs, we mean fault tolerant devices, but currently we only have NISQ devices.</p>
    </section>
</section>

<!-- Unitary gates -->
<section>
  <section>
      <h2>Unitary Operators</h2>
      <p align="left">Operations are performed on universal QCs by applying unitary gates.</p>
      <p align="left">Gates must be unitary in order to be reversible and preserve the normalisation of the quantum state.</p>
      <p>$UU^{\dagger} = I$</p>
      <img class="plain" align="center" width="25%" height="25%" src="https://upload.wikimedia.org/wikipedia/commons/6/6b/Bloch_sphere.svg">
      <p class="cite">
        From <a href="https://commons.wikimedia.org/wiki/File:Bloch_sphere.svg">Wikicommons</a> (2009).
      </p>
    </section>
    <section>
    <h2>Gates - Pauli X</h2>
    <br>
    <div class="left">
      <a href="http://www.desireevl.com"><img class="plain" width="200" height="54.684" src="/images/intro-qc/x_gate.png"></a>
      <br>
      <p>Equivalent to a classical NOT gate</p>
      <p>Performs a bit flip operation</p>
      <br>
      <p>$X=\begin{bmatrix} 0 & 1\\ 1 & 0 \end{bmatrix}$</p>
    </div>
    <div class="fragment right" data-autoslide="900">
      <br>
      <a href="http://www.desireevl.com"><img class="plain" width="300" height="300" src="/images/intro_unitary/X.gif"></a>
    </div>
    <div class="fragment" data-autoslide="0"></div>
  </section>
  <section>
      <h2>Gates - Hadamard</h2>
      <div class="left">
        <a href="http://www.desireevl.com"><img class="plain" width="200" height="54.684" src="/images/intro-qc/h_gate.png"></a>
        <br>
        <p>No equivalent classical gate</p>
        <p>Puts qubit into superposition state between 0 and 1</p>
        <br>
        <p>$H=\frac{1}{\sqrt{2}}\begin{bmatrix} 1 & 1\\ 1 & -1 \end{bmatrix}$</p>
      </div>
      <div class="fragment right" data-autoslide="900">
        <br>
        <a href="http://www.desireevl.com"><img class="plain" width="300" height="300" src="/images/intro_unitary/hadamard.gif"></a>
      </div>
      <div class="fragment" data-autoslide="0"></div>
  </section>
      <section>
        <h2>Gates - Controlled NOT (CNOT)</h2>
        <div class="left">
            <img class="plain" style="padding-left: 100px;" width="40%" height="40%" src="https://upload.wikimedia.org/wikipedia/commons/4/4e/CNOT_gate.svg">
            <br>
            <p>Performs a bit flip operation based on the value of the first qubit</p>
            <p style="font-size: 80%">$CNOT=\begin{bmatrix} 1 &0  &0  &0 \\ 0 &1  &0  &0 \\ 0 &0  &0  &1 \\ 0 &0  &1  &0 \end{bmatrix}$</p>
        </div>
        <div class="fragment right" data-autoslide="900">
            <br>
            <table style="background-color:rgba(241, 192, 192, 0.25);">
                <thead>
                    <tr>
                    <th>Before</th>
                    <th>After</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                    <td>00</td>
                    <td>00</td>
                    </tr>
                    <tr>
                    <td>01</td>
                    <td>01</td>
                    </tr>
                    <tr>
                    <td>10</td>
                    <td>11</td>
                    </tr>
                    <tr>
                    <td>11</td>
                    <td>10</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="fragment" data-autoslide="0"></div>
  </section>
</section>

<!-- Coding demo -->
<section>
        <h2>Example Coding on a Quantum Computer</h2>
        <a href="http://localhost:8888/notebooks/Bernstein-Vazirani.ipynb" target="_blank"><img class="plain" width="45%" height="45%" src="/images/intro-qc/code.png"></a>
</section>

<!-- Quantum algorithms -->
<section>
        <section>
            <h2>Quantum Algorithms - Shor's Algorithm</h2>
            <p>Factoring algorithm that runs in polynomial time</p>
            <img class="plain" align="center" width="60%" height="60%" src="https://upload.wikimedia.org/wikipedia/commons/6/6b/Shor%27s_algorithm.svg">
            <p class="cite">
              From <a href="https://upload.wikimedia.org/wikipedia/commons/6/6b/Shor%27s_algorithm.svg">Wikicommons</a> (2014).
            </p>
            <p>Could be used to break public key cryptography (RSA)</p>
        </section>
        <section>
          <h2>Quantum Algorithms - Grover's Algorithm</h2>
          <p>Searching algorithm that runs in $O(\sqrt{N})$ evaluations</p>
          <img class="plain" align="center" width="60%" height="60%" src="https://upload.wikimedia.org/wikipedia/commons/a/ae/Grovers_algorithm.svg">
          <p class="cite">
            From <a href="https://upload.wikimedia.org/wikipedia/commons/a/ae/Grovers_algorithm.svg">Wikicommons</a> (2009).
          </p>
        </section>
</section>

<!-- Applications -->
<section>
    <h2>Applications of Quantum Computing</h2>
    <div class="left">
        <img class="plain" style="padding-left: 100px;" width="10%" height="10%" src="/images/intro-qc/atom.png">
        <br>
        <p style="font-size: 90%; padding-left: 20px;"><b>Chemical Simulation</b></p>
        <ul style="line-height:10%">
            <li style="font-size: 75%">Molecular design</li>
            <li style="font-size: 75%">Drug discovery</li>
            <li style="font-size: 75%">Protein structure prediction</li>
        </ul>
        <br>
        <img class="plain" style="padding-left: 100px;" width="10%" height="10%" src="/images/intro-qc/lock.png">
        <br>
        <p style="font-size: 90%; padding-left: 50px;"><b>Cryptography</b></p>
        <ul style="line-height:10%">
            <li style="font-size: 75%">Breaking RSA</li>
            <li style="font-size: 75%">Breaking Diffie-Hellman</li>
        </ul>
    </div>
    <div class="right">
        <img class="plain" style="padding-right: 150px;" width="12%" height="12%" src="/images/intro-qc/chip.png">
        <br>
        <p style="font-size: 90%; padding-right: 50px;"><b>Artificial Intelligence</b></p>
        <ul style="line-height:10%; padding-right: 100px;">
            <li style="font-size: 75%">Prediction</li>
            <li style="font-size: 75%">Classification</li>
        </ul>
        <br>
        <img class="plain" style="padding-right: 150px;" width="9%" height="9%" src="/images/intro-qc/line-chart.png">
        <br>
        <p style="font-size: 90%; padding-right: 50px;"><b>Scenario Simulation</b></p>
        <ul style="line-height:10%">
            <li style="font-size: 75%">Risk Analysis</li>
            <li style="font-size: 75%">Disruption Management</li>
        </ul>
    </div>
</section>

<!-- Quantum error -->
<section>
        <h2 align="left">Biggest Issue with Current Quantum Computing</h2>
        <p align="left">Decoherence/Noise: the loss of coherence, where a quantum system reverts to a classical state due to interactions with the environment.</p>
        <p align="left">It is an issue as to perform computation, qubits need to be in an entangled or in superposition.</p>
        <p align="left">Overcome using quantum error correcting (QEC) codes such as repetition codes, and circuits are designed to not spread error.</p>
</section>

<!-- Hardware designs -->
<section>
    <h2>Hardware Designs</h2>
    <div>
        <table style="background-color:rgba(241, 192, 192, 0.25);">
                <thead>
                    <tr>
                    <th style="background-color:rgba(255, 255, 255)"></th>
                    <th style="padding: 0px; font-size: 70%; background-color:rgba(255, 255, 255)">Silicon Spin</th>
                    <th style="padding: 0px; font-size: 70%; background-color:rgba(255, 255, 255)">Superconducting</th>
                    <th style="padding: 0px; font-size: 70%; background-color:rgba(255, 255, 255)">Ion Traps</th>
                    <th style="padding: 0px; font-size: 70%; background-color:rgba(255, 255, 255)">Diamond</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                    <td style="padding: 0px; font-size: 70%; background-color:rgba(255, 255, 255)"><b>Pros</b></td>
                    <td style="font-size: 70%;">High stability, reproducible, manufacturable</td>
                    <td style="font-size: 70%;">Fast, easy to fabricate, flexible</td>
                    <td style="font-size: 70%;">One of the first qubit designs, very stable</td>
                    <td style="font-size: 70%;">Can operate at room temperature, interacts with light</td>
                    </tr>
                    <tr>
                    <td style="padding: 0px; font-size: 70%; background-color:rgba(255, 255, 255)"><b>Cons</b></td>
                    <td style="font-size: 70%;">Difficult to interconnect: only two entangled</td>
                    <td style="font-size: 70%;">Unstable, low temperatures required</td>
                    <td style="font-size: 70%;">Requires large vacuum, many lasers and slow</td>
                    <td style="font-size: 70%;">Difficult to entangle and fabricate reproducibility</td>
                    </tr>
                    <tr>
                    <td style="padding: 0px; font-size: 70%; background-color:rgba(255, 255, 255)"><b>Number Entangled</b></td>
                    <td style="font-size: 70%;">2</td>
                    <td style="font-size: 70%;">53</td>
                    <td style="font-size: 70%;">14</td>
                    <td style="font-size: 70%;">2</td>
                    </tr>
                    <tr>
                    <td style="padding: 0px; font-size: 70%; background-color:rgba(255, 255, 255)"><b>Coherence Time</b></td>
                    <td style="font-size: 70%;">30s</td>
                    <td style="font-size: 70%;">50$\mu s$</td>
                    <td style="font-size: 70%;">1000s</td>
                    <td style="font-size: 70%;">2s</td>
                    </tr>
                    <tr>
                    <td style="padding: 0px; font-size: 70%; background-color:rgba(255, 255, 255)"><b>Developers</b></td>
                    <td style="font-size: 70%;">Intel, UNSW, Princeton, TUDelft</td>
                    <td style="font-size: 70%;">D-Wave, IBM, Google, Rigetti, TUDelft</td>
                    <td style="font-size: 70%;">IonQ, MIT</td>
                    <td style="font-size: 70%;">TUDelft, Harvard</td>
                    </tr>
                </tbody>
            </table>
    </div>
</section>

<!-- Dwave -->
<section>
    <section>
        <h2>D-Wave 2000Q</h2>
        <p>2000 qubit quantum annealer (not a universal quantum computer!)</p>
        <div class="left">
            <br>
            <a><img class="plain" width="80%" height="80%" src="https://upload.wikimedia.org/wikipedia/commons/1/17/DWave_128chip.jpg"></a>
            <p class="cite">
                From <a href="https://commons.wikimedia.org/wiki/File:DWave_128chip.jpg">D-Wave</a> (2009).
            </p>
        </div>
        <div class="right">
            <a><img class="plain" width="100%" height="100%" src="https://cdn.arstechnica.net/wp-content/uploads/2017/01/qubit_connectivity.gif"></a>
            <p class="cite">
                From <a href="https://arstechnica.com/science/2017/01/explaining-the-upside-and-downside-of-d-waves-new-quantum-computer/">Ars Technica</a> (2017).
            </p>
        </div>
    </section>
    <section>
        <h2>D-Wave Annealer Speedup</h2>
        <br>
        <img class="plain" width="60%" height="60%" src="/images/intro-qc/dwave-graph.png">
        <p style="font-size:50%"><b>DW</b>: D-Wave &emsp; <b>SA</b>: Simulated Annealing &emsp; <b>SVMC</b>: Spin Vector Monte Carlo &emsp; <b>QMC</b>: Quantum Monte Carlo &emsp; <b>HFS</b>: Hamze-de Freitas-Selb Algorithm</p>
        <p class="cite">
            From <a href="https://arxiv.org/pdf/1701.04579.pdf">Quantum Annealing amid Local Ruggedness and Global Frustration</a> (2017).
        </p>
    </section>
</section>

<!-- Google supremacy -->
<section>
        <section>
            <a href="https://www.popularmechanics.com/technology/a29190975/google-quantum-supremacy/"><img class="plain" src="/images/intro-qc/google_article.png"></a>
        </section>
        <section>
            <a href="https://t.co/YOeB4cZqN1?amp=1"><img class="plain" width="70%" height="70%" src="/images/intro-qc/google_paper.png"></a>
            <p style="font-size: 40%">(Not officially released or peer reviewed!)</p>
            <!-- <br> -->
            <div class="fragment" data-autoslide="700">
                <h4 align="left">The task:</h4>
                <p style="font-size:80%" align="left">Sampling the output of pseudo-random quantum circuits. The circuits entangle a set of qubits by repeated application of single and two qubit operations which produce a set of bitstrings.
                The output is a probability distribution of the bitstrings.</p>
            </div>
            <div class="fragment" data-autoslide="700">
                <h4 align="left">Result:</h4>
                <p style="font-size:80%" align="left">Sampling the random circuit 1 million times <br>
                Google Sycamore (53 qubits): 200s <br>
                Classical supercomputer (Summit, Julich): 10,000yrs on 10M cores</p>
            </div>
            <div class="fragment" data-autoslide="700">
                <h4 align="left">Implication:</h4> 
                <p style="font-size:80%" align="left">Does <em>not</em> mean we can now break encryption!</p>
            </div>
            <div class="fragment" data-autoslide="0"></div>
        </section>
</section>

<!-- Quantum bullshit -->
<section>
    <div class="left">
        <h2>Quantum Bullshit Detector</h2>
        <p>Detects bullshit articles and comments in the media.</p>		
        <a href="https://twitter.com/BullshitQuantum"><img class="plain" src="/images/intro-qc/bs_banner.png"></a>
    </div>
    <div class="right">
        <a href="https://twitter.com/BullshitQuantum/status/1175214729347751938"><img class="plain fragment" data-autoslide="700" width="80%" height="80%" src="/images/intro-qc/bs2.png"></a>
        <a href="https://twitter.com/BullshitQuantum/status/1161304665952120833"><img class="plain fragment" data-autoslide="700" width="80%" height="80%" src="/images/intro-qc/nbs.png"></a>
        <a href="https://twitter.com/BullshitQuantum/status/1175257413319938049"><img class="plain fragment" data-autoslide="700" width="80%" height="80%" src="/images/intro-qc/bs1.png"></a>
    </div>
    <div class="fragment" data-autoslide="0"></div>
</section>

<!-- Useful resources -->
<section>
  <h2>Useful Resources</h2>
    <ul class="fragment scrollbar" data-autoslide="700">
        <li>Slides: <a href="https://desireevl.com/slides">https://desireevl.com/slides</a></li>
        <li>Bernstein-Vazirani IPYNB: <a href="https://github.com/desireevl/desireevl.github.io/blob/master/images/intro-qc/Bernstein-Vazirani.ipynb">https://github.com/desireevl/desireevl.github.io/blob/master/images/intro-qc/Bernstein-Vazirani.ipynb</a></li>
        <li>List of QC resources: <a href="https://github.com/desireevl/awesome-quantum-computing">https://github.com/desireevl/awesome-quantum-computing</a></li>
        <li>Michelle Simmons talk: <a href="https://www.youtube.com/watch?v=FnPp73F5cnE ">https://www.youtube.com/watch?v=FnPp73F5cnE</a></li>
        <li>D-Wave hardware: <a href="https://arxiv.org/pdf/1611.04528.pdf">https://arxiv.org/pdf/1611.04528.pdf</a>, <a href="https://arxiv.org/pdf/1701.04579.pdf">https://arxiv.org/pdf/1701.04579.pdf</a></li>
        <li>Google quantum supremacy paper: <a href="https://t.co/TVgiNS54FK?amp=1">https://t.co/TVgiNS54FK?amp=1</a></li>
        <li>Google quantum supremacy supplementary materials: <a href="https://t.co/8m8NHBbcDK?amp=1">https://t.co/8m8NHBbcDK?amp=1</a> </li>
    </ul>
  <div class="fragment" data-autoslide="0"></div>
</section>

<!-- Thanks and social media -->
<section>
  <h2>Thanks!</h2>
  <br>
  <div class="left">
    <br>
    <div>
      <img style="vertical-align:middle" src="/images/intro-qc/computer.png" class="plain" width="35" height="35">
      <span style="padding: 0 0 0 0.5em"><a href="https://desireevl.com">desireevl.com</a></span>
    </div>
    <div>
      <img style="vertical-align:middle" src="/images/intro-qc/instagram.png" class="plain" width="30" height="30">
      <span style="padding: 0 0 0 0.5em"><a href="http://instagram.com/mr.miso.oz">@mr.miso.oz (my cat)</a></span>
    </div>
    <div>
      <img style="vertical-align:middle" src="/images/intro-qc/twitter.png" class="plain" width="35" height="35">
      <span style="padding: 0 0 0 0.5em"><a href="https://twitter.com/desireevogtlee">@desireevogtlee</a></span>
    </div>
  </div>
  <div class="right">
    <a href="http://www.desireevl.com"><img class="plain" width="450" height="250" src="/images/miso.jpg"></a>
  </div>
</section>
