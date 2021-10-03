def waiting_time(processes, n, wt):
    rt = [0] * n

    for i in range(n):
        rt[i] = processes[i][1]

    complete = 0
    t = 0
    mini = 999999999
    short = 0
    check = False

    while (complete != n):

        for j in range(n):
            if ((processes[j][2] <= t) and
                    (rt[j] < mini) and rt[j] > 0):
                mini = rt[j]
                short = j
                check = True

        if (check == False):
            t += 1
            continue

        rt[short] -= 1

        mini = rt[short]
        if (mini == 0):
            mini = 999999999

        if (rt[short] == 0):

            complete += 1
            check = False

            fint = t + 1

            wt[short] = (fint - processes[short][1] - processes[short][2])

            if (wt[short] < 0):
                wt[short] = 0

        t += 1


def turn_around_time(processes, n, wt, tat):

    for i in range(n):
        tat[i] = processes[i][1] + wt[i]


def avg_time(processes, n):
    wt = [0] * n
    tat = [0] * n

    waiting_time(processes, n, wt)
    turn_around_time(processes, n, wt, tat)

    total_wt = 0
    total_tat = 0

    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]

    print("Average Waiting Time = {:.2f}".format(total_wt / n))
    print("Average Turn Around Time = {:.2f}".format(total_tat / n))

processes = [[1, 6, 1], [2, 8, 1], [3, 7, 2], [4, 3, 3]]
n = 4
avg_time(processes, n)
