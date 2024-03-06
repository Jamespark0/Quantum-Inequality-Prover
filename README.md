<div align="center"> 
    <center><h1>Quantum Information Theoretic Inequality Prover (Quantum ITIP)</h1></center> 
    </div>
     <br/> 
<div align="center">
An information prover dedicated to quantum information theory.
</div>

---

## What is Quantum ITIP?
Quantum ITIP automatically proves if a quantum information inequality can be derived from strong subadditivity and weak monotonicity in quantum information theory. If this is the case, this prover generates a set of inequalities that can be used to prove the inequality; otherwise, it generates a set of inequalities to help build a counterexample to "disprove" the inequality . Note that a counterexample may not be found due to the nature of quantum information inequality.

## Features
1. The inequality to be proved can have additional constraints imposed by the user.
2. The prover helps prove and disprove the given inequality.

## Usages
### Initialization:
Before entering the main page, the prover asks the number of quantum systems to be worked with. Enter an integer greater than 2.
![init-example](https://imgur.com/a/fVanb9X)

## Credits
This work is inspired by the classical ITIP formulated by Siu Wai Ho, Alex Lin Ling, Chee Wei Tan and Raymond Yeung. More information can be found from [the AITIP website](https://aitip.org).

## Warning
This is a master-thesis project, and still has a lot of rooms for improvements.