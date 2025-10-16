# Mamy plansze m x n z pionkiem w lewym gornym rogu oraz mete w prawym dolnym rogu
# Na ile sposobow mozemy dotrzec na mete jesli pionek moze poruszac sie tyko w prawo lub w dol?

def unique_paths_problem(m, n):
    row = [1] * n

    for i in range(m - 1):
        newRow = [1] * n
        for j in range(n - 2, -1, -1):
            newRow[j] = newRow[j + 1] + row[j]
        row = newRow
    return row[0]

# m - kolumny, n - wiersze
def unique_paths_problem_mine(m, n):
    arr = [[0 for a in range(m + 1)] for b in range(n + 1)]
    arr[m][n] = 1

    for i in range(m, -1, -1):
        for j in range(n, -1, -1):
            arr[i][j] = arr[i+1][j] + arr[i][j+1]

    return arr[0][0]
