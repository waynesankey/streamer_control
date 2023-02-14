import datetime as dt
import pytz
import time

class Time:

    turnOnTime = dt.datetime.now()
    turnOffTime = dt.datetime.now()
    totalTurnOnTime = time.time()
    totalTime = time.time()
    timeZone = ""
    timeFormat = ""
    deltaFormat = ""

    def __init__(self):
        print("in time module")
        self.timeZone = "US/Central"
        self.timeFormat = "%b-%d-%Y %I:%M:%S %p"
        self.deltaFormat = "%H:%M:%S"
        self.turnOnTime = dt.datetime.now(pytz.timezone(self.timeZone))
        self.turnOffTime = dt.datetime.now(pytz.timezone(self.timeZone))
        self.totalTurnOnTime = time.time()
        self.totalTime = 0
        return

    def turn_on(self):
        self.turnOnTime = dt.datetime.now(pytz.timezone(self.timeZone))
        self.totalTurnOnTime = time.time()
        return

    def turn_off(self):
        self.turnOffTime = dt.datetime.now(pytz.timezone(self.timeZone))
        self.totalTime = self.totalTime + (time.time() - self.totalTurnOnTime)
        return

    def current_time(self):
        awareTime = dt.datetime.now(pytz.timezone(self.timeZone))
        timeString = awareTime.strftime(self.timeFormat)
        return timeString

    def time_turned_on(self):
        elapsed = self.turnOffTime - self.turnOnTime
        outputString = self.formatTimedeltaDHMS(elapsed)
        return outputString

    def time_turned_off(self):
        elapsed = self.turnOnTime - self.turnOffTime
        outputString = self.formatTimedeltaDHMS(elapsed)
        return outputString

    def get_total_time(self):
        outputString = ""
        outputString = self.formatTimeHMS(self.totalTime)
        return outputString

    def formatTimedeltaDHMS(self, timeDeltaIn):
        stringDHMS = "ERROR in formatTimedeltaDHMS"
        # days = timeDeltaIn.days
        # hours = timeDeltaIn.hours
        # minutes = timeDeltaIn.minutes
        # seconds = timeDeltaIn.seconds

        intTime = int(timeDeltaIn.total_seconds())
        days, remainder = divmod(intTime, 24*60*60)
        hours, remainder = divmod(remainder, 60*60)
        minutes, seconds = divmod(remainder, 60)

        if days == 0:
            stringDHMS = str(hours) + "H " + str(minutes) + "M " + str(seconds) + "S"
        elif days > 0:
            stringDHMS = str(days) + " Days " + str(hours) + "H " + str(minutes) + "M " + str(seconds) + "S"
        return stringDHMS

    def formatTimeHMS(self, input_time):
        timeStringHMS = "ERROR in formatTimeHMS"
        intTime = int(input_time)
        print(f"time input is {input_time}, intTime is {intTime}")
        hours, remainder = divmod(intTime, 60*60)
        minutes, seconds = divmod(remainder, 60)
        print(f"hours {hours} minutes {minutes} seconds {seconds}")
        timeStringHMS = str(hours) + "H " + str(minutes) + "M " + str(seconds) + "S"
        return timeStringHMS