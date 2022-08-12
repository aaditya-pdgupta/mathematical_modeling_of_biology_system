# Introduction

Mathematical modelling is a process by which a real world problem is described by a mathematical formulation. This procedure is a kind of abstraction, that means, neither all details of single processes will be described nor all aspects concerning the problem will be included.

A main problem is to find an appropriate mathematical formulation. Then, for further studies of the model, common mathematical tools can be used or new ones are developed. Shortly, a model should be as simple as possible and detailed as necessary or vise versa. One mathematical formulation may be appropriate for several real-world problem, even from very different domains. 

<p align="center">
  <img src="../main/Latex/workflow_1.jpg" />
</p>

A great challenge of modelling is to bring together the abstract, mathematical formulation and concrete experimental data. The modelling process can be roughly described as follows:

<p align="center">
  <img src="../main/Latex/workflow_2.jpg" />
</p>

 Mathematical modeling has been applied to biological systems for decades, but with respect to gene  expression, too few molecular components have been known to build useful, predictive models. There are many different modelling approaches and their number is still increasing. We can not conclude all in our lecture. We are here to discuss about mathematical modeling in biological system. The following models are studied in this project.
 
 * Central Dogma
 * Hill fucntion
 * Oscillating Gene Network
 * Gillespie Algorithm
 * Deterministics vs Stochastics Modeling
 
 # Central Dogma

Central dogma of molecular biology is an explanation of the flow of genetics information within a biological system.It is often stated as "DNA makes RNA and RNA makes proteins". The transfer of information from nucleic acid to nucleic acid ,or from nucleic acid to protein may be possible but transfer from protein to protein or from protein to nucleic acid is impossible. Information means here precise determination of sequence either of bases in the nucleic acid or of amino acid residue in protein.

The dogma is a framework for understanding the transfer of sequence information between information-carrying biopolymers in the most common or general case in living organism. There are 3 major classes of such biopolymers: DNA and RNA(both nucleic acids), and protein. There arew 3*3 = 9 conceivable direct transfer of information that can occur between these. The dogma classes these into 3 groups of 3:
* 3 general transfers(believed to occur normally in most cells),
* 3 special transfers(known to occur, but only under specific conditions in case of some viruses or in a laboratory),
* 3 unknown transfers(believed never to occur).

The general transfers describe the normal flow of biological information: DNA can be copied to DNA (DNA replication), DNA information can be copied into mRNA, (transcription), and proteins can be synthesized using the information in mRNA as a template (translation).

 The differential equation for model of central dogma:

$$\frac{dm}{dt} = k_{m} -\gamma_{m}*{m}$$

$$\frac{dp}{dt} = k_{p} * m -\gamma_{p}*{p}$$

where

* p is protein
* m is mRNA
* $k_{m}$ is the production rate for the mRNA
* $\gamma_{p}$ is the degradation rate of protein
* $k_{p}$ is the production rate for the proteins
* $\gamma_{m}$ is the degradation rate for mRNA

<p align="center">
  <img src="../main/Central_Dogma/centra_dogma_1.jpg" />
</p>


The above figure shows the relation between abundance of mRNA and protein over time.  Along the y-axis, we have the time axis and along x-axis we have abundance of both mRNA and protein. We observe that M(blue line) denotes mRNA in the above fig while P(red line) denotes protein.Both of them starts at zero and then they increases until they reach their steady state .The steady state for mRNA is 4 and for protein is 16 above. The abundance of protein is more than mRNA because it depends upon the mRNA production ( $k_{p} * m$ )while mRNA production is indepentent ($k_{m}$).


# Hill Function

The so called Hill Function were  introduced by A.V hill in 1910 to describe the binding of oxygen to hameoglobin. Subsequently,  they have been widely used in biochemistry, physicology and  mathematical modeling gene expression.

The Central Dogma of molecular Biology states that DNA makes and RNA makes proteins.The process by which DNA is copied to RNA is called transcription and by which RNA is used to produce protein is translation. The hill function is expressed as follow:
* Activation Hill Function 
* Repression Hill Function

