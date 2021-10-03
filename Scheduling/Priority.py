def waiting_time(wt):
    service = [0] * 5
    service[0] = 0
    wt[0] = 0

    for i in range(1, n):
        service[i] = processes[i - 1][1] + service[i - 1]
        wt[i] = service[i] - processes[i][0] + 1

        if(wt[i] < 0):
            wt[i] = 0


def turn_around_time(tat, wt):
    for i in range(n):
        tat[i] = processes[i][1] + wt[i]


def avg_time():
    wt = [0] * 5
    tat = [0] * 5

    total_wt = 0
    total_tat = 0

    waiting_time(wt)
    turn_around_time(tat, wt)

    stime = [0] * 5
    ctime = [0] * 5
    stime[0] = 1
    ctime[0] = stime[0] + tat[0]

    for i in range(1, n):
        stime[i] = ctime[i - 1]
        ctime[i] = stime[i] + tat[i] - wt[i]

    for i in range(n):
        total_wt += wt[i]
        total_tat += tat[i]

    print("Average Waiting Time = {:.2f}".format(total_wt / n))
    print("Average Turn Around Time = {:.2f}".format(total_tat / n))


n = 5
processes = [[0]*4]*5
at = [1, 2, 3, 4, 5]
bt = [3, 5, 1, 7, 4]
priority = [3, 4, 1, 7, 8]

for i in range(n):
    processes[i][0] = at[i]
    processes[i][1] = bt[i]
    processes[i][2] = priority[i]
    processes[i][3] = i + 1

processes = sorted(processes, key=lambda x: x[2])
processes = sorted(processes)

avg_time()
