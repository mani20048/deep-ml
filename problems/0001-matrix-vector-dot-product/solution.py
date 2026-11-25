def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    res = []
    if len(a[0])==len(b):
        for i in range(len(a)):
            summ = 0
            for j in range(len(a[0])):
                prod = a[i][j]*b[j]
                summ = summ+prod
            res.append(summ)   
    else:
        return -1
    
    return res
    