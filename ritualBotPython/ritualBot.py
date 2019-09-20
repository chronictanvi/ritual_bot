# welcome to ritualBot.
# wake up in your (adjective) (place). (verb) your (noun) (adverb). (moveVerb) to your (place).

# Printer setup
import serial
uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=3000)

import adafruit_thermal_printer
ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.69)
printer = ThermalPrinter(uart, auto_warm_up=False)
printer.warm_up(12)

import time, random

# Raspberry Pi GPIO setup
import RPi.GPIO as GPIO # Import RPi GPIO library

# User Settings
lineWidth = 32 # this should be set according to font size. Suggested 32 for small, 16 for large
printer.size = adafruit_thermal_printer.SIZE_SMALL # can be SMALL, MEDIUM, or LARGE
#printer.bold = False # you want bold text? you got bold text.

class RitualPrinter:

    inputPin = 0

    line1 = ""
    line2 = ""
    line3 = ""

    printCount = 0

    def __init__(
        self, inputPin, interval_seconds=5
    ):
        self.inputPin = inputPin
        print("Input pin: {}".format(self.inputPin))
        self.interval_seconds = interval_seconds
        print("Interval seconds: {}".format(self.interval_seconds))

        # gpio setup stuff is in here because otherwise it doesn't know where the callback is T_T
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.inputPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # pin set and low initial val

        GPIO.add_event_detect(self.inputPin, GPIO.RISING, self.button_callback) # Set up event on pin

        # time related stuff!
        now = time.time()

        # Publish at most once every 5 seconds
        self.last_publish = now
        self.publish_interval_seconds = 5
        self.last_request = None #?

        # Print at most once every 10 seconds (adjust this?)
        self.last_print = now
        self.print_interval_seconds = 10

        self.setup()

    def on_shutdown(self):
        message = "ritual detector shutting down..."
        aio.send(monitor.key, message)
        print(message)

        GPIO.cleanup()

    def break_text(self, string):
        print(len(string))
        if(len(string) >= lineWidth):
            index = string.rfind(" ", 0, lineWidth)
            #string = string[:index] + "\n" + string[(index+1):]
            string1, string2 = string[:index], string[index+1:]
            print(len(string1))
            print(string1)
            printer.print(string1)
            self.break_text(string2)
        else:
            print(string)
            printer.print(string)

    def button_callback(self, channel):
        now = time.time()
        print("Button was pushed!")
        #if (time since last button pressed) >= 10 seconds?
        if (now - self.last_print > self.print_interval_seconds):
            self.generate_ritual()
        else:
            print("It's not time yet! Be patient. Don't make our printer sad :(")

        self.last_print = now

    def generate_ritual(self):
        origin = random.randint(1,3)
        print("Origin {} selected.".format(origin))
        if(origin == 1):
            line1 = (f"wake up in your {random.choice(adjectives)} {random.choice(places)}.")
            line2 = (f"{random.choice(verbs)} your {random.choice(nouns)} {random.choice(adverbs)}.")
            line3 = (f"{random.choice(moveVerbs)} to your {random.choice(places)}.")
            print("Lines randomized...")

            self.break_text(line1)
            printer.feed(2)
            self.break_text(line2)
            printer.feed(2)
            self.break_text(line3)
            printer.feed(4)
            print("Ritual printed!")

            self.printCount += 1
            print("This is print {}".format(self.printCount))
            aio.send(monitor.key, "Someone printed a ritual!")
            aio.send(counter.key, self.printCount)
            ritualComplete = line1 + " " + line2 + " " + line3
            aio.send(monitor.key, ritualComplete)
        elif(origin == 2):
            line1 = (f"you are {random.choice(adjectives)} again.")
            line2 = (f"{random.choice(adverbs)}, {random.choice(verbs)} your {random.choice(adjectives)} self and {random.choice(verbs)} from the {random.choice(nouns)}.")
            line3 = (f"bearing {random.choice(nouns)} of {random.choice(nouns)} on which a {random.choice(nouns)} and a {random.choice(nouns)} {random.choice(verbs)} {random.choice(adverbs)}.")
            print("Lines randomized...")

            self.break_text(line1)
            printer.feed(2)
            self.break_text(line2)
            printer.feed(2)
            self.break_text(line3)
            printer.feed(4)
            print("Ritual printed!")

            self.printCount += 1
            print("This is print {}".format(self.printCount))
            aio.send(monitor.key, "Someone printed a ritual!")
            aio.send(counter.key, self.printCount)
            ritualComplete = line1 + " " + line2 + " " + line3
            aio.send(monitor.key, ritualComplete)
        elif(origin == 3):
            line1 = (f"do you remember the first time you {random.choice(pastVerbs)} your {random.choice(nouns)}?")
            line2 = (f"if only you could {random.choice(verbs)} {random.choice(occurrences)}, you might {random.choice(verbs)} something for the {random.choice(nouns)}.")
            print("Lines randomized...")

            self.break_text(line1)
            printer.feed(2)
            self.break_text(line2)
            printer.feed(4)
            print("Ritual printed!")

            self.printCount += 1
            print("This is print {}".format(self.printCount))
            aio.send(monitor.key, "Someone printed a ritual!")
            aio.send(counter.key, self.printCount)
            ritualComplete = line1 + " " + line2
            aio.send(monitor.key, ritualComplete)
        else:
            print("Dunno what happened dude my bad")

    def publish(self, string):
        now = time.time()

        if (now - self.last_publish > self.publish_interval_seconds):
            to_publish = string
            print("Publishing this: {}".format(to_publish))

            # send data
            aio.send(monitor.key, to_publish)
            self.last_publish = now
            to_publish = ""

    def setup(self, *args):
        message = "Starting ritualBot on pi!"
        aio.send(monitor.key, message)
        self.last_publish = time.time()
        print(message)

        data = aio.receive('ritualbot.counter')
        self.printCount = int(data.value)
        print("So far we've printed {} rituals. Let's go make some more!".format(self.printCount))

    def run(self):
        # track time between intervals
        last_interval = time.time()
        last_trigger = time.time()

        while True:
            now = time.time()

            #if button is pressed

# seeeeeecrets
from secrets import secrets

# Import library and create instance of REST client.
from Adafruit_IO import Client
ADAFRUIT_IO_USERNAME = secrets.get("ADAFRUIT_IO_USERNAME")
ADAFRUIT_IO_KEY = secrets.get("ADAFRUIT_IO_KEY")
print("Setting up Adafruit IO client...")
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
monitor = aio.feeds('ritualbot.monitor')
counter = aio.feeds('ritualbot.counter')
print("...done.")

# Get an array of all data from feed
print("Getting word data...")
adjectivesData = aio.data('ritualbot.adjectives')
placesData = aio.data('ritualbot.placewords')
verbsData = aio.data('ritualbot.verbs')
pastVerbsData = aio.data('ritualbot.pastverbs')
occurrencesData = aio.data('ritualbot.occurrences')
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

pastVerbs = []
for d in pastVerbsData:
    #print('Data value: {0}'.format(d.value))
    pastVerbs.append(d.value)

occurrences = []
for d in occurrencesData:
    #print('Data value: {0}'.format(d.value))
    occurrences.append(d.value)

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

print("Initializing handler...")
# initialize main class?
#handler = RitualPrinter(aio, "monitor")
handler = RitualPrinter(10)
print("...done.")

# start the whole thing, run forever
handler.run()
