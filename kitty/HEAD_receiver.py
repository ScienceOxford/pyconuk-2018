from microbit import *
import radio
import random

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

'''
Start conditions:
Turn radio on and to channel 12 (to stop interference)
The channel can be between 0 and 100, and will need to be unique to me!
'''
radio.on()
radio.config(channel=12)
time_off = 0


def red():
    pin0.write_digital(1)
    pin1.write_digital(0)
    pin2.write_digital(0)


def blue():
    pin0.write_digital(0)
    pin1.write_digital(1)
    pin2.write_digital(0)


def green():
    pin0.write_digital(0)
    pin1.write_digital(0)
    pin2.write_digital(1)


def purple():
    pin0.write_digital(1)
    pin1.write_digital(1)
    pin2.write_digital(0)


def teal():
    pin0.write_digital(0)
    pin1.write_digital(1)
    pin2.write_digital(1)


def orange():
    pin0.write_digital(1)
    pin1.write_digital(0)
    pin2.write_digital(1)


def multi():
    pin0.write_digital(1)
    pin1.write_digital(1)
    pin2.write_digital(1)


def off():
    pin0.write_digital(0)
    pin1.write_digital(0)
    pin2.write_digital(0)


def blink():
    timing = random.randint(0, 3)
    if timing == 0:
        time = 500
    if timing == 1:
        time = 3000
    if timing == 2:
        time = 4000
    if timing == 3:
        time = 2000
    blue()
    sleep(time)
    off()
    sleep(100)


def spin():
    for i in range(0, 2):
        red()
        sleep(100)
        blue()
        sleep(100)
        green()
        sleep(100)
        purple()
        sleep(100)
        teal()
        sleep(100)
        orange()
        sleep(100)
        multi()
        sleep(100)
        off()
        sleep(300)


def direction_command():
    global time_off
    if command == "forward":
        green()
        display.show(Image("09990:90009:00000:09090:00000"))
        time_off = 0
    elif command == "backward":
        red()
        display.show(Image("90909:99999:00000:09090:90009"))
        time_off = 0
    elif command == "left":
        purple()
        display.clear()
        time_off = 0
    elif command == "right":
        teal()
        display.clear()
        time_off = 0
    elif command == "stop":
        time_off += 1
        if time_off >= 5:
            display.show(Image("00900:09990:99999:99999:09090"))
            blink()
            time_off = 0
    elif command == "spin":
        display.show(Image("90909:09090:00000:09090:00000"))
        spin()
        time_off = 0
    else:
        display.show("!")


while True:
    command = radio.receive()

    while command is not None:
        direction_command()
        sleep(10)
        command = radio.receive()

    if command is None:
        off()
        display.clear()
