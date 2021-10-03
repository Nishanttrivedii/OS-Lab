def waiting_time(wt, bt, n):
    for i in range(1, n):
        wt[i] = bt[i-1] + wt[i-1]


def turn_around_time(wt, bt, tat, n):
    for i in range(n):
        tat[i] = wt[i] + bt[i]


def avg_time(bt, n):
    wt = [0]*5
    tat = [0]*5
    total_wt = 0
    total_tat = 0

    waiting_time(wt, bt, n)
    turn_around_time(wt, bt, tat, n)

    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]

    print("Average Waiting Time = ", total_wt/n)
    print("Average Turn Around Time = ", total_tat/n)


bt = [4, 7, 3, 2]
n = 4

avg_time(bt, n)
