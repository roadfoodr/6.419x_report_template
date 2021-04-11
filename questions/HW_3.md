## Module 3: Network Analysis
### Problem 1: Suggesting Similar Papers
>A citation network is a directed network where the vertices are academic papers and there is a directed edge from paper $A$ to paper $B$ if paper $A$ cites paper $B$ in its bibliography. **Google Scholar** performs automated citation indexing and has a useful feature that allows users to find similar papers. In the following, we analyze two approaches for measuring similarity between papers.
|
> **1.2.c** (2 points) How does the time complexity of your solution involving matrix multiplication in part (a) compare to your friend's algorithm? (100 word limit)
|
> **1.2.d** (3 points) Bibliographic coupling and cocitation can both be taken as an indicator that papers deal with related material. However, they can in practice give noticeably different results. Why? Which measure is more appropriate as an indicator for similarity between papers? (100 word limit)
|
### Problem 2: Investigating a time-varying criminal network
>In this problem, you will study a time-varying criminal network that is repeatedly disturbed by police forces. The data for this problem can be found in the CAVIAR directory of the data archive.
|
> **2.c** (2 points) Observe the plot you made in Part (a) Question 1. The number of nodes increases sharply over the first few phases then levels out. Comment on what you think may be causing this effect. Based on your answer, should you adjust your conclusions in Part (b) Question 5? (200 word limit)
|
> **2.d** (5 points) In the context of criminal networks, what would each of these metrics teach you about the importance of an actor's role in the traffic? In your own words, could you explain the limitations of degree centrality? In your opinion, which one would be most relevant to identify who is running the illegal activities of the group? Please justify. (400 word limit)
|
> **2.e** (3 points) In real life, the police need to effectively use all the information they have gathered, to identify who is responsible for running the illegal activities of the group. Armed with a qualitative understanding of the centrality metrics from Part (d) and the quantitative analysis from Part (b) Question 5, integrate and interpret the information you have to identify which players were most central (or important) to the operation.

> Hint: Note that the definition of a player's "importance" (i.e. how central they are) can vary based on the question you are trying to answer. Begin by defining what makes a player important to the group (in your opinion) ; use your answers from Part (d) to identify which metric(s) are relevant based on your definition and then, use your quantitative analysis to identify the central and peripheral traffickers. You may also perform a different quantitative analysis, if your definition of importance requires it. (200 word limit)
|
> **2.f.2** (3 points) The change in the network from Phase X to X+1 coincides with a major event that took place during the actual investigation. Identify the event and explain how the change in centrality rankings and visual patterns, observed in the network plots above, relates to said event. (300 word limit)
|
> **2.g** (4 points) While centrality helps explain the evolution of every player's role individually, we need to explore the *global* trends and incidents in the story in order to understand the behavior of the criminal enterprise.

> Describe the coarse pattern(s) you observe as the network evolves through the phases. Does the network evolution reflect the background story?

> **Hint: Look at the set of actors involved at each phase, and describe how the composition of the graph is changing. Investigate when important actors seem to change roles by their movement within the hierarchy. Correlate your observations with the information that the police provided in the setup to this homework problem.** (300 word limit)
|
> **2.h** (2 points) Are there other actors that play an important role but are not on the list of investigation **(i.e., actors who are not among the 23 listed above)** ? List them, and explain why they are important. (100 word limit)
|
> **2.i** (2 points) What are the advantages of looking at the directed version vs. undirected version of the criminal network?

>**Hint: If we were to study the directed version of the graph, instead of the undirected, what would you learn from comparing the in-degree and out-degree centralities of each actor? Similarly, what would you learn from the left- and right-eigenvector centralities, respectively?** (250 word limit)
|
> **2.j** (4 points) Recall the definition of hubs and authorities. Compute the hub and authority score of each actor, and for each phase. (**Remember** to load the adjacency data again this time using `create_using = nx.DiGraph()`.)

>With **networkx** you can use the `nx.algorithms.link_analysis.hits` function, set `max_iter=1000000` for best results.

> Using this, what relevant observations can you make on how the relationship between **n1** and **n3** evolves over the phases. Can you make comparisons to your results in Part (g)?

> **Optional: Also comment on what the hub and authority score can tell you about the actors you identified in Part (e).** (400 word limit)
|
### Problem 4: Co-offending Network

>The data for this problem set consists of individuals who were arrested in Quebec between 2003 and 2010. Some of the individuals have always acted solo, and have been arrested alone throughout their criminal career. Others co-offended with other individuals, and have been arrested in groups. The goal of this problem set is to construct and analyze the co-offender network. The nodes in the network are the offenders, and two offenders share a (possibly weighted) edge whenever they are arrested for the same crime event.
|
> **4.g** (3 points) Plot the degree distribution (or an approximation of it if needed) of G. Comment on the shape of the distribution. Could this graph have come from an Erdos-Renyi model? Why might the degree distribution have this shape? (100 word limit)
|
> **4.m** (4 points) Plot the distribution of clustering coefficients for each node for $G_r$ and $G_{nr}$. What shape do the plots make? What does this tell you about the behavior of the actors? **Hint: What does it mean for an actor to have a clustering coefficient of 0.5? Are there as many actors with intermediate clustering coefficients (say, between 0.25 and 0.75) as you expect for each graph?** (400 word limit)
|
> **4.n** (4 points) Pick a centrality measure (degree, eigenvector, betweenness, etc) and compute the scores for the top component of $G_r$ and $G_{nr}$. Compare the distribution of the centrality across nodes (for example, with summary statistics and/or a histogram). Examine the number of crimes committed by the most central actor in the repeat offender graph, does this support your conclusions? (300 word limit)
|
### Project

> The last part of this assignment is an open-ended project. Choose a sociologically interesting question about the co-offending network, and try to answer your question using the data. You can subset the data in whichever way you desire as long as it is sociologically meaningful. For example, you can group nodes by attributes such as sex, group edges such as repeat/non-repeating cooffenses, use the weighted or unweighted co-offending networks, focus on the largest connected component, etc.
|