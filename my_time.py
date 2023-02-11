import datetime
import pytz
import time

class Time:

    turnOnTime = 0
    turnOffTime = 0
    onTime = 0
    offTime = 0
    totalOnTime = 0
    timeZone = ""
    timeFormat = ""

    def __init__(self):
        print("in time module")
        self.timeZone = "US/Central"
        self.timeFormat = "%Y-%m-%d %H:%M:%S"
        self.totalOnTime = 0
        self.onTime = 0
        self.offTime = 0
        return

    def turn_on(self):
        self.turnOnTime = time.time()
        self.offTime = time.time() - self.turnOffTime
        return

    def turn_off(self):
        self.turnOffTime = time.time()
        self.onTime = time.time() - self.turnOnTime
        self.totalOnTime = self.totalOnTime + self.onTime
        return

    def current_time(self):
        awareTime = datetime.datetime.now(pytz.timezone(self.timeZone))
        timeString = awareTime.strftime(self.timeFormat)
        return timeString

    def time_turned_on(self):
        return self.onTime

    def time_turned_off(self):
        return self.offTime