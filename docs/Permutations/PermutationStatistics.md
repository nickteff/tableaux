$[n] := \{ 1, 2, \cdots, n \} \subset \mathbb{N}$

##### Descents
Given a permutation $w \in \mathfrak{S}_n$ a *descent* is an instance where $w(i) > w(i+1)$ for $i \in [n]$

Let $desc(w) := \\#  \\{i \in [n-1] : w(i) > w(i+1)\\}$

##### Eulerian Numbers
For each $i \in \mathbb{N}$, then the *Eulerian Numbers* are  $A_n(i) := \\# \\{ w \in \mathfrak{S}_n : exc(w) = i\\}$.  Recall $exc(w)$ is the number of [excedances](../docs/Permutations/PermutationStatistics.md#excedances) of the permutation $w$.

##### Excedances 
Given a permutation $w \in \mathfrak{S}_n$ an *excedance* is an instance where $w(i) > i$ for $i \in [n]$

Let $exc(w) := \\# \\{ i \in [n] : w(i) > i \\}$

##### Inversion
Given a permutation $w \in \mathfrak{S}_n$ an *inversion* is an instance where $i < j$ and $w(i) > w(j)$ for $i, j \in [n]$.  Note that every [descent](../docs/Permutations/PermutationStatistics.md#descents) is an inversion.

Let  $inv(w) := \\#\\{(i, j) \in [n]\times[n] : i < j \ \\& \ w(i) > w(j)\\}$
