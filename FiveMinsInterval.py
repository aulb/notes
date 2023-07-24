from typing import List

days_to_integer_mapping = {
  "sun": 0, "mon": 1, "tue": 2, "wed": 3, "thu": 4, "fri": 5, "sat": 6,
}

AM_STRING = "am"
PM_STRING = "pm"

AM = 0
PM = 1

def isDayStringValid(day):
  return day in days_to_integer_mapping

def isAmPmStringValid(amOrPm):
  return amOrPm in [AM_STRING, PM_STRING]

def isHourStringValid(hour):
  # "000001" => 1 MON 00000001:12 AM
  if not hour or (len(hour) > 2 and hour.startswith("-")): return False
  try:
    hour = int(hour)
  except Exception:
    return False
  return hour != 0 and hour < 13

def isMinuteStringValid(minute):
  if not minute or (len(minute) != 2 and minute.startswith("-")): return False
  try:
    minute = int(minute)
  except Exception:
    return False
  return minute < 60

def isInputTimeValid(inputTime: str) -> bool:
  # DAY [0-11]:[0-59] [am|pm]
  try:
    day, time, amOrPm = inputTime.split(" ") 
    hour, minute = time.split(":")
  except Exception:
    return False # Incorrect format/malformed string
  return isDayStringValid(day) and \
    isAmPmStringValid(amOrPm) and \
    isHourStringValid(hour) and \
    isMinuteStringValid(minute)

class TimeInput:
  def __init__(self, inputTime: str):
    self.day, self.hour, self.minute, self.amOrPm = self.__getInputTime(inputTime)
    # 12 am -> 0, None
    # 01 am -> 1, None
    # 11 am -> 11, None
    # 12 pm -> 12, None
    # 01 pm -> 13, + 12
    # 11 pm -> 23, + 12
    if self.hour == 12 and self.amOrPm == AM:
      self.hourInMilitary = 0
    elif self.hour == 12 and self.amOrPm == PM:
      self.hourInMilitary = 12
    else:
      self.hourInMilitary = self.hour if self.hour < 12 and self.amOrPm == AM else self.hour + 12
  
  def __getInputTime(self, inputTime: str) -> List[int]:
    day, time, amOrPm = inputTime.split(" ")
    hour, minute = time.split(":")
    return [days_to_integer_mapping[day], int(hour), int(minute), AM if amOrPm == AM_STRING else PM] # Change to military time right away
  
  def incrementByMinute(self, minute: int) -> None:
    if minute < 1: return
    #   everytime minute passes 60 -> reset minute to 0 + %60 increment hour 
    #   everytime hour passes 24 -> reset hour to 0 increment day
    #   everytime day passes 6 -> reset day to 0 (sunday)
    self.minute += minute
    self.__updateTime()
  
  def __updateMinute(self) -> None:
    if self.minute > 59:
      hours = self.minute // 60
      remainder = self.minute % 60
      self.minute = remainder
      self.hourInMilitary += hours
    
  def __updateHour(self) -> None:
    if self.hourInMilitary > 23:
      days = self.hourInMilitary // 24
      remainder = self.hourInMilitary % 24
      self.hourInMilitary = remainder
      self.day += days

  def __updateAmOrPm(self) -> None:
    self.amOrPm = AM if self.hourInMilitary < 12 else PM
    if self.hourInMilitary == 0:
      self.hour = 12
      self.amOrPm = AM
    elif self.hourInMilitary > 12:
      self.hour = self.hourInMilitary - 12

  def __updateDay(self) -> None:
    if self.day > 6:
      self.day = self.day % 6

  def __updateTime(self) -> None:
    self.__updateMinute()
    self.__updateHour()
    self.__updateAmOrPm()
    self.__updateDay()
  
  def __eq__(self, otherTime: "TimeInput"):
    return self.day == otherTime.day and \
      self.hourInMilitary == otherTime.hourInMilitary and \
      self.minute == otherTime.minute 
  
  def __hash__(self):
    # if we hash with "+": a, 1 + 2 + 3 + 4 + 5, b, 5 + 4 + 3 + 2 + 1 
    return hash((self.day, self.hour, self.minute, self.amOrPm))
  
  def __lt__(self, otherTime: "TimeInput"):
    return self.day < otherTime.day or \
       self.hourInMilitary < otherTime.hourInMilitary or \
       self.minute < otherTime.minute
  
  def __gt__(self, otherTime: "TimeInput"):
    return self.day > otherTime.day or \
       self.hourInMilitary > otherTime.hourInMilitary or \
       self.minute > otherTime.minute

  def __le__(self, otherTime: "TimeInput"):
    return self.__lt__(otherTime) or self.__eq__(otherTime)
  
  def __ge__(self, otherTime: "TimeInput"):
    return self.__gt__(otherTime) or self.__eq__(otherTime)
    
  def __repr__(self):
    minuteString = str(self.minute).rjust(2, "0")
    return f"{self.day} {self.hourInMilitary}:{minuteString} {AM_STRING if self.amOrPm == AM else PM_STRING}"

def fiveMinuteIntervals(startTime: str, endTime: str) -> List[str]:
  if not isInputTimeValid(startTime) or not isInputTimeValid(endTime): return [] # Error
  start, end = TimeInput(startTime), TimeInput(endTime)
  result = []
  # For every increment check end time, stop when it passes the end time 
  # Easy case - end time is later
  while end >= start:
    result.append(str(start))
    start.incrementByMinute(5)
  # Tricky case - end time is "earlier" - wrap around # Not yet implemented
  return result

if __name__ == "__main__":
  startTime = "mon 12:01 am"
  endTime = "tue 12:02 am"
  print(fiveMinuteIntervals(startTime, endTime))
  # test = TimeInput("mon 12:00 am")
  # test.incrementByMinute(539) 
