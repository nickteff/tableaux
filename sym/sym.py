# %%
import numpy as np


def inverse_from_word(w):
    w = np.array(w)
    return np.array([(np.where(w == i)[0]).item() for i in range(len(w))])


def matrix_from_word(w):
    n = len(w)
    M = np.zeros(shape=(n, n))

    for i in range(n):
        M[w[i], i] = 1

    return M


def word_from_matrix(M):
    return np.array([np.where(M[:, i] == 1)[0].item() for i in range(M.shape[0])])


def gen(i, n):
    if n < 1:
        raise Exception('n must a positive integer')
    if i < 1 or i > n - 2:
        raise Exception("i must be between 1 and n-1")
    i -= 1
    col = np.arange(n)
    col[i:i + 2] = [i + 1, i]
    return matrix_from_word(col)

class SymmetricGroup(object):
    pass

class Permutation(object):
    def __init__(self, word):
        self.word = np.array(word)
        self._matrix = matrix_from_word(word)
        self.n = len(self.word)
        self._inverse = inverse_from_word(self.word)

    def __mul__(self, v):
         m = np.array([v.word[self.word[i]] for i in range(self.n)])
         return m

    def power(self, n: int):
        matrix = np.linalg.matrix_power(w._matrix, n)
        word = word_from_matrix(matrix)
        return word

    def inverse(self):
         return self._inverse

# %%


w = Permutation([2, 0, 3, 1])

print(w._matrix)
print(w.word)
print(w.n)
print(w._inverse)
v = (w * w)
print(w.power(2))
print(w.inverse())
# %%

v  = Permutation(w*w)

v.inverse()
# %%

w = Permutation(np.random.permutation(range(3)))

print(w.word)
print(w._matrix)
print()


