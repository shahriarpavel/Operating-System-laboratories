pages = list(map(int, input("Enter the reference pages string: ").split()))
frame = int(input("Enter the number of frame: "))

frames = []
page_miss = 0
page_hit = 0
recent_page = 0

for i in pages:
    if i in frames:
        page_hit += 1
        recent_page = i
        print(i, "Page hit", frames)
    else:
        if len(frames) < frame:
            frames.append(i)
        else:
            frames[frames.index(recent_page)] = i
        page_miss += 1
        recent_page = i
        print(i, "Page miss", frames)

print("Page miss", page_miss)
print("Page hit", page_hit)
#7 0 1 2 0 3 0 4 2 3