#Tableau MOC

This MOC will help me organize my work on the [Stanley-Stembridge conjecture](docs/Stanley-Stembridge/Stanley-Stembridge conjecture.md).  How I look at this problem involves showing that a family of [[Representations of the Symmetric Group]] are in fact permutation representations.  As stated the conjecture involves $e$-positivity of a family of (*quasi*)symmetric functions.  

The approach I have been developing is an attempt to extend the results of Stembridge found in [Eulerian numbers, tableaux, and the Betti numbers of a toric variety](https://www.sciencedirect.com/science/article/pii/0012365X9290378S?ref=pdf_download&fr=RR-2&rr=8591a837785f26bb).  This is a purely combinatorial construction of the permutation representation that relies of showing certain generating functions of symmetric functions coincide to prove that this is the representation of interest.  

I am looking to adapt Stembridge's algorithm from the paper linked above and then see if there is a way to generalize it to all of the cases I am interested in.  

The first step involves building an adaptation of Stembridge's algorithm.  In his paper, he connects the [[Permutation Statistics#Excedances| excedances]] of the permutations to the [[Permutation Statistics#Eulerian Numbers|Eularian Numbers]].  I would rather see this result framed in terms of [[Permutation Statistics#Descents| descents]].  The reason being that from my dissertation the representation in interest has a nice definition in terms of descents and [[Permutation Statistics#Inversion|inversions]].

I have a first draft of such an algorithm that I'll call the [[Descent Algorithm#Descent Algo| Descent Algorithm]].  This function takes a permutation and maps it to one of Stembridge's `marked codes`.  So far I have verified that this function is bijective for $n \le 11$.  





