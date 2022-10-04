from math import floor

encounters = ["F", "W"]
alle = []
space = {"F": 1, "W": 1}

def f(combo, lim, length):
    #Function that puts all the combinations of the battlegroups from the encounters list, considering how many monsters per group (from the space dict)
    # and puts all of them into the alle global list
    # (also because of how I made it here the three arguments you call it are an empty list, number of monsters to kill and 0 as the 3rd one)
    for x in encounters:
        new_combo = combo + [x,]
        new_length = length + space[x]
        if new_length >= lim:
            alle.append(new_combo)
        else:
            f(new_combo, lim, new_length)

def scr_steps(argument0, argument1, argument2, kills): # Remake of the gamemaker code but with fixed average value
    populationfactor = (argument2 / (argument2 - kills))
    if populationfactor > 8:
        populationfactor = 8
    steps = (argument0 + 0.5*(argument1)) * populationfactor
    return floor(steps)+1

f([], 13, 0) # Gets first half combinations of froggit and whimsuns

first_half = alle.copy() # Transfer to first_half and clear it for the second half
alle = []

encounters = ["1M", "2M", "3M", "1F", "2F"] # 2nd half encounters, 1f is frog whimsun, 2f is froggit froggit, the rest are moldsmal ones
space = {"1M": 1, "2M": 2, "3M": 3, "1F": 2, "2F": 2}

f([], 7, 0) #this is same as above but this time for 2nd half

second_half = alle.copy()
alle = []

# this baseline is just a bunch of fixed timings, it also includes the first half things like transitioning and steps, since those are the same everytime (with average values)
baseline = 0
baseline += 4057
baseline += 28
baseline += 90
baseline += 50
baseline += 31
baseline += 33
baseline += 5
baseline += 244
baseline += 116
baseline += 27
baseline += 4565
baseline -= 9 + 18

i = 0 # kills simulator
for x in range(1,14):
    baseline += scr_steps(80,40,20,i)
    baseline += 9 + 47 + 2.5
    print(scr_steps(80,40,20,i))
    i += 1

#this times one is important since it pertains to each encounter's timing, frog skips are considered in average (90 * 0.405)
times = {"F": 306.55, "W": 101, "1M": 368, "2M": 845, "3M": 1326, "1F": 527-72.9, "2F": 765-72.9, "2MAT19": 518, "3MAT19": 516, "1FAT19": 248-36.45, "2FAT19": 486-36.45, "3MAT18": 998}

probs = {"1M": 1/10, "2M": 1/4, "3M": 1/4, "1F": 1/4, "2F": 3/20} # 2nd half encounter probabilities

win = 0 # Number of sub 10s
progress = 0 # Just to keep track

for x in first_half: # x and z are a combination of encounters, not the encounters itself
    for z in second_half:
        progress += 1
        if progress % 10000 == 0:
            print(progress)
        this = baseline # "this" is the time for these combinations x and z
        for monster in x:
            this += times[monster] # Just adding the first half time to kill frog and whimsuns
        probability = 1/8192 # first half chance is fixed at 1/2^13
        kills = 13 # kills counter will be used for step counts, start at 13 into first half
        for y in z:
            probability *= probs[y] # Weighting the probability of this outcome
            new_kills = space[y] # Store how many kills will be added after this encounter
            if y == "2M" or y == "2F" or y == "1F" or y == "3M": # These arejust the checks to see if it's at 19 or 18 kills, to include fleeing time
                if kills == 19:
                    y += "AT19"
            if y == "3M" and kills == 18:
                y += "AT18"
            this += scr_steps(60, 60, 20, kills) + 47 + 2.5 + times[y] + 18 # 47 + 2.5 is the average time to get "!" and start battle, 18 is the transition, steps and then the encounter times are added too
            kills += new_kills # Update kill count for future steps
        if this < 18000: # 18000 = 10 minutes in frames
            win += probability
