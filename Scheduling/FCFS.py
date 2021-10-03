def waiting_time(processes, n, bt, wt, at):
    service_time = [0] * n
    service_time[0] = 0
    wt[0] = 0

    for i in range(1, n):
        service_time[i] = (service_time[i - 1] +
                           bt[i - 1])
        wt[i] = service_time[i] - at[i]
        if (wt[i] < 0):
            wt[i] = 0


def turn_around_time(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]


def avg_time(processes, n, bt, at):
    wt = [0] * n
    tat = [0] * n

    waiting_time(processes, n, bt, wt, at)
    turn_around_time(processes, n, bt, wt, tat)

    total_wt = 0
    total_tat = 0
    for i in range(n):

        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]

    print("Average Waiting Time = {:.2f}".format(total_wt / n))
    print("Average Turn Around Time = {:.2f}".format(total_tat / n))


processes = [1, 2, 3]
bt = [5, 9, 6]
at = [0, 3, 6]
n = 3

avg_time(processes, n, bt, at)
