import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    t = -(matrix[0][0]+matrix[1][1])
    d = (matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0])
    eigenvalues = []

    l1 = -(t)+np.sqrt(t**2-(4*1*d))# lambda = -b+- sqrt(b**2-4ac)/2a  a=1,b=t,c=d
    l2 = -(t)-np.sqrt(t**2-(4*1*d))
    eigenvalues.append(l1/2)
    eigenvalues.append(l2/2)
    return eigenvalues