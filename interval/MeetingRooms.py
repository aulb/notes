def canAttendAll(intervals):
    if len(intervals) == 0: return True
    intervals.sort(key=lambda interval: interval[0])
    previousInterval = intervals[0]
    for index in range(1, len(intervals)):
        interval = intervals[index]
        if previousInterval[1] > interval[0]: return False
    return True