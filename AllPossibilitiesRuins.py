from math import floor

encounters = ["F", "W"]
alle = []
space = {"F": 1, "W": 1}

def f(combo, lim, length):
    for x in encounters:
        new_combo = combo + [x,]
        new_length = length + space[x]
        if new_length >= lim:
            alle.append(new_combo)
        else:
            f(new_combo, lim, new_length)

def scr_steps(argument0, argument1, argument2, kills): # Remake of the gamemaker code
    populationfactor = (argument2 / (argument2 - kills))
    if populationfactor > 8:
        populationfactor = 8
    steps = (argument0 + 0.5*(argument1)) * populationfactor
    return floor(steps)+1

def framesToMinutes(x):
    seconds = x/30
    minutes = floor(seconds/60)
    seconds = seconds - minutes * 60
    if seconds < 10:
        seconds = '0' + str(seconds)
    else:
        seconds = str(seconds)
    minutes = str(minutes)
    return minutes + ":" + seconds

f([], 13, 0)

first_half = alle.copy()
alle = []

encounters = ["1M", "2M", "3M", "1F", "2F"]
space = {"1M": 1, "2M": 2, "3M": 3, "1F": 2, "2F": 2}

f([], 7, 0)

second_half = alle.copy()
alle = []

baseline = 4057 + 28 + 90 + 50 + 31 + 33 + 5 + 13 * (47 + 2.5 + 9) + 101 + 106 + 111.5 + 118.5 + 126 + 134 + 143.5 + 154.5 + 167.5 + 182.5 + 201 + 222.5 + 251 + 244 + 116 + 27 - 18 + 4565

times = {"F": 306.55, "W": 101, "1M": 368, "2M": 845, "3M": 1326, "1F": 527-72.9, "2F": 765-72.9, "2MAT19": 518, "3MAT19": 516, "1FAT19": 248-36.45, "2FAT19": 486-36.45, "3MAT18": 998}

probs = {"1M": 1/4, "2M": 1/10, "3M": 1/4, "1F": 1/4, "2F": 3/20}

win = 0
progress = 0

for x in first_half:
    for z in second_half:
        progress += 1
        if progress % 10000 == 0:
            print(progress)
        this = baseline
        for monster in x:
            this += times[monster]
        probability = 1/8192
        kills = 13
        for y in z:
            probability *= probs[y]
            new_kills = space[y]
            if y == "2M" or y == "2F" or y == "1F" or y == "3M":
                if kills == 19:
                    y += "AT19"
            if y == "3M" and kills == 18:
                y += "AT18"
            this += scr_steps(60, 60, 20, kills) + 47 + 2.5 + times[y] + 18
            kills += new_kills
        if this < 18000:
            win += probability
