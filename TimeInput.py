AM_STRING = "am"
PM_STRING = "pm"

AM = 0
PM = 1

days_to_integer_mapping = {
  "sun": 0,
  "mon": 1,
  "tue": 2,
  "wed": 3,
  "thu": 4,
  "fri": 5,
	"sat": 6,
}

class TimeInput:
  def __init__(self, inputTime: str):
    self.day, self.hour, self.minute, self.amOrPm = self.__getInputTime(inputTime)
    self.hourInMilitary = self.hour if self.amOrPm == AM else self.hour + 12
  
  def __getInputTime(self, inputTime: str) -> List[int]:
    day, time, amOrPm = inputTime.split(" ")
    hour, minute = time.split(":")
    return [day, hour, minute, AM if amOrPm == AM_STRING else PM] # Change to military time right away
  
  def incrementByMinute(self, minute: int) -> None:
    if minute < 1: return
    #   everytime minute passes 60 -> reset minute to 0 + %60 increment hour 
    #   everytime hour passes 24 -> reset hour to 0 increment day
    #   everytime day passes 6 -> reset day to 0 (sunday)
    self.minute += 5
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
    if self.hourInMilitary == 0:
      self.hour = 12
    elif self.hourInMilitary > 12:
      self.hour = self.hourInMilitary - 12
    self.amOrPm = AM if self.hourInMilitary < 12 else PM

  def __updateDay(self) -> None:
    if self.day > 6:
      self.day = self.day % 6

  def __updateTime(self) -> None:
    self.__updateMinute()
    self.__updateHour()
    self.__updateAmOrPm()
    self.__updateDay()
  
  def __eq__(self, otherTime: "TimeInput"):
    return isinstance(otherTime, "TimeInput") and \
      self.day == otherTime.day and \
      self.hourInMilitary == otherTime.hourInMilitary and \
      self.minute == otherTime.minute 
  
  def __hash__(self):
    # a, 1 + 2 + 3 + 4 + 5
    # b, 5 + 4 + 3 + 2 + 1 
    return hash((self.day, self.hour, self.minute, self.amOrPm))
  
  def __lt__(self, otherTime: "TimeInput"):
    return isinstance(otherTime, "TimeInput") and \
      self.day < otherTime.day or \
      self.hourInMilitary < otherTime.hourInMilitary or \
      self.minute < otherTime.minute 
  
  def __gt__(self, otherTime: "TimeInput"):
    return isinstance(otherTime, "TimeInput") and \
      self.day > otherTime.day or \
      self.hourInMilitary > otherTime.hourInMilitary or \
      self.minute > otherTime.minute 
    
  def __repr__(self):
    return f"{self.day} {self.hourInMilitary}:{self.minute} {AM_STRING if self.amOrPm == AM else PM_STRING}"
  