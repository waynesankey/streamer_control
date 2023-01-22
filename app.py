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
powerState = GPIO.input(POWER_GPIO)
#powerState = 1
GPIO.output(POWER_GPIO, powerState)

app = Flask(__name__)

@app.route("/streamer")
def index():
    awareTime = datetime.datetime.now(pytz.timezone(timeZone))
    timeString = awareTime.strftime(timeFormat)
    templateData = {
        'pageTitle' : pageTitleStr,
        'time'      : timeString,
        'powerState': powerState
    }
    return  render_template("index.html", **templateData)


@app.route("/<deviceName>/<action>")
def action(deviceName, action):
    if (deviceName == 'powerButton'):
        if (action == 'on'):
            powerState = POWER_ON
            GPIO.output(POWER_GPIO, powerState)
        elif (action == 'off'):
            powerState = POWER_OFF
            GPIO.output(POWER_GPIO, powerState)
    awareTime = datetime.datetime.now(pytz.timezone(timeZone))
    timeString = awareTime.strftime(timeFormat)
    templateData = {
	    'pageTitle' : pageTitleStr,
        'time'      : timeString,
        'powerState': powerState
	}
    return render_template('index.html', **templateData)


if __name__ == '__main__':
    app.run(debug=True, port=5002, host='0.0.0.0')