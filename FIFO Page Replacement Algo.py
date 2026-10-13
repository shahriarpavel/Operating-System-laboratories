pages = list(map(int, input("Enter the reference pages string: ").split()))
frame = int(input("Enter the number of frame: "))

frames = []
page_miss = 0
page_hit = 0

for i in pages:
  if i in frames:
    page_hit +=1
    print(i, "Page hit" , frames)
  else:
    if len(frames) < frame:
      frames.append(i)
      page_miss +=1
      print(i, "Page miss" , frames)
    else:
      frames[page_miss % frame] = i
      page_miss +=1
      print(i, "Page miss" , frames)
print("Page miss" , page_miss)
print("Page hit" , page_hit)
