import numpy as np


A = [[2, 0, -3], [1, 4, 5]]
B = [[3, 1], [-1, 0], [4, 2]]
C = [[4, 7], [2, 1], [1, -1]]

# Sesuai dengan yang disuruh oleh tugas, ini adalah bagian kode yg non library untuk perkalian matriks manual
def matrix_multiply_manual(mat1, mat2):
    result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result

def matrix_add_manual(mat1, mat2):
    result = [[0 for _ in range(len(mat1[0]))] for _ in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            result[i][j] = mat1[i][j] + mat2[i][j]
    return result

# if untuk metode
def calculate_result(A, B, C, method="numpy"):
    if method == "manual":
        
        AB = matrix_multiply_manual(A, B)
        AC = matrix_multiply_manual(A, C)
        result = matrix_add_manual(AB, AC)
    elif method == "numpy":
       
        A_np = np.array(A)
        B_np = np.array(B)
        C_np = np.array(C)
        AB = np.dot(A_np, B_np)
        AC = np.dot(A_np, C_np)
        result = AB + AC
    else:
        raise ValueError("Method hanya bisa antara 'manual' atau 'numpy'")
    
    return result


result_manual = calculate_result(A, B, C, method="manual")
print("Hasil AB + AC (manual):")
print(result_manual)


result_numpy = calculate_result(A, B, C, method="numpy")
print("\nHasil AB + AC (numpy):")
print(result_numpy)
