import argparse

parser = argparse.ArgumentParser(description="Calculate disk scheduling via c-scan")
parser.add_argument('file')
filename = parser.parse_args().file
f = open(filename, 'r')
current = int(f.readline().strip())
listQueue = map(int, f.readline().strip().split(','))
distance = 0
result = []
f.close()

larger = [track for track in listQueue if track >= current]
smaller = [track for track in listQueue if track not in larger]
larger = sorted(larger)
smaller = sorted(smaller)

if larger:
    for nextTrack in larger:
        result.append(nextTrack)
        distance += abs(current - nextTrack)
        current = nextTrack
if smaller:
    distance += (199 - current) + 199
    current = 0
    for nextTrack in smaller:
        result.append(nextTrack)
        distance += abs(current - nextTrack)
        current = nextTrack
print ','.join(map(str, result))
print distance