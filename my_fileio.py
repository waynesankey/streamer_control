import json

class Files:

    def getTimeZone(self):
        timeZone = "GMT"
        with open('staticData.json', encoding="utf-8") as f:
            x = json.load(f)
            timeZone = x["timeZone"]        
        return timeZone

    def getUserName(self):
        userName = "Wayne"
        with open('staticData.json', encoding="utf-8") as f:
            x = json.load(f)
            userName = x["userName"]
        return userName

    def getMachineName(self):
        machineName = "Streamer"
        with open('staticData.json', encoding="utf-8") as f:
            x = json.load(f)
            machineName = x["machineName"]
        return machineName

    def getTotalOnTime(self):
        with open('dynamicData.json', "r", encoding="utf-8") as f:
            x = json.load(f)
            totalOnTime = x["totalOnTime"]        
        return totalOnTime

    def putTotalOnTime(self, totalOnTime):
        with open('dynamicData.json', "r", encoding="utf-8") as f:
            x = json.load(f)
        x["totalOnTime"] = totalOnTime
        with open('dynamicData.json', "w", encoding="utf-8") as f:
            json.dump(x,f, indent=4)
        return

    def getHeading1(self):
        heading1Str = ""
        with open('staticData.json', "r", encoding="utf-8") as f:
            x = json.load(f)
            heading1Str = x["heading1"]       
        return heading1Str