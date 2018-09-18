from microbit import *
import radio

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

'''
A1A-B1B are the four pins of the motor driver.
A1A/B are for one motor, B1A/B are for the other motor
Define which motor driver pin is connected to which micro:bit pin
'''
AIA = pin14
AIB = pin13
BIA = pin12
BIB = pin15
on = 0
off = 1


'''
Because of the way the motor driver works - 1/high is OFF and 0/low is ON.
Define which pins are high/low for each direction.
'''
def stop():
    AIA.write_digital(off)
    AIB.write_digital(off)
    BIA.write_digital(off)
    BIB.write_digital(off)
    display.show(Image.HAPPY)


def forward():
    AIA.write_digital(on)
    AIB.write_digital(off)
    BIA.write_digital(on)
    BIB.write_digital(off)
    display.show(Image.ARROW_N)


def backward():
    AIA.write_digital(off)
    AIB.write_digital(on)
    BIA.write_digital(off)
    BIB.write_digital(on)
    display.show(Image.ARROW_S)


def left_turn():
    AIA.write_digital(off)
    AIB.write_digital(on)
    BIA.write_digital(on)
    BIB.write_digital(off)
    display.show(Image.ARROW_W)


def right_turn():
    AIA.write_digital(on)
    AIB.write_digital(off)
    BIA.write_digital(off)
    BIB.write_digital(on)
    display.show(Image.ARROW_E)


def spin():
    left_turn()
    sleep(700)
    stop()
    sleep(300)
    right_turn()
    sleep(700)
    stop()
    sleep(300)


'''
Assign each of the above functions to a specific message string.
'''
def direction_command():
    if command == "forward":
        forward()
    elif command == "backward":
        backward()
    elif command == "left":
        left_turn()
    elif command == "right":
        right_turn()
    elif command == "stop":
        stop()
    elif command == "spin":
        spin()
    else:
        display.show("!")


'''
Start conditions:
Turn radio on and to channel 12 (to stop interference)
The channel can be between 0 and 100, and will need to be unique to me!
Define the time_off variable to enable shutoff when no signal received.
'''
radio.on()
radio.config(channel=12)
time_off = 0


'''
Main program:
Check for latest message.
If that message is one of the sent strings, run the associated direction function.
If there is no message received, increase the time_off variable for 10 cycles, then turn off.
'''
while True:
    command = radio.receive()

    while command is not None:
        direction_command()
        command = radio.receive()
        time_off = 0

    if command is None:
        time_off += 1
        if time_off >= 10:
            stop()
