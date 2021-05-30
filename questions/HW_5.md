## Module 5: Environmental Data and Gaussian Processes|||  
### Part I - Ocean Flow|||  
### Problem 2: Identifying long-range correlations|||  
**1.** In this problem, we will try to identify areas in the Philippine Archipelago with long-range correlations. Your task is to identify two places on the map that are not immediately next to each other but still have some high correlation in their flows. Your response should be the map of the Archipelago with the two areas marked (e.g., circled). You claim that those two areas have correlated flows. Explain how you found that those two areas have correlated flows.

- (5 points): A map with the two points with correlations marked.  
- (3 points): Provides an explanation of how the correlation was computed.  
- (2 points): Provides a convincing commentary on why the two marked locations could be correlated.|||  

### Problem 3: Simulating particle movement in flows
In this problem, you are asked to build a simulator that can track a particle's movement on a time-varying flow.|||  
**a.** We assume that the velocity of a particle in the ocean, with certain coordinates, will be determined by the corresponding water flow velocity at those coordinates. Implement a procedure to track the position and movement of multiple particles as caused by the time-varying flow given in the data set. Explain the procedure, and show that it works by providing examples and plots.  

Draw particle locations uniformly at random across the entire map, do not worry if some of them are placed on land. Simulate the particle trajectories for 300 hours and provide a plot of the initial state, a plot of the final state, and two plots at intermediate states of the simulation. You may wish to draw colors at random for your particles in order to help distinguish them.

- (3 points): Provides an explanation of the simulation algorithm, with equations for the evolution of the particle trajectory.  
- (2 points): Provides a plot of the initial state of the simulation.  
- (3 points): Provides two plots of intermediate states of the simulation.  
- (2 points): Provides a plot of the final state of the simulation.|||  

**b.** A (toy) plane has crashed in the Sulu Sea at $T=0$. The exact location is unknown, but data suggests that the location of the crash follows a Gaussian distribution with mean $(100,350)$ (namely $(300km,1050km)$) with variance $\sigma^2$. The debris from the plane has been carried away by the ocean flow. You are about to lead a search expedition for the debris. Where would you expect the parts to be at $48$hrs, $72$hrs, $120$hrs? Study the problem by varying the variance of the Gaussian distribution. Either pick a few variance samples or sweep through the variances if desired. (Hint: Sample particles and track their evolution.)

- (3 points): Provides plots showing the state of the simulation at the times: T=48hrs, 72hrs, 120hrs. (Three plots required.)  
- (3 points): Two or more additional choices of the variances were tried, and three plots of the state of the simulation at the above three times are provided. (Six additional plots required.)  
- (4 points): Comments on where one should concentrate search activities based on the observed results.|||
### Part II - Estimating Flows with Gaussian Processes|||  
### Problem 4: Creating a Gaussian process model for the flow
In this problem, we will create a Gaussian process model for the flow given the information we have.||| 
**a.** Pick a location of your liking from the map for which you are given flow data (ideally from a location on the ocean not in the land). Moreover, consider the two vectors containing the flow speed for each direction: you will end up with two vectors of dimension $100$.  

You are asked to find the parameters of the kernel function that best describes the data independently for each direction.

- (1 point): States the choice of kernel function and provides a justification for this choice.  
- (1 point): Identifies the parameters of the kernel function.  
- (1 point): Explicitly states the search space for each kernel parameter.  
- (1 point): Explicitly states the number of folds (k) for the cross-validation.  
- (3 points): Provides the optimal kernel parameters from the search.  
- (3 points): Provides a plot of the computed cost/performance metric over the search space for the kernel parameters.|||  
**b.** Run the process described in the point (a) for at least three more points in the map, you free to choose more if you wish. What do you observe? Which of your kernel parameters show patterns? Which do not?

- (3 points): Provides the optimal kernel values for three new location that are different from the location in Problem 4.a. (Plots do not need to be provided.)  
- (2 points): For each kernel parameter, states if a pattern was observed.|||
**c.** We have suggested one particular value for $\tau$. Consider other possible values and comment on the effects such parameter has on the estimated parameters and the estimation process's performance. Try at least two values different from that used in Problem 4.a.

(1 point): Provides the optimal kernel values for at least two new choices of $\tau$.  
(2 points): A plot showing the cost/optimization target is provided for the search space, for each choice of $\tau$.  
(2 points): Comments on whether these results differ from those found in Problem 4.a, and on whether results from the choices of $\tau$ in the problem differ from each other.|||
**d.** Currently, most of the commonly used languages like Python, R, Matlab, etc., have pre-installed libraries for Gaussian processes. Use one library of your choice, maybe the language or environment you like the most, and compare the obtained results. Did you get the same parameters as in problem 4.a? If not, why are they different? Elaborate on your answer.

