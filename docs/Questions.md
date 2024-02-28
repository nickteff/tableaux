
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

#### Investigated

> [!NOTE] #question 
>    ##### In the remover function, what if instead of looking at the first valley, we look for the last valley?  Then we will be interested in the case where there is a climb or not.  
>
>  I looked into this and we run into issues looking backward from the last valley.  e.g. [5, 4, 3, 1, 2] or just [4, 3, 1, 2] the algorithm would not include the `5` in the former and `4` in the latter.   






