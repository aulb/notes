"""
   Paul: 1315 1355 1405
   Jose: 830 835 855 915 930
   Zhang: 10 109 110
   Amos: 500 503 504
"""
# 1315x 1355 indstart 1416 1417 indend

def within_the_hour(time1, time2):
    return time1 + 100 >= time2

def find_multiple_badging(badge_times):
    sorted_badge_times = sorted(badge_times, key=lambda x: int(x[1])) # O(nlogn)
    employee_activities = {}
    for badge_time in sorted_badge_times: # O(n)
        name, time = badge_time
        if name not in employee_activities: employee_activities[name] = []
        employee_activities[name].append(int(time))
    # Paul: [1315, 1355, 1405, 1416]
    records = {} # {"Paul": [1315, 1355, 1405]}
    for name in employee_activities: # O(n)
        times = employee_activities[name]
        start_index = 0
        for index, time in enumerate(times):
            if within_the_hour(times[start_index], time):
                if name not in records or records[name][1] - records[name][0] < index - start_index:
                    records[name] = [start_index, index]
            else:
                start_index += 1
    
    delete_name = []
    for name in records:
        times = employee_activities[name]
        if records[name][1] - records[name][0] + 1 < 3:
            delete_name.append(name)
        else:
            records[name] = [times[index] for index in range(records[name][0], records[name][1] + 1)]

    for name in delete_name: del records[name]
    return records
    
badge_records = [
  ["Paul", "1355"],
  ["Jennifer", "1910"],
  ["Jose", "835"],
  ["Jose", "830"],
  ["Paul", "1315"],
  ["Chloe", "0"],
  ["Chloe", "1910"],
  ["Jose", "1615"],
  ["Jose", "1640"],
  ["Paul", "1405"],
  ["Jose", "855"],
  ["Jose", "930"],
  ["Jose", "915"],
  ["Jose", "730"],
  ["Jose", "940"],
  ["Jennifer", "1335"],
  ["Jennifer", "730"],
  ["Jose", "1630"],
  ["Jennifer", "5"],
  ["Chloe", "1909"],
  ["Zhang", "1"],
  ["Zhang", "10"],
  ["Zhang", "109"],
  ["Zhang", "110"],
  ["Amos", "1"],
  ["Amos", "2"],
  ["Amos", "400"],
  ["Amos", "500"],
  ["Amos", "503"],
  ["Amos", "504"],
  ["Amos", "601"],
  ["Amos", "602"],
  ["Paul", "1416"],
]

print(find_multiple_badging(badge_records))