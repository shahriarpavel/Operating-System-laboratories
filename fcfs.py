from __future__ import print_function

n = int(input("Enter the number of processes: "))

pro = []

for i in range(n):
    p = input(f"Enter Process Name (P{i+1}): ")
    at = int(input(f"Enter Arrival Time of {p}: "))
    bt = int(input(f"Enter Burst Time of {p}: "))
    pro.append([p, at, bt])

pro.sort(key=lambda x:x[1])
print(pro)

ct = 0 
total_tat=0
total_wt = 0
for i in pro:

  if ct < i[1]:
    ct = i[1]

  ct+=i[2]

  i.append(ct)
  i.append(ct-i[1])
  i.append(i[4]-i[2])
  total_tat+=i[4]
  total_wt+=i[5]

avg_tat = total_tat/len(pro)
avg_wt = total_wt/len(pro)

print(f"Process\tAT\tBT\tCT\tTAT\tWT")
for i in pro:
  print(i)

print(avg_tat)
print(avg_wt)
