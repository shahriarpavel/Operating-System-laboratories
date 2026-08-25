n = int(input("Enter number of processes: "))

processes = []
for i in range(n):
    at = int(input(f"Enter Arrival Time for P{i+1}: "))
    bt = int(input(f"Enter Burst Time for P{i+1}: "))
    processes.append([i+1, at, bt])


processes.sort(key=lambda x: x[1])

time = 0
completed = 0
n = len(processes)
visited = [False] * n
ct = [0] * n
tat = [0] * n
wt = [0] * n
gantt = []

while completed < n:

    id = -1
    min_bt = float('inf')

    for i in range(n):
        if not visited[i] and processes[i][1] <= time:
            if processes[i][2] < min_bt:
                min_bt = processes[i][2]
                id = i

    if id == -1:
        if not gantt or gantt[-1][0] != "Idle":
            gantt.append(["Idle", time, time+1])
        else:
            gantt[-1][2] = time + 1
        time += 1
        continue

    visited[id] = True
    start = time
    time += processes[id][2]
    end = time

    if gantt and gantt[-1][0] == f"P{processes[id][0]}":
        gantt[-1][2] = end
    else:
        gantt.append([f"P{processes[id][0]}", start, end])


    ct[id] = time
    tat[id] = ct[id] - processes[id][1]
    wt[id] = tat[id] - processes[id][2]


    if wt[id] < 0:
        wt[id] = 0

    completed += 1

print("\n--- Gantt Chart ---")
for g in gantt:
    print(f"{g[0]} : {g[1]} - {g[2]}")

print("\nProcess\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"P{processes[i][0]}\t{processes[i][1]}\t{processes[i][2]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")

avg_tat = sum(tat) / n
avg_wt = sum(wt) / n
print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
print(f"Average Waiting Time: {avg_wt:.2f}")
