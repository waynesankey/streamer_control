from flask import Flask, render_template, request, flash
import RPi.GPIO as GPIO
import my_time
import my_fileio
import json


# constants to set for project
POWER_OFF = GPIO.LOW
POWER_ON = GPIO.HIGH
POWER_GPIO = 17

userName = "Wayne"
machineName = "Streamer"

#instantiate the user defined classes

tim = my_time.Time()
fi = my_fileio.Files()


machineName = fi.getMachineName()
userName = fi.getUserName()
pageTitleStr = userName + "\'s " + machineName
heading1Str = fi.getHeading1()
print(f"this {machineName} belongs to {userName}")

# this sets up the output to work with Ian's ShieldPiPro, using the GPIO17 as the power control. (RPi J8 Header pin11)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(POWER_GPIO, GPIO.OUT)
powerActual = GPIO.input(POWER_GPIO)
powerState = powerActual
GPIO.output(POWER_GPIO, powerState)

print(f"powerState is {powerState}.")



app = Flask(__name__)

@app.route("/streamer", methods = ["POST", "GET"])
def index():
    global powerState
    global powerActual

    if request.method == "POST":
        print("Starting the streamer route.")

        #doens't work - whong language ?
#        if request.POST.get("button_turn_on") or request.POST.get("button_turn_off"): 
        # if request.form["button_turn_off"]:
        #     print(f"OFF button pushed.")
        # if request.form["button_turn_on"]:
        #     print(f"ON button pushed.")

        # also doens't work - not sure why, right out of a web page example
        # output = request.form.to_dict()
        # name = output["name"]
        # print(f"button name is {name}")

        tim.setTimeZone(fi.getTimeZone())

        powerActual = GPIO.input(POWER_GPIO)
        print(f"Just sampled GPIO {POWER_GPIO}, the value is {powerActual}")

        print(f"at start of route, powerState is {powerState}")
        if powerState >= 1:  # Power was ON - turn it OFF
            powerState = 0
            tim.setTurnOffTime()
            timeOn = tim.getTimeOn()
            totalOnTime = fi.getTotalOnTime()
            print(f"totalOnTIme from json file: {totalOnTime}")
            totalOnTime =  totalOnTime + timeOn
            tim.updateTotalOnTime(totalOnTime)
            fi.putTotalOnTime(totalOnTime)
            delta_time = tim.timeTurnedOn()
            total_time = tim.getTotalOnTime()
        else:                # Power was OFF - turn it ON
            powerState = 1
            tim.setTurnOnTime()
            delta_time = tim.timeTurnedOff()
            total_time = tim.getTotalOnTime()
        print(f"Now powerState is toggled and is: {powerState}")
        print(f"Setting GPIO {POWER_GPIO} power to {powerState}")
        GPIO.output(POWER_GPIO, powerState)
        powerActual = GPIO.input(POWER_GPIO)
        print(f"And one final sample of the GPIO {POWER_GPIO} to see what it's actually set to: {powerActual}")
        
        templateData = {
            'pageTitle'    : pageTitleStr,
            'heading'      : heading1Str,
            'time'         : tim.currentTime(),
            'deltaTime'    : delta_time,
            'totalTime'    : total_time,
            'powerState'   : powerState,
            'powerActual'  : powerActual
        }
        return  render_template("index.html", **templateData)
    else:
        templateData = {
            'pageTitle'    : pageTitleStr,
            'heading'      : heading1Str,
            'time'         : tim.currentTime(),
            'powerState'   : powerState,
            'powerActual'  : powerActual
        }
        return  render_template("index.html", **templateData)


# @app.route("/<deviceName>/<action>")
# def action(deviceName, action):
#     if (deviceName == 'powerButton'):
#         if (action == 'on'):
#             powerState = POWER_ON
#             GPIO.output(POWER_GPIO, powerState)
#         elif (action == 'off'):
#             powerState = POWER_OFF
#             GPIO.output(POWER_GPIO, powerState)
#     awareTime = datetime.datetime.now(pytz.timezone(timeZone))
#     timeString = awareTime.strftime(timeFormat)
#     templateData = {
# 	    'pageTitle' : pageTitleStr,
#         'time'      : timeString,
#         'powerState': powerState
# 	}
#     return render_template('index.html', **templateData)


if __name__ == '__main__':
    app.run(debug=True, port=5002, host='0.0.0.0')