---
layout: slide
title: Introduction to Quantum Computing
description: UQCS Talk
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
      <a><img class="plain" width="80%" height="80%" src="images/classical.png"></a>
    </div>
    <div class="right">
      <h3>Quantum Bits (qubits)</h3>
      <br>
      <a><img class="plain" align="center" width="350" height="350" src="https://upload.wikimedia.org/wikipedia/commons/6/6b/Bloch_sphere.svg"></a>
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
</section>

<!-- Gates X, Z, H -->
<section>
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
      <h2>Gates - Pauli Z</h2>
      <div class="left">
        <a href="http://www.desireevl.com"><img class="plain" width="200" height="54.684" src="/images/intro-qc/z_gate.png"></a>
        <br>
        <p>No equivalent classical gate</p>
        <p>Performs a phase flip operation</p>
        <br>
        <p>$Z=\begin{bmatrix} 1 & 0\\ 0 & -1 \end{bmatrix}$</p>
      </div>
      <div class="fragment right" data-autoslide="900">
        <br>
        <br>
        <a href="http://www.desireevl.com"><img class="plain" width="220" height="220" src="/images/intro_unitary/Z_zero.png"></a>
        <a href="http://www.desireevl.com"><img class="plain" width="220" height="220" src="/images/intro_unitary/Z_one.gif"></a>
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
        <a><img class="plain" width="60%" height="60%" src="images/dwave-graph.png"></a>
        <p style="font-size:50%"><b>DW</b>: D-Wave &emsp; <b>SA</b>: Simulated Annealing &emsp; <b>SVMC</b>: Spin Vector Monte Carlo &emsp; <b>QMC</b>: Quantum Monte Carlo &emsp; <b>HFS</b>: Hamze-de Freitas-Selb Algorithm</p>
        <p class="cite">
            From <a href="https://arxiv.org/pdf/1701.04579.pdf">Quantum Annealing amid Local Ruggedness and Global Frustration</a> (2017).
        </p>
    </section>
</section>

<!-- Quantum algorithms -->
<section>
    <section>
        <h2>Quantum Algorithms - Shor's Algorithm</h2>
    </section>
    <section>
        <h2>Quantum Algorithms - Grover's Algorithm</h2>
    </section>
</section>

<!-- Quantum error -->
<section>
  <h2>Issues with Current Quantum Computers</h2>

</section>

<!-- Google supremacy -->
<section>
    <section>
        <a href="https://www.popularmechanics.com/technology/a29190975/google-quantum-supremacy/"><img class="plain" width="80%" heigh="80%" src="images/google_article.png"></a>
    </section>
    <section>
        <a href="https://t.co/YOeB4cZqN1?amp=1"><img class="plain" width="70%" height="70%" src="images/google_paper.png"></a>
        <br>
        <ul>
            <li>test</li>
        </ul>
    </section>
</section>

<!-- Coding demo -->
<section>
        <a href="http://localhost:8888/notebooks/Grover_IBM.ipynb" target="_blank"><img class="plain" width="80%" height="80%" src="images/google_article.png"></a>
</section>

<!-- Quantum bullshit -->
<section>
    <div class="left">
        <h2>Quantum Bullshit Detector</h2>
        <p>Detects bullshit articles and comments in the media.</p>		
        <a href="https://twitter.com/BullshitQuantum"><img class="plain" src="images/bs_banner.png"></a>
    </div>
    <div class="right">
        <a href="https://twitter.com/BullshitQuantum/status/1175214729347751938"><img class="plain fragment" data-autoslide="700" width="80%" height="80%" src="images/bs2.png"></a>
        <a href="https://twitter.com/BullshitQuantum/status/1161304665952120833"><img class="plain fragment" data-autoslide="700" width="80%" height="80%" src="images/nbs.png"></a>
        <a href="https://twitter.com/BullshitQuantum/status/1175257413319938049"><img class="plain fragment" data-autoslide="700" width="80%" height="80%" src="images/bs1.png"></a>
    </div>
    <div class="fragment" data-autoslide="0"></div>
</section>

<!-- Useful resources -->
<section>
  <h2>Useful Resources</h2>
  <ul class="fragment scrollbar" data-autoslide="700">
    <li>Slides: <a href="https://desireevl.com/slides">https://desireevl.com/slides</a></li>
    <li>List of QC resources: <a href="https://github.com/desireevl/awesome-quantum-computing">https://github.com/desireevl/awesome-quantum-computing</a></li>
    <li>Michelle Simmons talk: <a href="https://www.youtube.com/watch?v=FnPp73F5cnE ">https://www.youtube.com/watch?v=FnPp73F5cnE</a></li>
    <li>D-Wave: <a href="https://arxiv.org/pdf/1611.04528.pdf">https://arxiv.org/pdf/1611.04528.pdf</a>, <a href="https://arxiv.org/pdf/1701.04579.pdf">https://arxiv.org/pdf/1701.04579.pdf</a></li>
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
