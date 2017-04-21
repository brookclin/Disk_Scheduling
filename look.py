import argparse

parser = argparse.ArgumentParser(description="Calculate disk scheduling via look")
parser.add_argument('file')
filename = parser.parse_args().file
f = open(filename, 'r')
current = int(f.readline().strip())
listQueue = map(int, f.readline().strip().split(','))
distance = 0
result = []
f.close()

larger = [track for track in listQueue if track > current]
same = [track for track in listQueue if track == current]
smaller = [track for track in listQueue if track < current]
larger = sorted(larger)
smaller = sorted(smaller, reverse=True)

if same:
    for track in same:
        result.append(track)
listset = []
if larger and smaller:
    if larger[0] - current == current - smaller[0]:
        if current < 100:
            listset = [smaller, larger]
        else:
            listset = [larger, smaller]
    elif larger[0] - current < current - smaller[0]:
        listset = [larger, smaller]
    else:
        listset = [smaller, larger]
elif larger and not smaller:
    listset = [larger]
elif smaller and not larger:
    listset = [smaller]

for sublist in listset:
    for nextTrack in sublist:
        result.append(nextTrack)
        distance += abs(current-nextTrack)
        current = nextTrack

print ','.join(map(str, result))
print distance