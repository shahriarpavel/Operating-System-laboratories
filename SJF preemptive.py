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
remaining = [p[2] for p in processes]
ct = [0] * n
tat = [0] * n
wt = [0] * n
gantt = []
prev_pid = -1
start_time = 0

while completed < n:
    idx = -1
    min_rem = float('inf')
    for i in range(n):
        if processes[i][1] <= time and remaining[i] > 0:
            if remaining[i] < min_rem:
                min_rem = remaining[i]
                idx = i

    if idx == -1:
        if not gantt or gantt[-1][0] != "Idle":
            gantt.append(["Idle", time, time+1])
        else:
            gantt[-1][2] = time + 1
        time += 1
        continue

    if prev_pid != idx:
        if prev_pid != -1:
            gantt.append([f"P{processes[prev_pid][0]}", start_time, time])
        prev_pid = idx
        start_time = time

    remaining[idx] -= 1
    time += 1

    if remaining[idx] == 0:
        ct[idx] = time
        tat[idx] = ct[idx] - processes[idx][1]
        wt[idx] = tat[idx] - processes[idx][2]
        if wt[idx] < 0:
            wt[idx] = 0
        completed += 1
        if prev_pid == idx:
            gantt.append([f"P{processes[idx][0]}", start_time, time])
            prev_pid = -1

print("\n--- Gantt Chart ---")
for g in gantt:
    print(f"{g[0]} : {g[1]} - {g[2]}")

print("\nProcess\tAT\tBT\tCT\tTAT\tWT")
for i in sorted(range(n), key=lambda x: processes[x][0]):
    print(f"P{processes[i][0]}\t{processes[i][1]}\t{processes[i][2]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")

avg_tat = sum(tat) / n
avg_wt = sum(wt) / n
print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
print(f"Average Waiting Time: {avg_wt:.2f}")
