
## 2024-02-20

Today I started working on setting up the gasharov tableaux in order to compare the values as h changes by and index, partition etc...

* A Gasharov is implemented
* A new  [[Tableau]] class is created to encapsulate some tableau methods
	* it is just inherits from List
* []


## 2024-02-22

I spent time writing the overview, specifically adding notes on the descent algorith.  Editing this opened a question about looking at the last valley instead of the first valley.  This wasn't too fruitful as it pushes the complexity earlier in the permutation.  

## 2024-02-23

Spent time investigating how the allowable descents/inversions evolve as the h function changes.  Have some leads on looking at the disconnected cases we know lifted from $n --> n+1$, or the banded examples --> esp the highest root case.

I have a vague idea of a "super" permutation rep.  Look at the toric case and $n=3$. The four permutations in degree 1 look the same but are like rotated around.  

## 2024-02-24

Today was spent cleaning and improving the repo.  I figured out how to improve the search functionality on the html output files.  This will aid looking for patterns in the descents by `desc` etc...

I also improved the directory structure and want to improve `README.md` so it would be easier to share the code.  

## 2024-02-27

Continued looking at the highest root repn.  A vague idea around looking at the longest roots allowed and marking descents by that:  e.g for n = 4 and d = 3, then 
$w \in \{ (1, 4, 3, 2), (2, 4, 3, 1), (3, 2, 1, 4), (4,2, 1, 3)\}$ to be in an orbit.  While for example w = (3, 4, 1, 2) is fixed because 3 > 1, 4 > 2, but 4 > 1, so they are connected.  While a connection cannot be made in the set identified...  still vague.  e.g  1, 2, 4, 3 are all left out.  
For n = 5 d = 6 then the set $\{(15432), (25431), (43215), (53214), [(51432) or (35241)]\}$ is an orbit and 1, 2, 5, 4, (5 or 3).  I like the second because of the identifcation of 1,2,3,4,5, but...

Added a `docs` directory to keep my notes here

## 2024-02-28

A little more clean up of the docs and merged into main.

Looking at just the banded type and looking for examples of $M^{[n-1, 1]}$, developing this thought around looking at `blocks`, `connections` in the permutation patterns.  Right now if I look at the longest `h-descent` root, inversion (in the banded type it a unique answer) you can begin to group the numbers together by those that are reached by the descent or something.  

I may need to build the web app in order to look at $n > 7$...

Looking further into the Brosan-Chow paper along with JT's Linear Conditions paper.  Theorem 127 and Eqn 128 are the main result.  I still need to more carefully understand how JT's tableaux and the Brosan-Chow result combine.  It seems there is a connection to be made back to Gasharov tableaux.

## 2024-02-29

I determined I need a way to filter the `h_map` files by h_function and degree and I want a function that will generate the q_polys in the `S` and `M` representation bases, so I will also want a function that generates a vector of `S` by (partition, degree, count) and a function the calculates the inverse Kostka matrix (I know! an inverse)

```python
import numpy as np
def Kn(n): return np.array(K(n))
def Kn_inv(n): return np.linalg.inv(Kn(n))
```
This is Copilots first attempt -- needs some work -- the P_inv function returns a list of tuples, so needs a fix
```python
from algo.partitions import partitions, gasharov, P_inv

def count_gasharov_tableaux(n, h):
    counts = {}
    for partition in partitions(n):
        tableaux = gasharov(partition, h)
        for tableau in tableaux:
            degree = P_inv(tableau)
            key = (tuple(partition), degree)
            if key in counts:
                counts[key] += 1
            else:
                counts[key] = 1
    return counts
```
