---
layout: slide
title: Quantum Game Theory
description: Qiskit Advocates Presentation
theme: white
custom_css: quantum-game-theory
transition: slide
date: 2020-01-06
---

<!-- Title and About me slides -->
<section>
    <section>
        <h1>Quantum Game Theory</h1>
        <br>
        <p>
        <small>Desiree Vogt-Lee</small>
        </p>
    </section>
    <section>
        <h2>The Beginning</h2>
        <ul>
            <li>Idea formed at the Qiskit Hackathon Europe (2019)</li>
            <li>Decided to continue post-hackathon as we all enjoyed working together and wanted to create a better version of our 24 hr mockup</li>
        </ul>
        <a href="http://www.desireevl.com/posts/qcamp-europe"><img width="489.6" height="295.2" src="/images/qcamp-europe/team.jpg"></a>
    </section>
    <section>
        <h2>Version 1 - at the Hackathon</h2>
        <div class="left">
            <img class="plain" style="padding-left: 120px;" width="60%" height="60%" src="/images/quantum-game-theory/old_load_screen.png">
            <br>
            <img class="plain" style="padding-left: 120px;" width="60%" height="60%" src="/images/quantum-game-theory/old_player2_screen.png">
            <br>
        </div>
        <div class="right">
            <img class="plain" style="padding-right: 120px;" width="60%" height="60%" src="/images/quantum-game-theory/old_player1_screen.png">
            <br>
            <img class="plain" style="padding-right: 120px;" width="60%" height="60%" src="/images/quantum-game-theory/old_results_screen.png">
            <br>
        </div>
    </section>
    <section data-background-iframe="https://nbviewer.jupyter.org/github/desireevl/quantum-game-theory/blob/master/notebooks/quantum_game_theory.ipynb" data-background-interactive>
        <div style="position: absolute; width: 30%; right: 0; box-shadow: 0 1px 4px rgba(0,0,0,0.5), 0 5px 25px rgba(0,0,0,0.2); background-color: rgba(241, 192, 192, 0.4); color: #000000; padding: 20px; font-size: 20px; color: #4a4746; text-align: left;">
            <p>Quantum Game Theory tutorial (with exercises) as Jupyter Notebook.</p>
        </div>
    </section>
        <section data-background-iframe="http://quantum-game.desireevl.com/" data-background-interactive>
        <div style="position: absolute; width: 30%; right: -10%; box-shadow: 0 1px 4px rgba(0,0,0,0.5), 0 5px 25px rgba(0,0,0,0.2); background-color: rgba(241, 192, 192, 0.4); color: #000000; padding: 20px; font-size: 20px; color: #4a4746; text-align: left;">
            <p>Version 2 - post Hackathon <br><br> New user interface to play different games and run on the IBMQ simulator. <br><br>Available at:<br> http://quantum-game.desireevl.com/</p>
        </div>
    </section>
</section>

<!-- Game theory terms -->
<section>
    <h2>Game Theory Terminology</h2>
    <ul>
        <li>Payoff Matrix: A way to visualise all possible outcomes that can occur when two or more players make a strategic decision.</li>
        <li>Nash Equilibrium: A solution to a cooperative game in which each player is assumed to know the equilibrium strategies of the other players, and no player has anything to gain by changing only their own strategy.</li>
    </ul>
</section>

