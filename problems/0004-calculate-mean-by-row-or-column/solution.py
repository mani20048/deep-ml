def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    means= []
    if mode=='column':
        for j in range(len(matrix[0])):
            summ = 0
            for i in range(len(matrix)):
                summ += matrix[i][j]
            m = summ/len(matrix)
            means.append(m)
    else:
        for i in range(len(matrix)):
            summ = 0
            for j in range(len(matrix[0])):
                summ += matrix[i][j]
            m = summ/len(matrix[0])
            means.append(m)
    return means