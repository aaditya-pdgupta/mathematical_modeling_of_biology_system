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