## Activation Hill Function

In this  function Gene first ($G_{1}$) act as an activator  for Gene second($G_{2}$) and it increases the probablity of transcription often by increasing probability of RNA polymerase binding.

The differential equation for Activation Hil Function:
$$\frac{dG_1}{dt} = k_{1} - \gamma_{1}G_{1}$$
$$\frac{dG_2}{dt} = \left[\frac{G_{1}^{n}}{c^{n} + G_{1}^{n}}\right]k_{2} - \gamma_{2}G_{2}$$
Where
* $k_{1}$ is production rate of $G_{1}$
* $\gamma_{1}$ is degradation rate of $G_{1}$
* $k_{2}$ is production rate of $G_{2}$
* $\gamma_{2}$ is degradation rate of $G_{2}$
* c = constant
* n =  hill constant 
       
<p align="center">
  <img src="../main/Hill_function/Hill_function_Activation_1.jpg" />
</p>


The above figure shows the relation between Gene first ($G_{1}$) and Gene second($G_{2}$)  over time. Along the x-axis, we have the time axis and along y-axis we have number of Gene first ($G_{1}$) and Gene second$G_{2}$.  We observe that $G_{1}$(blue line) denotes Gene first in the above fig while $G_{2}$(red line) denotes Gene second. Here (($G_{1}$) quickly get activated and reaches to the steady point while $G_{2}$ delays. This is because for activating the $G_{2}$, $G_{1}$ should be produced.


## Repression Hill Function

In this  function Gene first ($G_{1}$) act as an repressor  for Gene second($G_{2}$) and it decreases the probablity of transcription often by decreasing probability of RNA polymerase binding.

The differential equation for Repression Hil Function:
$$\frac{dG_1}{dt} = k_{1} - \gamma_{1}G_{1}$$
$$\frac{dG_2}{dt} = [\frac{c^{n}}{c^{n} + G_{1}^{n}}]k_{2} - \gamma_{2}G_{2}$$
Where
* $k_{1}$ is production rate of $G_{1}$
* $\gamma_{1}$ is degradation rate of $G_{1}$
* $k_{2}$ is production rate of $G_{2}$
* $\gamma_{2}$ is degradation rate of $G_{2}$
* c = constant
* n =  hill constant 

<p align="center">
  <img src="../main/Hill_function/Hill_function_Repression_1.jpg" />
</p>


The above figure shows the relation between Gene first ($G_{1}$) and Gene second($G_{2}$)  over time. Along the x-axis, we have the time axis and along y-axis we have number of Gene first ($G_{1}$) and Gene second$G_{2}$.  We observe that $G_{1}$(blue line) denotes Gene first in the above fig while $G_{2}$(red line) denotes Gene second. Here (($G_{2}$) quickly get activated and reaches to the  peak point  but  $G_{1}$ protein start repressing it and suddenly it goes down . This show that $G_{1}$ act as repressor in this case.

# 0scillating Gene Model

Oscillating gene is a gene that is expressed in a rhythmic pattern or in periodic cycles.Oscillating genes are usually circadian and can be identified by periodic changes in the state of an organisms. Oscillating gene model is a complex gene network.

Same as above, the Central Dogma of molecular Biology states that DNA makes and RNA makes proteins.The process by which DNA is copied to RNA is called transcription and by which RNA is used to produce protein is translation.

For this model, let us consider Gene first as ($G_{1}$), Gene second as ( $G_{2}$) and Gene third($G_{3}$). $G_{1}$ activate the $G_{2}$ and facilitates the transcription of $G_{2}$ as a result $G_{2}$ get transcribed. It is positive interaction. $G_{2}$ does same for the $G_{3}$  and facilitates the transcription of $G_{3}$ as a result $G_{3}$ get transcribed.

But  $G_{3}$  comes back to repress the transcription of  $G_{1}$.  $G_{3}$ is inhibiting the expression by blocking the transcription of  $G_{1}$.It is known as negative feedback because it is cascading  $G_{1}$ being transcribed and then activating  $G_{2}$ which later transcribe and help in activating  $G_{3}$. But  $G_{3}$  is negatively feeding back. This cause oscillation during stimulation.

The differential equation for 0scillating Gene Model :
$$\frac{dG_1}{dt} = \left[\frac{c^{n}}{c^{n} + G_{3}^{n}}\right]k_{1} - \gamma_{1}G_{1}$$
$$\frac{dG_2}{dt} = \left[\frac{G_{1}^{n}}{c^{n} + G_{1}^{n}}\right]k_{2} - \gamma_{2}G_{2}$$
$$\frac{dG_3}{dt} = \left[\frac{G_{2}^{n}}{c^{n} + G_{2}^{n}}\right]k_{3} - \gamma_{3}G_{3}$$

Where
* $k_{1}$ is production rate of $G_{1}$
* $\gamma_{1}$ is degradation rate of $G_{1}$
* $k_{2}$ is production rate of $G_{2}$
* $\gamma_{2}$ is degradation rate of $G_{2}$
* $k_{3}$ is production rate of $G_{3}$
* $\gamma_{3}$ is degradation rate of $G_{3}$
* c = constant
* n =  hill constant 

<p align="center">
  <img src="../main/Oscillating_Gene_Network/Oscillating_Gene_Network_1.jpg" />
</p>

The above figure shows the relation between Gene first ($G_{1}$) , Gene second($G_{2}$) and Gene third($G_{3}$)  over time. Along the x-axis, we have the time axis and along y-axis we have number of Gene first ($G_{1}$), Gene second$G_{2}$ and Gene 3($G_{3}$).  We observe that $G_{1}$(blue line) denotes Gene first, $G_{2}$(red line) denotes Gene second and $G_{3}$(green line) denotes Gene third. In this figure we find oscillation with 3G network.Gene third $G_{3}$ is repressing $G_{1}$ which is negative feedback. Here $G_{1}$ is being produced that leads to $G_{2}$ production and $G_{2}$ is produced which leads to production of $G_{3}$. But $G_{3}$ produced stops $G_{1}$ from being produced. So that we get waves like this.      


# Gillespie Algoritm

The Gillespie Algoritm(or occasionally the Doob-Gillespie algorithm) generates a statistically correct trajectory(posssible solution) of a stochastic equation system for which the reaction rates are known. The algorithm was first presented by Doob in the mid 1940s. It was implented by Kendall in the 1950s. However it wasn't until the mid 1970s that Gillespie re-drived the method by studying physical systems that it became widely used. It is also sometime called as SSA method.

For this let consider a gene as x and some mRNA is transcribed from x with production rate k and it will be degraded with rate $\gamma_{x}$. For this list, all the rate in array as {r = [k , $\gamma_{x}$]}. For this let choose a time point of the reaction. If we are at time t which could be zero or can be any time between algorithm. Then next time is going to be t + $\tau$ . Here we choose $\tau $ from exponential random distribution with the parameter lambda  which is the sum of all rates at time t. After choosing the time point it is important to know whether it will be production of mRNa or breakdown of mRNA . The rate for breakdown depends on the current level of x. If there will be x zero than $\gamma_{x}$ will be zero and there will be only production. But suppose if we have couple of x with some positive number . So to choose the event going to happen we take random draw between two of them and weight the probabilities accordingly. Here probability of production of mRNA that means probability of x going to x + 1{ P( x$\rightarrow$ x + 1) = ($\frac{k}{sum(r)}$)} and probability of breaking down of mRNA isthat means probability of x - 1 { P( x$\rightarrow$ x - 1) = ($\frac{\gamma_{x}}{sum(r)}$)}.

The differential equation for this:
$$\frac{dx}{dt} = k - \gamma x $$

| Events                | Rates       |
| --------------------- | ----------- |
| x $\rightarrow$ x + 1 | k           |
| x $\rightarrow$ x - 1 | $\gamma x $ |

Where
* k is the production rate for mRNA
* $\gamma_{x}$ is the degradation rate for mRNA

<p align="center">
  <img src="../main/Gillespie_Algoritm/gillespie_algoritm_1.jpg" />
</p>

The above figures shows the relation between quantity of mRNA and protein over time.  Along the y-axis, we have the time axis and along x-axis we have abundance of both mRNA and protein. We observe that M(blue line) denotes quantity of  mRNA in the above fig. If we do the stimulation for hundred times or thousand times it will show average steady state near about 20 for above fig. Since it is stochastic model the steady state is not real because it is fluctuating near the steady state. 

# Deterministics vs Stochastics Modelings

Deterministics modeling allows us to calculate a future event exactly without the involvement of randomness. stochastics modeling allows us to calculate a future event exactly with the involvement of randomness. In determinstics there is each set of initial condition so there is only one trajectory. Through this model we get smooth curve. The difference with stochastics model is that stochastics model involves some random component.

The trajectory of deterministics modeling is compeletly defined by the initial parameters and conditions due to no involvement of randomness but in stochastics modeling with the same parameters and same initial conditions we get different tracjectories running at different times.

In computional biology one motive for using stochastics modeling is to calculate random variation in system which is not possible through determistics modelings. Here we will discuss about oscillating gene network same as above for stochastics modeling calculation.


The differential equation for Stochastics Modelings:
$$\frac{dG_1}{dt} = \left[\frac{c^{n}}{c^{n} + G_{3}^{n}}\right]k_{1} - \gamma_{1}G_{1}$$
$$\frac{dG_2}{dt} = \left[\frac{G_{1}^{n}}{c^{n} + G_{1}^{n}}\right]k_{2} - \gamma_{2}G_{2}$$
$$\frac{dG_3}{dt} = \left[\frac{G_{2}^{n}}{c^{n} + G_{2}^{n}}\right]k_{3} - \gamma_{3}G_{3}$$


| Events                           | Rates                                                      |
| -------------------------------- | ---------------------------------------------------------- |
| $$G_{1} \rightarrow G_{1} + 1$$  | $$\left[\frac{c^{n}}{c^{n} + G_{3}^{n}}\right]k_{1}$$      |
| $$G_{1} \rightarrow G_{1} - 1$$  | $$\gamma_{1} G_{1}$$                                       |
| $$G_{2} \rightarrow G_{2} + 1$$  | $$\left[\frac{G_{1}^{n}}{c^{n} + G_{1}^{n}}\right]k_{2}$$ |
| $$G_{2} \rightarrow G_{2} - 1$$  | $$\gamma_{2} G_{2}$$                                       |
| $$G_{3} \rightarrow G_{3} + 1$$  | $$\left[\frac{G_{2}^{n}}{c^{n} + G_{2}^{n}}\right]k_{3}$$ |
| $$G_{3} \rightarrow G_{3} - 1$$  | $$\gamma_{3} G_{3}$$                                       |


Where

* $k_{1}$ is production rate of $G_{1}$
* $\gamma_{1}$ is degradation rate of $G_{1}$
* $k_{2}$ is production rate of $G_{2}$
* $\gamma_{2}$ is degradation rate of $G_{2}$
* $k_{3}$ is production rate of $G_{3}$
* $\gamma_{3}$ is degradation rate of $G_{3}$
* c = constant
* n =  hill constant 


<p align="center">
  <img src="../main/Deterministic_vs_Stochastics_Modeling/Stochastic_Oscillator_1.jpg" />
</p>

The above figure shows the relation between Gene first ($G_{1}$) , Gene second($G_{2}$) and Gene third($G_{3}$)  over time. Along the x-axis, we have the time axis and along y-axis we have number of Gene first ($G_{1}$), Gene second$G_{2}$ and Gene 3($G_{3}$).  We observe that $G_{1}$(blue line) denotes Gene first, $G_{2}$(red line) denotes Gene second and $G_{3}$(green line) denotes Gene third. Each one have the oscillations but there is unevenly space because of the stochastic nature of this model. In compared to previous oscillator topic we did determistic ode model which was smooth but this is stochastic so they are still oscillating but it is much more random. 
