<div align="center"> 
    <center><h1>Quantum Information Theoretic Inequality Prover (Quantum ITIP)</h1></center> 
    </div>
     <br/> 
<div align="center">
An information prover dedicated to quantum information theory.
</div>

---

## What is Quantum ITIP?
Quantum ITIP automatically proves if a quantum information inequality can be derived from strong subadditivity and weak monotonicity in quantum information theory. If this is the case, this prover generates a set of inequalities that can be used to prove the inequality; otherwise, it generates a set of inequalities to help build a counterexample to "disprove" the inequality. Note that a counterexample may not be found due to the nature of quantum information inequality.

## Features
1. The inequality to be proved can have additional constraints imposed by the user.
2. The prover helps prove and disprove the given inequality.

## Usages
### Initialization:
Before entering the main page, the prover asks the number of quantum systems to be worked with. Enter an integer greater than 2. For example, if we are to work with 4 quantum systems:

![init](https://imgur.com/TOzrWY2.png)

### Choose actions:
The homepage shows a list of actions that a user can choose from:

1. add/update an inequality
2. impose a constraint on the inequality
3. clear all constraints
4. check if the inequality is von-Neumann type
5. end the prover

![homepage](https://imgur.com/oQDe4Ju.png)
The action is activated by typing in the index next to the action. For example, 

`Pick an action: 1` prompts the user to add or update the inequality to be proved.

`Pick an action: q` ends the prover.

#### Add inequality:
![add\update inequality](https://imgur.com/8i5FcVY.png)
The inequality should be expressed in terms of the marginal entropies, and takes the form:

`[A linear combination of marginal entropis] >= 0`

 To assign the coefficient value for a certain marginal entropy, the indices of the systems in the marginal entropy is separated by spaces, and the assignment is followed by '->'.

`[indices of the systems] -> [coefficient value]`

If the inequality has more than one coefficient to assign (which is often the case), each assignment is separated by ';'. Those coefficients not specified by the user will be set to $0$.

For example, if the inequality to be checked is 
```math
I(1;2\mid 3) = S(1, 3) + S(2, 3) - S(1,2,3) - S(3) \geq 0,
```

one should input something like:

`1 3 -> 1; 2 3 -> 1; 1 2 3 -> -1; 3 -> -1`

where the order does not matter.

#### Add one constraint:
This prover current allows only adding **one equality constraint** at a time. The constraint is expressed in the form of marginal entropies just like the inequality to be proved, and the equality constraint takes the form:

`[linear combination of marginal entropies] = 0`.

The way to assign the coefficients in the constraint is identical to assigning the coefficients in the inequality.

![add one constraint](https://imgur.com/TFT9vUE.png)

#### Clear constraints:
This clears all the constraints provided by the user. 

#### Check von-Neumann type:
By choosing this functionality, the prover check if the given inequality, under the imposed constraints, can be derived from strong sub-additivity and weak monotonicity. The program returns one of the two possible outcomes:

1. `It's von-Neumann type!` The prover shows how to construct the inequality from strong subadditivity and from weak monotonicity altogether.
2. `It's not provable by Quantum ITIP :(` This indicates that the inequality cannot be derived from strong subadditivity and from weak monotonicity. It also generates a list of **equalities** that the counterexample can satisfy. Note that the hints provided by the prover is a sufficient condition not a necessary condition.

For example, 
1. The non-negativity of quantum entropy. Let's say to prove the marginal entropy $S(1)$ which indicates the quantum entropy of system $1$ is non-negative, the prover generates the following result
![non-negativity of quantum entropy](https://imgur.com/BrXJBBb.png)
2. Conditional entropy can be negative in quantum information theory. If we are to show $S(1\mid 2) \geq 0$ cannot be derived from strong subadditivity and weak monotonicity, the prover suggests the following result to disprove the inequality
![negativity of conditional entropy](https://imgur.com/Q6ovlmk.png)

#### End prover:
This terminates the program.

## Credits
This work is inspired by the classical ITIP formulated by Siu Wai Ho, Alex Lin Ling, Chee Wei Tan and Raymond Yeung. More information can be found from [the AITIP website](https://aitip.org).

## Warning
This is a master-thesis project, and still has a lot of rooms for improvements.