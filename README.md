# Oscillating-Boolean-Network-Generator
Oscillating Boolean Network Generator to look for behaviors exhibited by biological systems


It is unclear whether the sophistication of biological systems is driven by the additive action of many singular parts (such as individual protein molecules) or by the network topology of their interactions (such as cell signaling networks that exist between individual proteins). The latter view is supported by the fact that Boolean logic networks have been used to model complex biological systems for decades.  A classic example here is the cell cycle network, whose cycling behavior is largely dictated by its network topology and is maintained over an astonishingly large swath of parameter space.

What "life-like" behaviors can be obtained simply by generating random boolean logic networks? Let's assume cycling behavior is "life-like" (real life examples could include: cyclic pattern generator activity in the central nervous system of metazoans, oscillating activity of transcription factors, and segmented morphogen gradient patterns during development).  

How frequently does a randomly generated network of N nodes and k edges produce indefinite oscillation? 

Here, I use the following program to address this question.

This program:
(1) generates a random boolean network of N nodes and K edges (loosely based off the Watts-Strogatz model) with signed (+ or -) and directed (-->) edges.
(2) runs the network for t timesteops (with the initial condition being all nodes ON to provide sufficient stimulus to the system at t0), and 
(3) heuristically determines whether a given network is capable of indefinite oscillation.

Here are 30 networks (N=4, k=3) that produce indefinite oscillation, simulated over 10 timesteps. x-axis: nodes, y-axis (from top to botom): timesteps. Blue corresponds to OFF and yellow corresponds to ON node status for each timestep. 

<img width="800" alt="image" src="https://user-images.githubusercontent.com/44078648/179062753-a0786f84-5fbe-4b49-b835-bdcbafd351a5.png">

Now, let's scan through various node and edge parameter sets and generate 100 random networks for each. Then we can see how often we obtain a network capable of indefinite oscillation for each parameter set:

<img width="600" alt="image" src="https://user-images.githubusercontent.com/44078648/179062910-fdb052ee-1607-411a-a87e-d2acf3a3a3ef.png">

We see that probability a randomly generated network will be capable of oscillation if a function of network size and connectivity. No networks with k<3 are capapble of producing oscillation (at the number of networks sampled). Importantly, we see that under a large range of parameters indefinite oscillation is favored, sometimes at frequencies over 1/6.

Thus, it can be imagined that systems of interdependent parts with moderate connectivities are naturally capable of "life-like" behaviors as a universal quality.
