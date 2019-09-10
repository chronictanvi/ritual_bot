import random

# seeeeeecrets
from secrets import secrets

# Import library and create instance of REST client.
from Adafruit_IO import Client
ADAFRUIT_IO_USERNAME = secrets.get("ADAFRUIT_IO_USERNAME")
ADAFRUIT_IO_KEY = secrets.get("ADAFRUIT_IO_KEY")
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Get an array of all data from feed 'Test'
adjectivesData = aio.data('ritualbot.adjectives')
placesData = aio.data('ritualbot.placewords')
verbsData = aio.data('ritualbot.verbs')
nounsData = aio.data('ritualbot.nouns')
adverbsData = aio.data('ritualbot.adverbs')
movementVerbsData = aio.data('ritualbot.movementverbs')

# Print out all the results.
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

lineWidth = 16

def break_text(string):
    print(len(string))
    if(len(string) >= 16):
        index = string.rfind(" ", 0, 16)
        #string = string[:index] + "\n" + string[(index+1):]
        string1, string2 = string[:index], string[index+1:]
        print(len(string1))
        print(string1)
        break_text(string2)
    else:
        print(string)
        #printer.write(l + "\n" + r1 + "\n" + r2)

# wake up in your (adjective) (place). (verb) your (noun) (adverb). (moveVerb) to your (place).
line1 = (f"wake up in your {random.choice(adjectives)} {random.choice(places)}.")
line2 = (f"{random.choice(verbs)} your {random.choice(nouns)} {random.choice(adverbs)}.")
line3 = (f"{random.choice(moveVerbs)} to your {random.choice(places)}.")

break_text(line1)
break_text(line2)
break_text(line3)