<!-- Different game theory games -->
<section>
    <section>
        <h2>Game Theory Games</h2>
        <ul>
            <li>Game of Chicken</li>
            <li>Prisoner's Dilemma</li>
            <li>Minority Game</li>
            <li>Bach or Stravinsky</li>
        </ul>
    </section>
    <section>
        <h2>Game of Chicken</h2>
        <p>Two players are heading towards each other. If the players both continue on the same path, they collide with each other. If one swerves out of the way and the other doesn't, the swerver loses and is labelled the chicken, while the other, implicitly braver player, wins.</p>
        <style type="text/css">
        .tg  {border-collapse:collapse;border-spacing:0;border:none;}
        .tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:0px;overflow:hidden;word-break:normal;}
        .tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:0px;overflow:hidden;word-break:normal;}
        .tg .tg-vsem{background-color:rgba(241, 192, 192, 0.25);text-align:center;vertical-align:top}
        .tg .tg-vxga{background-color:#ffffff;text-align:center;vertical-align:middle}
        .tg .tg-qrep{background-color:rgba(241, 192, 192, 0.25);text-align:center;vertical-align:top}
        .tg .tg-i81m{background-color:#ffffff;text-align:center;vertical-align:top}
        </style>
        <table class="tg">
        <tr>
            <th class="tg-vxga">Measured State</th>
            <th class="tg-i81m">Payoff to Players</th>
        </tr>
        <tr>
            <td class="tg-qrep">&#124;00&#9002;</td>
            <td class="tg-vsem">(0, 0)</td>
        </tr>
        <tr>
            <td class="tg-qrep">&#124;01&#9002;</td>
            <td class="tg-vsem">(-1, 1)</td>
        </tr>
        <tr>
            <td class="tg-qrep">&#124;10&#9002;</td>
            <td class="tg-vsem">(1, -1)</td>
        </tr>
        <tr>
            <td class="tg-qrep">&#124;11&#9002;</td>
            <td class="tg-vsem">(-10, -10)</td>
        </tr>
        </table>
    </section>
    <section>
        <h2>Prisoner's Dilemma</h2>
        <p>All players are involved in committing a crime and get caught, but not quite red handed. In order to get a confession from all players, the police separate each player into different rooms and present two options: one, to remain silent, and two, to confess and maybe receive a reduced sentence.</p>
        <style type="text/css">
        .tg  {border-collapse:collapse;border-spacing:0;border:none;}
        .tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:0px;overflow:hidden;word-break:normal;}
        .tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:0px;overflow:hidden;word-break:normal;}
        .tg .tg-vsem{background-color:rgba(241, 192, 192, 0.25);text-align:center;vertical-align:top}
        .tg .tg-vxga{background-color:#ffffff;text-align:center;vertical-align:middle}
        .tg .tg-qrep{background-color:rgba(241, 192, 192, 0.25);text-align:center;vertical-align:top}
        .tg .tg-i81m{background-color:#ffffff;text-align:center;vertical-align:top}
        </style>
        <table class="tg">
        <tr>
            <th class="tg-vxga">Measured State</th>
            <th class="tg-i81m">Payoff to Players</th>
        </tr>
        <tr>
            <td class="tg-qrep">&#124;00&#9002;</td>
            <td class="tg-vsem">(-1, -1)</td>
        </tr>
        <tr>
            <td class="tg-qrep">&#124;01&#9002;</td>
            <td class="tg-vsem">(-3, 0)</td>
        </tr>
        <tr>
            <td class="tg-qrep">&#124;10&#9002;</td>
            <td class="tg-vsem">(0, -3)</td>
        </tr>
        <tr>
            <td class="tg-qrep">&#124;11&#9002;</td>
            <td class="tg-vsem">(-2, -2)</td>
        </tr>
        </table>
    </section>
    <section>
        <h2>Minority Game</h2>
        <p>A simple anti-coordination game in which a player wins the game if their outcome is different to every other player's.</p>
        <style type="text/css">
        .tg  {border-collapse:collapse;border-spacing:0;border:none;}
        .tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:0px;overflow:hidden;word-break:normal;}
        .tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:0px;overflow:hidden;word-break:normal;}
        .tg .tg-vsem{background-color:rgba(241, 192, 192, 0.25);text-align:center;vertical-align:top}
        .tg .tg-vxga{background-color:#ffffff;text-align:center;vertical-align:middle}
        .tg .tg-qrep{background-color:rgba(241, 192, 192, 0.25);text-align:center;vertical-align:top}
        .tg .tg-i81m{background-color:#ffffff;text-align:center;vertical-align:top}
        </style>
        <table class="tg">
        <tr>
            <th class="tg-vxga">Measured State</th>
            <th class="tg-i81m">Payoff to Players</th>
        </tr>
        <tr>
            <td class="tg-qrep">&#124;0000&#9002;</td>
            <td class="tg-vsem">(0, 0, 0, 0)</td>
        </tr>
        <tr>
            <td class="tg-qrep">&#124;0001&#9002;</td>
            <td class="tg-vsem">(0, 0, 0, 1)</td>
        </tr>
        <tr>
            <td class="tg-qrep">&#124;0100&#9002;</td>
            <td class="tg-vsem">(0, 1, 0, 0)</td>
        </tr>
        <tr>
            <td class="tg-qrep">&#124;0101&#9002;</td>
            <td class="tg-vsem">(0, 0, 0, 0)</td>
        </tr>
        <tr>
            <td class="tg-qrep">. . . </td>
            <td class="tg-vsem">. . . </td>
        </tr>
        </table>
    </section>
    <section>
        <h2>Bach or Stravinsky</h2>
        <p>Two player coordination game involving Alice and Bob who want to attend a musical concert. Alice prefers Bach and Bob prefers Stravinsky however they would like to attend a concert together.</p>
        <style type="text/css">
        .tg  {border-collapse:collapse;border-spacing:0;border:none;}
        .tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:0px;overflow:hidden;word-break:normal;}
        .tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:0px;overflow:hidden;word-break:normal;}
        .tg .tg-vsem{background-color:rgba(241, 192, 192, 0.25);text-align:center;vertical-align:top}
        .tg .tg-vxga{background-color:#ffffff;text-align:center;vertical-align:middle}
        .tg .tg-qrep{background-color:rgba(241, 192, 192, 0.25);text-align:center;vertical-align:top}
        .tg .tg-i81m{background-color:#ffffff;text-align:center;vertical-align:top}
        </style>
        <table class="tg">
        <tr>
            <th class="tg-vxga">Measured State</th>
            <th class="tg-i81m">Payoff to Players</th>
        </tr>
        <tr>
            <td class="tg-qrep">&#124;00&#9002;</td>
            <td class="tg-vsem">(3, 2)</td>
        </tr>
        <tr>
            <td class="tg-qrep">&#124;01&#9002;</td>
            <td class="tg-vsem">(0, 0)</td>
        </tr>
        <tr>
            <td class="tg-qrep">&#124;10&#9002;</td>
            <td class="tg-vsem">(0, 0)</td>
        </tr>
        <tr>
            <td class="tg-qrep">&#124;11&#9002;</td>
            <td class="tg-vsem">(2, 3)</td>
        </tr>
        </table>
    </section>
</section>

<!-- Quantum Game Theory -->
<section>
    <section>
        <h2>The First Quantum Game</h2>
        <p></p>
    </section>
    <section>
        <img class="plain" style="padding-left: 120px;" width="60%" height="60%" src="/images/quantum-game-theory/ewl.png">
        <p>https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.87.069802</p>
    </section>
</section>


<!-- Demos -->
<section>
    <section data-background-iframe="https://nbviewer.jupyter.org/github/desireevl/quantum-game-theory/blob/master/notebooks/quantum_game_theory.ipynb" data-background-interactive>
    </section>
    <section data-background-iframe="http://quantum-game.desireevl.com/" data-background-interactive>
    </section>
</section>

<!-- Improvements/suggestions/feedback -->
<section>
    <h2>Thanks!</h2>
    <p>Suggestions are welcome. Hopeful additions:</p>
    <ul>
        <li>Ability to run the circuits on a real IBMQ device</li>
        <li>Option to view the payoff table on the results page</li>
        <li>Further upgrades to the UI</li>
        <li>More information about QGT as you play</li>
    </ul>
</section>