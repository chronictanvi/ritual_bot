# welcome to ritualBot.
# wake up in your (adjective) (place). (verb) your (noun) (adverb). (moveVerb) to your (place).

# Printer setup
import serial
uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=3000)

import adafruit_thermal_printer
ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.69)
printer = ThermalPrinter(uart, auto_warm_up=False)
printer.warm_up(12)

import random

# User Settings
lineWidth = 32 # this should be set according to font size. Suggested 32 for small, 16 for large
printer.size = adafruit_thermal_printer.SIZE_SMALL # can be SMALL, MEDIUM, or LARGE
#printer.bold = False # you want bold text? you got bold text.

printsAttempted = 0

def break_text(string):
    print(len(string))
    if(len(string) >= lineWidth):
        index = string.rfind(" ", 0, lineWidth)
        #string = string[:index] + "\n" + string[(index+1):]
        string1, string2 = string[:index], string[index+1:]
        print(len(string1))
        print(string1)
        printer.print(string1)
        break_text(string2)
    else:
        print(string)
        printer.print(string)
        #printer.write(l + "\n" + r1 + "\n" + r2)

# Rasberry Pi GPIO setup
import RPi.GPIO as GPIO # Import RPi GPIO library

def button_callback(channel):
    print("Button was pushed!")
    # if (time since last button pressed) >= 10 seconds?
    line1 = (f"wake up in your {random.choice(adjectives)} {random.choice(places)}.")
    line2 = (f"{random.choice(verbs)} your {random.choice(nouns)} {random.choice(adverbs)}.")
    line3 = (f"{random.choice(moveVerbs)} to your {random.choice(places)}.")
    print("Lines randomized...")
    break_text(line1)
    printer.feed(2)
    break_text(line2)
    printer.feed(2)
    break_text(line3)
    printer.feed(4)
    print("Ritual printed!")
    #printsAttempted += 1
    #print(printsAttempted)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 as input 10, and initial value low

GPIO.add_event_detect(10, GPIO.RISING, callback=button_callback) # Set up event on pin 10 rising edge

# seeeeeecrets
from secrets import secrets

# Import library and create instance of REST client.
from Adafruit_IO import Client
ADAFRUIT_IO_USERNAME = secrets.get("ADAFRUIT_IO_USERNAME")
ADAFRUIT_IO_KEY = secrets.get("ADAFRUIT_IO_KEY")
print("Setting up Adafruit IO client...")
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
print("...done.")

# Get an array of all data from feed
print("Getting word data...")
adjectivesData = aio.data('ritualbot.adjectives')
placesData = aio.data('ritualbot.placewords')
verbsData = aio.data('ritualbot.verbs')
nounsData = aio.data('ritualbot.nouns')
adverbsData = aio.data('ritualbot.adverbs')
movementVerbsData = aio.data('ritualbot.movementverbs')
print("...done.")

# Print out all the results.
print("Populating word arrays...")
adjectives = []
for d in adjectivesData:
    #print('Data value: {0}'.format(d.value))
    adjectives.append(d.value)

places = []
for d in placesData:
    #print('Data value: {0}'.format(d.value))
    places.append(d.value)

verbs = []
for d in verbsData:
    #print('Data value: {0}'.format(d.value))
    verbs.append(d.value)

nouns = []
for d in nounsData:
    #print('Data value: {0}'.format(d.value))
    nouns.append(d.value)

adverbs = []
for d in adverbsData:
    #print('Data value: {0}'.format(d.value))
    adverbs.append(d.value)

moveVerbs = []
for d in movementVerbsData:
    #print('Data value: {0}'.format(d.value))
    moveVerbs.append(d.value)
print("...done.")
print("Ready!")

printSuccess = False

while True:
    if (printSuccess == True):
        print("Yay?")
    #choice = input("> ")
    #if "q" in choice:
    #    break
