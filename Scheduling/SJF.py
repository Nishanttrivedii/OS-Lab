def arrange_at(n, mat):
    for i in range(0, n):
        for j in range(i, n-i-1):
            if mat[1][j] > mat[1][j+1]:
                for k in range(0, n):
                    mat[k][j], mat[k][j+1] = mat[k][j+1], mat[k][j]


def completion_time(n, mat):
    value = 0
    mat[3][0] = mat[1][0] + mat[2][0]
    mat[5][0] = mat[3][0] - mat[1][0]
    mat[4][0] = mat[5][0] - mat[2][0]

    for i in range(1, n):
        temp = mat[3][i-1]
        mini = mat[2][i]

        for j in range(i, n):
            if temp >= mat[1][j] and mini >= mat[2][j]:
                mini = mat[2][j]
                value = j

        mat[3][value] = temp + mat[2][value]
        mat[5][value] = mat[3][value] - mat[1][value]
        mat[4][value] = mat[5][value] - mat[2][value]

        for k in range(0, 6):
            mat[k][value], mat[k][i] = mat[k][i], mat[k][value]


n = 4
lst = [[int(i) for i in range(1, n+1)], [2, 0, 4, 5],
       [3, 4, 2, 4], [0]*n, [0]*n, [0]*n]

arrange_at(n, lst)
completion_time(n, lst)

total_wt = 0
total_tat = 0

for i in range(0, n):
    total_wt += lst[4][i]
    total_tat += lst[5][i]

print("Average Waiting Time = ", (total_wt/n))
print("Average Turn Around Time = ", (total_tat/n))
