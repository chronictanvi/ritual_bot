import random

lineWidth = 16

def space_text(string):
    print(len(string))
    if(len(string) >= 16 and string[16] != " "):
        index = string.rfind(" ", 0, 16)
        string = string[:index] + "\n" + string[(index+1):]
        if(len(string) >= 32 and string[32] != " "):
            index = string.rfind(" ", 16, 32)
            string = string[:index] + "\n" + string[(index+1):]
        return string
    else:
        return string

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

places = ['apartment', 'bathroom', 'cabin', 'cell', 'community garden', 'community pool', 'condo', 'cottage', 'ditch', 'dream', 'environment', 'fish tank', 'friend\'s basement', 'grave', 'house', 'local grocery store', 'local library', 'local park', 'river', 'roof', 'school bus', 'womb', 'workplace']

adjectives = ['charming', 'chilly', 'conflicted', 'damp', 'dusty', 'frivolous', 'glamorous', 'glowing', 'gruesome', 'languid', 'lovely', 'medium', 'messy', 'modern', 'orange', 'ripe', 'rural', 'sad', 'silly', 'sparkly', 'suspicious', 'tasty', 'ugly', 'uncaring', 'underdeveloped', 'unfortunate', 'warm']

verbs = ['annotate', 'avoid', 'bake', 'browse', 'brush', 'burn', 'caress', 'check', 'confess', 'contemplate', 'criticize', 'deny', 'drink', 'eat', 'email', 'feed', 'find', 'forget', 'gamble', 'hear', 'hide from', 'ignore', 'lose', 'lubricate', 'observe', 'part from', 'perform', 'pet', 'pray to', 'press', 'put on', 'question', 'read', 'rearrange', 'rescue', 'restart', 'restore', 'share', 'solve', 'spend', 'steal', 'stop', 'synthesize', 'touch', 'visit', 'wash', 'watch', 'wrestle with', 'write']

moveVerbs = ['amble', 'climb', 'crawl', 'drive', 'escape', 'inch', 'jump in', 'limp', 'march', 'moonwalk', 'prowl', 'ride', 'roll', 'run', 'shimmy','shuffle', 'skate', 'sleepwalk', 'sneak', 'stomp', 'stride', 'strut', 'stumble', 'swim', 'trek', 'walk']

nouns = ['alarm', 'bra', 'breakfast', 'breath', 'cat', 'coffee', 'colonizer', 'crossword', 'cup of water', 'dog', 'elevator button', 'email', 'enemy', 'family', 'future', 'government', 'hope', 'identity', 'income', 'information', 'local news', 'love', 'lover', 'mail', 'meds', 'memory', 'papers', 'phone', 'printer', 'problems', 'reflection', 'roommate', 'sexuality', 'socks', 'spouse', 'sweater', 'teeth', 'television', 'text', 'time', 'toothbrush', 'twin', 'window']

adverbs = ['adequately', 'aggressively', 'automatically', 'begrudgingly', 'carefully', 'carelessly', 'cheerfully', 'dejectedly', 'deliciously', 'delusionally', 'disastrously', 'ethically', 'exclusively', 'gently', 'hastily', 'hypnotically', 'internally', 'loudly', 'lovingly', 'mischievously', 'necessarily', 'notoriously', 'obsessively', 'poorly', 'precariously', 'problematically', 'punctually', 'religiously',
'reluctantly', 'repeatedly', 'secretly', 'shamefully', 'shamelessly', 'soulfully', 'suspiciously', 'tastefully', 'thoughtfully', 'thoughtlessly', 'timidly', 'unfortunately', 'unwillingly']

# wake up in your (adjective) (place). (verb) your (noun) (adverb). (moveVerb) to your (place).
# print
line1 = (f"wake up in your {random.choice(adjectives)} {random.choice(places)}.")
line2 = (f"{random.choice(verbs)} your {random.choice(nouns)} {random.choice(adverbs)}.")
line3 = (f"{random.choice(moveVerbs)} to your {random.choice(places)}.")

testLine = "rearrange your government thoughtlessly."
testLine2 = "wake up in your charming local grocery store."
testLine3 = "wake up in your uncaring workplace."
testLine4 = "wake up in your ugly fish tank."

#break_text(testLine4)

break_text(line1)
break_text(line2)
break_text(line3)
