#include <iostream>
using namespace std;

void queue_updation(int queue[], int timer, int arrival[], int n, int max_process_idx)
{
    int zero_idx;
    for (int i = 0; i < n; i++)
    {
        if (queue[i] == 0)
        {
            zero_idx = i;
            break;
        }
    }
    queue[zero_idx] = max_process_idx + 1;
}

void queue_maintenance(int queue[], int n)
{
    for (int i = 0; (i < n - 1) && (queue[i + 1] != 0); i++)
    {
        int temp = queue[i];
        queue[i] = queue[i + 1];
        queue[i + 1] = temp;
    }
}

void check_new_arrival(int timer, int arrival[], int n, int max_process_idx, int queue[])
{
    if (timer <= arrival[n - 1])
    {
        bool new_arrival = false;
        for (int j = (max_process_idx + 1); j < n; j++)
        {
            if (arrival[j] <= timer)
            {
                if (max_process_idx < j)
                {
                    max_process_idx = j;
                    new_arrival = true;
                }
            }
        }

        if (new_arrival)
            queue_updation(queue, timer, arrival, n, max_process_idx);
    }
}

int main()
{
    int n, tq, timer = 0, max_process_idx = 0;
    float total_wt = 0, total_tat = 0;
    cout << "\nEnter the time quantum: ";
    cin >> tq;
    cout << "Enter the no. of processes: ";
    cin >> n;
    int at[n], bt[n], wt[n], tat[n], queue[n], temp_burst[n];
    bool complete[n];

    cout << "Enter the arrival time of the processes: ";
    for (int i = 0; i < n; i++)
        cin >> at[i];

    cout << "Enter the burst time of the processes: ";
    for (int i = 0; i < n; i++)
    {
        cin >> bt[i];
        temp_burst[i] = bt[i];
    }

    for (int i = 0; i < n; i++)
    {
        complete[i] = false;
        queue[i] = 0;
    }

    while (timer < at[0])
        timer++;
    queue[0] = 1;

    while (true)
    {
        bool flag = true;
        for (int i = 0; i < n; i++)
        {
            if (temp_burst[i] != 0)
            {
                flag = false;
                break;
            }
        }
        if (flag)
            break;

        for (int i = 0; (i < n) && (queue[i] != 0); i++)
        {
            int ctr = 0;
            while ((ctr < tq) && (temp_burst[queue[0] - 1] > 0))
            {
                temp_burst[queue[0] - 1] -= 1;
                timer += 1;
                ctr++;

                check_new_arrival(timer, at, n, max_process_idx, queue);
            }

            if ((temp_burst[queue[0] - 1] == 0) && (complete[queue[0] - 1] == false))
            {
                tat[queue[0] - 1] = timer;
                complete[queue[0] - 1] = true;
            }

            bool idle = true;
            if (queue[n - 1] == 0)
            {
                for (int i = 0; i < n && queue[i] != 0; i++)
                {
                    if (complete[queue[i] - 1] == false)
                    {
                        idle = false;
                    }
                }
            }
            else
                idle = false;

            if (idle)
            {
                timer++;
                check_new_arrival(timer, at, n, max_process_idx, queue);
            }

            queue_maintenance(queue, n);
        }
    }

    for (int i = 0; i < n; i++)
    {
        tat[i] = tat[i] - at[i];
        wt[i] = tat[i] - bt[i];
    }

    for (int i = 0; i < n; i++)
    {
        total_wt += wt[i];
        total_tat += tat[i];
    }
    cout << "\nAverage Waiting Time : " << (total_wt / n)
         << "\nAverage Turn Around Time : " << (total_tat / n);

    return 0;
}