from microbit import *
import radio

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
display.show(Image.GIRAFFE)

'''
Main program:
Send message string based on which button or external switch pressed.
'''
while True:
    if pin14.read_digital() == 1:
        radio.send("left")
        sleep(1)
        display.show("L")
    elif pin1.read_digital() == 1:
        radio.send("right")
        sleep(1)
        display.show("R")
    elif pin16.read_digital() == 1:
        radio.send("forward")
        sleep(1)
        display.show("F")
    elif pin2.read_digital() == 1:
        radio.send("backward")
        sleep(1)
        display.show("B")
    elif pin0.read_digital() == 1:
        radio.send("spin")
        display.show("S")
        sleep(500)
    else:
        radio.send("stop")
        display.show(Image.GIRAFFE)
        sleep(500)
