
### Descent Algorithm 

#### Todo

> [!NOTE] #question
> Look further into the cases like `(2,3,3,4), (1,3,4,4), (2, 2, 4, 4)` and try to explain/understand what is happening from the $n=3$ to $n=4$.  
> 
> Look at the coset representative and the action more carefully.  Esp in the toric case (permutahedron) case.


> [!NOTE] #question
> Look further into the banded cases, esp the highest root cases.  Is it possible to identify the orbits responsible for the $M^(n-1, 1)$ rep?
> Looking at the $n=4$ and the $degree = 3$ case seemed like it could be classified easier into trivial vs standard rep.   


> [!NOTE] #question
> Is there a version of the descent algorithm that removes by position instead of numbers?  
> Try looking at the sequence function and what if recording the increment at the values removed, but rather it is the positions that should be removed?

> [!NOTE] #todo
>
> Write down the details of Brosan Chow and Tymoczko paving paper to understand the combinatorial details.

> [!NOTE] #question
>
> Is it possible to do some manipulatorics with Forbenius reciprocity, Peri Rules, upper triangularity and the Gasharov tableaux to glean any insights?
 
#### Investigated

> [!NOTE] #question 
>    ##### In the remover function, what if instead of looking at the first valley, we look for the last valley?  Then we will be interested in the case where there is a climb or not.  
>
>  I looked into this and we run into issues looking backward from the last valley.  e.g. [5, 4, 3, 1, 2] or just [4, 3, 1, 2] the algorithm would not include the `5` in the former and `4` in the latter.   

> [!NOTE] #question
>
> Investigate surjectivity, or the back map of the descent algorithm.  Preliminary thoughts point to needing to understand:
> * what is the deal with climbs?
> * Is there some sort of statement on sequences of length k and d descents and uniqueness?
> 
> e.g. [1, 1, 0, 1, 1] deg = 2 is this unique?
> 
>I have looked at the uniqueness in some ways it is contingent on how precisely we start.  We can make a statment about it when the largest number N is required to begin or end the sequence.  If there is a statement that there is at most 1 valley -- and when no valleys then it is either the decreasing or increasing sequence.  The latter being the unique one with no descents -- to say this claim we need to know about climbs, because otherwise we can end with N more readily.  If no climbs, then there is a recursive/inductive argument at our disposal. 

>[!NOTE] #question
> 
> Does hanving the full inversion set make a perm trivial?
>
> No!  Look at `h=34555` and degree 2, there are 9 perms with full inversion set, but only 7 copies of the trivial





