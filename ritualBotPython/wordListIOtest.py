import random

# seeeeeecrets
from secrets import secrets

# Import library and create instance of REST client.
from Adafruit_IO import Client
ADAFRUIT_IO_USERNAME = secrets.get("ADAFRUIT_IO_USERNAME")
ADAFRUIT_IO_KEY = secrets.get("ADAFRUIT_IO_KEY")
print("Establishing Adafruit IO client...")
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
print("...done.")

# Sophie's feeds test?
#IO_FEED = 'sharingtest.feedtest'
#IO_FEED_USERNAME = 'perhapsfrogs'

print("Getting word data from Adafruit IO...")
# Get an array of all data from feed 'Test'
adjectivesData = aio.data('ritualbot.adjectives')
placesData = aio.data('ritualbot.placewords')
verbsData = aio.data('ritualbot.verbs')
pastVerbsData = aio.data('ritualbot.pastverbs')
occurrencesData = aio.data('ritualbot.occurrences')
nounsData = aio.data('ritualbot.nouns')
adverbsData = aio.data('ritualbot.adverbs')
movementVerbsData = aio.data('ritualbot.movementverbs')

# testing getting data from Sophie's feeds?
# sophieData = aio.data('sharingtest.feedtest')
print("...done.")

print("Appending word data to arrays...")
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

# sophieTest = []
# for d in sophieData:
#     print('Data value: {0}'.format(d.value))
#     sophieTest.append(d.value)
print("...done.")

lineWidth = 32

def break_text(string):
    print(len(string))
    if(len(string) >= lineWidth):
        index = string.rfind(" ", 0, lineWidth)
        #string = string[:index] + "\n" + string[(index+1):]
        string1, string2 = string[:index], string[index+1:]
        print(len(string1))
        print(string1)
        break_text(string2)
    else:
        print(string)
        #printer.write(l + "\n" + r1 + "\n" + r2)

def generate_ritual():
    origin = random.randint(1,3)
    print("Origin {} selected.".format(origin))
    if(origin == 1):
        line1 = (f"wake up in your {random.choice(adjectives)} {random.choice(places)}.")
        line2 = (f"{random.choice(verbs)} your {random.choice(nouns)} {random.choice(adverbs)}.")
        line3 = (f"{random.choice(moveVerbs)} to your {random.choice(places)}.")

        break_text(line1)
        break_text(line2)
        break_text(line3)
    elif(origin == 2):
        line1 = (f"you are {random.choice(adjectives)} again.")
        line2 = (f"{random.choice(adverbs)}, {random.choice(verbs)} your {random.choice(adjectives)} self and {random.choice(verbs)} from the {random.choice(nouns)}.")
        line3 = (f"bearing {random.choice(nouns)} of {random.choice(nouns)} on which a {random.choice(nouns)} and a {random.choice(nouns)} {random.choice(verbs)} {random.choice(adverbs)}.")

        break_text(line1)
        break_text(line2)
        break_text(line3)
    elif(origin == 3):
        line1 = (f"do you remember the first time you {random.choice(pastVerbs)} your {random.choice(nouns)}?")
        line2 = (f"if only you could {random.choice(verbs)} {random.choice(occurrences)}, you might {random.choice(verbs)} something for the {random.choice(nouns)}.")

        break_text(line1)
        break_text(line2)
    else:
        print("Dunno what happened dude my bad")


# wake up in your (adjective) (place). (verb) your (noun) (adverb). (moveVerb) to your (place).
#line1 = (f"wake up in your {random.choice(adjectives)} {random.choice(places)}.")
#line2 = (f"{random.choice(verbs)} your {random.choice(nouns)} {random.choice(adverbs)}.")
#line3 = (f"{random.choice(moveVerbs)} to your {random.choice(places)}.")

# you are (adjective) again. (adverb), (verb) your (adjective) self and (verb) from the (noun). bearing  (noun) of (noun) on which a (noun) and a (noun) (verb) (adverb).
#line1 = (f"you are {random.choice(adjectives)} again.")
#line2 = (f"{random.choice(adverbs)}, {random.choice(verbs)} your {random.choice(adjectives)} self and {random.choice(verbs)} from the {random.choice(nouns)}.")
#line3 = (f"bearing {random.choice(nouns)} of {random.choice(nouns)} on which a {random.choice(nouns)} and a {random.choice(nouns)} {random.choice(verbs)} {random.choice(adverbs)}.")

# do you remember the first time you (pastverb) your (noun)? if only you could (verb) (occurrence), you might (verb) something for the (noun).
#line1 = (f"do you remember the first time you {random.choice(pastVerbs)} your {random.choice(nouns)}?")
#line2 = (f"if only you could {random.choice(verbs)} {random.choice(occurrences)}, you might {random.choice(verbs)} something for the {random.choice(nouns)}.")

generate_ritual()
