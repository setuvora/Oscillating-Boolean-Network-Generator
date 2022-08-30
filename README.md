# Oscillating-Boolean-Network-Generator

How frequently is a randomly generated boolean network able to produce indefinite oscillation? 

Here, I use the following program to address this question.

This program:

  (1) generates a random boolean network of N nodes and K edges (loosely based off the Watts-Strogatz model) with signed (+ or -) and directed (-->) edges.
  (2) runs the network for t timesteps (with the initial condition being all nodes ON to provide sufficient stimulus to the system), and 
  (3) heuristically determines whether a given network is capable of indefinite oscillation.

Here are the simulations of 30 networks (N=4, k=3) that produce indefinite oscillation. Each network is simulated over 10 timesteps. x-axis: nodes, y-axis (from top to botom): timesteps. Blue corresponds to OFF and yellow corresponds to ON node status for each timestep. 

<img width="800" alt="image" src="https://user-images.githubusercontent.com/44078648/179062753-a0786f84-5fbe-4b49-b835-bdcbafd351a5.png">

Now, let's scan through various node and edge parameter settings and generate 100 random networks for each one. Then we can see how often we obtain a network capable of indefinite oscillation for each parameter set:

<img width="600" alt="image" src="https://user-images.githubusercontent.com/44078648/179062910-fdb052ee-1607-411a-a87e-d2acf3a3a3ef.png">

We see that the probability a randomly generated network will be capable of oscillation scales with network size and connectivity. No networks with a threshold of k<4 are capapble of producing oscillation (at the number of trials sampled). Importantly, we see that under a large range of parameters indefinite oscillation is common, sometimes at frequencies over 1/6.

