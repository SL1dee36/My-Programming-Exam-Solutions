s = input()
result = []
intervals = s.split(',')

for interval in intervals:
    if '-' in interval:
        start, end = map(int,interval.split('-'))
        for i in range(start,end+1):
            result.append(i)
    else:
        result.append(int(interval))
result.sort()
print(*result)