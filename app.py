from flask import Flask, render_template, request, flash
import RPi.GPIO as GPIO
import datetime
import pytz

# constants to set for project
POWER_OFF = GPIO.LOW
POWER_ON = GPIO.HIGH
POWER_GPIO = 17

pageTitleStr = "Wayne's High-end Streamer"
timeZone = "US/Central"
timeFormat = "%Y-%m-%d %H:%M:%S"

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
        powerActual = GPIO.input(POWER_GPIO)
        print(f"Just sampled GPIO {POWER_GPIO}, the value is {powerActual}")

        awareTime = datetime.datetime.now(pytz.timezone(timeZone))
        timeString = awareTime.strftime(timeFormat)

        print(f"at start of route, powerState is {powerState}")
        if powerState >= 1:
            powerState = 0
        else:
            powerState = 1
        print(f"Now powerState is toggled and is: {powerState}")
        print(f"Setting GPIO {POWER_GPIO} power to {powerState}")
        GPIO.output(POWER_GPIO, powerState)
        powerActual = GPIO.input(POWER_GPIO)
        print(f"And one final sample of the GPIO {POWER_GPIO} to see what it's actually set to: {powerActual}")
        
        templateData = {
            'pageTitle'    : pageTitleStr,
            'time'         : timeString,
            'powerState'   : powerState,
            'powerActual'  : powerActual
        }
        return  render_template("index.html", **templateData)
    else:
        awareTime = datetime.datetime.now(pytz.timezone(timeZone))
        timeString = awareTime.strftime(timeFormat)

        templateData = {
            'pageTitle'    : pageTitleStr,
            'time'         : timeString,
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