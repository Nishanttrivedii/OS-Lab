def waiting_time(processes, n, bt, wt, tq):
    rem_bt = [0] * n

    for i in range(n):
        rem_bt[i] = bt[i]
    t = 0

    while True:
        done = True

        for i in range(n):
            if (rem_bt[i] > 0):
                done = False

                if (rem_bt[i] > tq):
                    t += tq
                    rem_bt[i] -= tq

                else:
                    t = t + rem_bt[i]
                    wt[i] = t - bt[i]
                    rem_bt[i] = 0

        if (done == True):
            break


def turn_around_time(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]


def avg_time(processes, n, bt, tq):
    wt = [0] * n
    tat = [0] * n

    waiting_time(processes, n, bt, wt, tq)
    turn_around_time(processes, n, bt, wt, tat)

    total_wt = 0
    total_tat = 0

    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]

    print("Average Waiting Time = {:.2f}".format(total_wt / n))
    print("Average Turn Around Time = {:.2f}".format(total_tat / n))


processes = [1, 2, 3]
bt = [10, 5, 8]
n = 3
tq = 2

avg_time(processes, n, bt, tq)
