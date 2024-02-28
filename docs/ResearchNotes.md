
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

