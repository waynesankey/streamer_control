from flask import Flask, render_template, request, flash
import RPi.GPIO as GPIO

# this sets up the output to work with Ian's ShieldPiPro, using the GPIO17 as the power control. (RPi J8 Header pin11)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)

app = Flask(__name__)

@app.route("/streamer")
def index():
    return  render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')