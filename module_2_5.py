def get_matrix(n, m, value):
    matrix = []

    for i in range(n):
        row = []
        for j in range(m):
            row.append(value)
        matrix.append(row)

    return matrix
result = get_matrix(5, 3, 6)
print(result)