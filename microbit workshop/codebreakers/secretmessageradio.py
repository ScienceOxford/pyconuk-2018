from microbit import *
import radio

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

radio.on()

channels = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
start = "the     password     is  :  "
password = ["lemon",
            "speed",
            "apple",
            "wrong",
            "water",
            "sunny",
            "wheel",
            "robot",
            "maths",
            "horse",
            "block",
            "allow",
            "space"]


def encrypt(key, message):
    translated = ''
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            translated += chr(num)
        else:
            translated += symbol
    return translated


display.show(Image.TARGET)
while True:
    for number in channels:
        radio.config(channel=int(number))
        if number == 12:
            radio.send("X")
        else:
            encrypted = encrypt(number, start + password[number-13])
            encrypted = encrypted.upper()
            radio.send(encrypted)
            #print(encrypted)
    sleep(200)
