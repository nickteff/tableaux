# Tableaux Notes

Welcome to my notes on the [Stanley-Stembridge conjecture](../docs/Stanley-Stembridge/Stanley-StembridgeConjecture.md). I'm working on showing that a set of [Representations of the Symmetric Group](../docs/RepTheory/RepsOfSn.md) are actually permutation representations. The conjecture itself is about the $e$-positivity of a family of (*quasi*)symmetric functions.

I'm building on the work of Stembridge, specifically his results in [Eulerian numbers, tableaux, and the Betti numbers of a toric variety](https://www.sciencedirect.com/science/article/pii/0012365X9290378S?ref=pdf_download&fr=RR-2&rr=8591a837785f26bb). His approach involves a combinatorial construction of the permutation representation, and I'm trying to extend that.

My goal is to adapt Stembridge's algorithm and see if I can make it work for all the cases that interest me.

My first step is to create an adaptation of Stembridge's algorithm. In his paper, he links the [excedances](/docs/Permutations/PermutationStatistics.md#excedances) of the permutations to the [Eulerian Numbers](/docs/Permutations/PermutationStatistics.md#eulerian-numbers). I'd like to frame this result in terms of [descents](/docs/Permutations/PermutationStatistics.md#descents) instead, because from my dissertation, the representation of interest has a clear definition in terms of descents and [inversions](/docs/Permutations/PermutationStatistics.md#inversions).

I have got a first draft of this algorithm, which I'm calling the [Descent Algorithm](../docs/DescentAlgorithm.md#descent-algo). This function maps a permutation to one of Stembridge's `marked codes`. So far, it looks like this function is bijective for $n \le 11$.