(2 points): Provides the optimal kernel parameters as found through the software library.  
(2 points): Provides details on the library used.  
(2 points): Comments on whether these results differ from those found in Problem 4.a.  
(2 points): The results are the same, or, the results are different and an explanation is provided.  
(2 points): A plot showing the cost/optimization target is provided for the search space, or a plot comparing the predictions generated (in problem 5) if the results are different.|||  
### Problem 5: Estimating unobserved flow data  
In the previous problem, we have found a good set of parameters to model the sequence of speeds at one location as a Gaussian process. Recall that we have assumed our 100 observations came at a rate of one every three days. We are going to assume that when we advance to our simulations, we will choose a smaller time step. Thus, we need to interpolate how the flow would look like at some unobserved points.|||  
**a.** You are given flow information every three days. Pick some time stamps in-between each observation for which to estimate the flow. For example, you want flows every day, so there will be two unknown points between two observations. You could pick only one, or more than two. Make your choice and explain why.  

Compute the conditional distribution (mean and covariance) at the time locations selected in part (a). Use the kernel parameters that you obtained in Problem 4.a, and use the same location as you did in Problem 4.a.  

For the initial estimate of the mean at the unknown time locations, you can use zero, use the average of all the observations, or take the average of the two closest observed points.  

Plot your predictions, clearly showing:

- The predicted means.  
- The predicted standard deviation as a $3\sigma$ band (three standard deviations above and below the mean).  
- The observed data points.  
    
    
- (2 points): Clearly states the choice of time-stamps at which to create predictions, and states why the choice was made.  
- (2 points): Clearly states the method by which the prior means were chosen.  
- (2 points): Provides a plot with a prediction for the horizontal velocity component at the chosen location.  
- (2 points): Provides a plot with a prediction for the vertical velocity component at the chosen location.  
- (3 points): Both plots have a labelled prediction for the mean for all of the time-stamps chosen.  
- (3 points): Both plots have a labelled $3\sigma$ band around the predicted mean for all of the time-stamps chosen.  
- (1 point): Both plots have the observations included.|||  
### Problem 6: A longer time-scale simulation  
In the previous problems, we learned to model the flow at one location as a Gaussian process. Thus, we can extend this to estimate the flow at any point in time at that particular location using the kernel function parameters. At a certain point in time, the flow can be computed as the realization of a multivariate Gaussian random variable with parameters given by the conditional distributions given the flow data. At this point, you are asked to simulate a particle moving according to the flow data and using the estimates for times between the original timestamps of the problem.  

Ideally, one would have to estimate the parameters of the flow at every point in the map. However, having to run $504 \times 555$ parameter selection models seems like much computational work. So, here we take a more straightforward approach: use your results from Problem 4.b to choose a value of your kernel parameters that is generally representative of the points that you tested.|||  
**a.** Modify the simulator that you built in Problem 3.3 to use this new flow estimated flow information. Note that with this new change, you will be able to simulate the flow of particles for 300 days! Regarding data, originally, we have 100 measurements per point, now with this approach, let us say you use the estimates for two extra points to get one flow data per day, so in total, you should have at your disposal 300 descriptions of flow per location.  

Now repeat Problem 3 (b). This time you will be simulating flows for 300 days. This allows some debris to arrive on land. Where are some possible places along the coast where one could find debris? Again, to do this, pick some σ of your choice, and simulate the movement of particles with initial location sampled from the bivariate Gaussian. Evolve the location of the particles. Some times particles trajectories will terminate on the shore. Continue to keep track of such particles. These points are likely where you could find the debris.  

Provide a plot that includes your initial, final, and at least one intermediate state of your simulation. For the final state, clearly mark one location on land where you would search for debris. Also mark one location over the ocean where you would search for debris. Provide a brief justification for both choices.  

Try at least one other value for $\sigma$, and create the same three plots. Comment if your conclusions should change.  

- (2 points): Provides a plot with the initial state of the simulation.  
- (2 points): Provides a plot with an intermediate state of the simulation.  
- (2 points): Provides a plot with the final state of the simulation.  
- (2 points): Marks a location **on the coast** of the final state of the simulation where one should search for debris and provides a justification.  
- (2 points): Marks a location **over the ocean** of the final state of the simulation where one should search for debris and provides a justification.  
- (5 points): Provides three plots (initial, intermediate, final) for one other choice of $\sigma$, and comments on results (either to state why conclusions should change or why they should not).|||  
**b.** As a final stage, you are tasked with locating three new monitoring stations on the coast. The purpose of these stations is to monitor general ocean debris. Using the tools you have build in this homework, propose the location of such three new stations. Simulate the trajectories of as many particles as you want, initialized at random locations uniformly distributed on the map. This is essentially a repeat of Problem 3 (a) with the new simulation; this time, remove particles that start on land so that they do not confuse your conclusions.  

Many of the particles will end up on the coast. A good location for a monitoring station will be areas where many of such particles land on the coast.  

Provide a plot that includes your initial, final, and at least one intermediate state of your simulation. For the final state, clearly mark where you would place your three monitoring stations. Provide a justification for why you chose these locations.  

- (2 points): Provides a plot with the initial state of the simulation, there should be no particles on land.  
- (2 points): Provides a plot with an intermediate state of the simulation.  
- (2 points): Provides a plot with the final state of the simulation.  
- (4 points): Marks three locations on the final state of the simulation where monitoring stations should be placed.  
- (4 points): Provides a convincing explanation for choosing these locations.|||  
