import numpy as np


A = np.array([[2, 0, -3], [1, 4, 5]])
B = np.array([[3, 1], [-1, 0], [4, 2]])
C = np.array([[4, 7], [2, 1], [1, -1]])


AB = np.dot(A, B)
AC = np.dot(A, C)


result = AB + AC

print("Matriks AB:")
print(AB)
print("\nMatriks AC:")
print(AC)
print("\nHasil AB + AC:")
print(result)
