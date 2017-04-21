import argparse


def getIndexes(mapValues, minValue):
    # get all the indexes of duplicates
    indexes = set()
    startAt = -1
    while True:
        try:
            ind = mapValues.index(minValue, startAt + 1)
        # indexes.add(mapValues.index(minValue, i))
        except ValueError:
            break
        else:
            indexes.add(ind)
            startAt = ind
    return indexes


def shortestSeek(currentLoc, currentQueue, previousTrack):
    mapValues = map(lambda x: abs(currentLoc-x), currentQueue)
    minValue = min(mapValues)
    if not mapValues.count(minValue) > 1:
        return currentQueue[mapValues.index(min(mapValues))]
    else:
        # get all the indexes of duplicates
        indexes = getIndexes(mapValues, minValue)
        candidates = []
        for i in indexes:
            candidates.append(currentQueue[i]);
        if previousTrack == -1:
            larger = [track for track in candidates if track > currentLoc]
            smaller = [track for track in candidates if track < currentLoc]
            if larger and smaller:
                # if current < 100, move smaller one
                if currentLoc < 100:
                    return min(candidates)
                # else move larger one
                else:
                    return max(candidates)
            elif larger:
                return max(candidates)
            elif smaller:
                return min(candidates)

        if currentLoc > previousTrack:
            # move to the larger one
            return max(candidates)
        elif currentLoc < previousTrack:
            # move to the smaller one
            return min(candidates)

parser = argparse.ArgumentParser(description="Calculate disk scheduling via sstf")
parser.add_argument('file')
filename = parser.parse_args().file
f = open(filename, 'r')
current = int(f.readline().strip())
prevTrack = -1
listQueue = map(int, f.readline().strip().split(','))
same = [track for track in listQueue if track == current]
otherQueue = [track for track in listQueue if track not in same]
distance = 0
result = []
f.close()

if same:
    for track in same:
        result.append(track)
while otherQueue:
    nextTask = shortestSeek(current, otherQueue, prevTrack)
    result.append(nextTask)
    distance += abs(current - nextTask)
    if not current == nextTask:
        prevTrack = current
    current = nextTask
    otherQueue.remove(current)

print ','.join(map(str, result))
print distance
