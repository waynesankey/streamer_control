import datetime as dt
import pytz
import time

class Time:

    #initalize variables and set the types by putting dummy variables on the RHS
    turnOnTime = dt.datetime.now()
    turnOffTime = dt.datetime.now()
    totalTurnOnTime = time.time()
    totalOnTime = time.time()
    timeZone = ""
    timeFormat = ""
    deltaFormat = ""

    def __init__(self):
        print("in time module")
        self.timeZone = "GMT"
#        self.timeZone = fi.getTimeZone()
        self.timeFormat = "%b-%d-%Y %I:%M:%S %p"
        self.deltaFormat = "%H:%M:%S"
        self.turnOnTime = dt.datetime.now(pytz.timezone(self.timeZone))
        self.turnOffTime = dt.datetime.now(pytz.timezone(self.timeZone))
        self.totalTurnOnTime = time.time()
        self.totalTurnOffTime = time.time()
        self.totalOnTime = 0
        return

    def setTimeZone(self, tz):
        print(f"Setting tz to {tz}")
        self.timeZone = tz
        return

    def setTurnOnTime(self):
        self.turnOnTime = dt.datetime.now(pytz.timezone(self.timeZone))
        self.totalTurnOnTime = time.time()
        return

    def setTurnOffTime(self):
        self.turnOffTime = dt.datetime.now(pytz.timezone(self.timeZone))
        self.totalTurnOffTime = time.time()
        return

    def getTimeOn(self):
        timeOn = 0.0
        timeOn = self.totalTurnOffTime - self.totalTurnOnTime
        return int(timeOn)

    def updateTotalOnTime(self, totalOnTime):
        self.totalOnTime = totalOnTime
        return self.totalOnTime

    def currentTime(self):
        awareTime = dt.datetime.now(pytz.timezone(self.timeZone))
        timeString = awareTime.strftime(self.timeFormat)
        return timeString

    def timeTurnedOn(self):
        elapsed = self.turnOffTime - self.turnOnTime
        outputString = self.formatTimedeltaDHMS(elapsed)
        return outputString

    def timeTurnedOff(self):
        elapsed = self.turnOnTime - self.turnOffTime
        outputString = self.formatTimedeltaDHMS(elapsed)
        return outputString

    def getTotalOnTime(self):
        outputString = ""
        outputString = self.formatTimeHMS(self.totalOnTime)
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