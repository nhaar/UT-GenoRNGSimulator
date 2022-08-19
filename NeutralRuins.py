from random import random
from math import floor

simulations = 100000

def roundrandom(x): # Simulate Toby's usage of round(random()) in gamemaker
    return round(random()*x)
    
def scr_steps(argument0, argument1, argument2): # Remake of the gamemaker code
    global kills
    populationfactor = (argument2 / (argument2 - kills))
    if populationfactor > 8:
        populationfactor = 8
    steps = (argument0 + roundrandom(argument1)) * populationfactor
    return floor(steps)+1

def first_room_encounterer(): # 80, 120, 20
    probability = random()
    if probability > 0.5:
        return "Froggit"
    else:
        return "Whimsun"

def toriel_attacker():
    probability = random()
    if probability < 0.195:
        return "One Hand"
    elif probability < 0.395:
        return "Two Hands"
    elif probability < 0.595:
        return "Clamped Fireball"
    elif probability < 0.795:
        return "Wide A"
    else:
        return "Wide B"

# EXECUTION TIME

start_to_unnecessary = 3934 # Start of run until first frame of movement in the post long hallway room
walking_in_first_room = 97 # How many steps to exit the room after long hallway
first_room_to_post_napsta = 2127 # The time walking and doing stuff, no encounters included, from the first frame hitting trigger to JOIN the room before 1 rock room, and hitting the trigger to enter the 3 froggit room
post_napsta_to_toriel = 2864 # Hitting the trigger to enter the 3 froggit room to first frame of the Toriel encounter (no encounters)
toriel_end = 2037 # from the first frame you can act after the last scripted encounter to the first frame having movement in the flowey room
ruins_end = 61 # time from first frame of moevemnt post flowy to hitting door

flat_execution = start_to_unnecessary + walking_in_first_room + first_room_to_post_napsta + post_napsta_to_toriel + \
            toriel_end + ruins_end

# Misc execution timing

flee = 98 # Time to flee, no reaction time accounted, includes time getting the encounter
spare = 59 # Same as above, but with insta spare
reaction_time = 12 # Just an estimate to account reaction time
kill_whimsun_time = 159 # Time to kill whimsun, incldues getting the encounter
walking_in_second_room = 86 # Steps in the second room
three_frog_room_steps = 170 #steps in 3 frog room
six_hole_steps = 187 # steps in six hole room
perspectiveA = 105 # steps in first perspective
perspectiveB = 99 # steps in second perspective
perspectiveC = 108 # steps in the third perspective
perspectiveD = 151 # steps in the fourth perspective

killed_whimsun_flowey = 196 # time from first frame in flowey room to gaining movement post flowey dialogue
no_whimsun_flowey = 291 #

# Toriel attack timings
hand_fast = 30
hand_slow = 41
other_ones = 154

# Toriel menuing to spare and mashing the text for each turn
toriel_turn_mash = 22

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

desired_treshold = (6*60 + 54)*30


total_attempts = 0
successful_attempts = 0

lowest_time = 20*60*30
highest_time = 0

while total_attempts < simulations:
    encounters = 0
    total_time = 0
    if total_attempts % 1000 == 0: # Printing out the progress
        print(total_attempts)
    total_attempts += 1
    kills = 0
    first_room = scr_steps(80, 40, 20)
    killed_whimsun = False
    if first_room < walking_in_first_room:
        encounters += 1
        encounter = first_room_encounterer()
        if encounter == "Froggit":
            total_time += flee + reaction_time
        elif encounter == "Whimsun":
            total_time += kill_whimsun_time
            killed_whimsun = True
    second_room = scr_steps(80, 40, 20)
    if second_room < walking_in_second_room:
        encounters += 1
        encounter = first_room_encounterer()
        if encounter == "Froggit":
            if killed_whimsun:
                total_time += flee + reaction_time
            else:
                total_time += flee + reaction_time
        elif encounter == "Whimsun":
            if killed_whimsun:
                total_time += spare + reaction_time
            else:
                total_time += kill_whimsun_time
                killed_whimsun = True
    # 3rd room RNG
    encounter = first_room_encounterer()
    if encounter == "Froggit":
        if killed_whimsun:
            total_time += flee + reaction_time
        else:
            total_time += flee + reaction_time
    elif encounter == "Whimsun":
        if killed_whimsun:
            total_time += spare + reaction_time
        else:
            total_time += kill_whimsun_time
            killed_whimsun = True
    # post napsta rooms
    room_steps = [three_frog_room_steps, perspectiveA]
    for x in room_steps:
        if scr_steps(120, 140, 20) < x:
            encounters += 1
            total_time += flee
    if scr_steps(140, 120, 20) < six_hole_steps:
        encounters += 1
        total_time += flee
    perspectives = [perspectiveB, perspectiveC, perspectiveD]
    for x in perspectives:
        if scr_steps(90, 100, 20) < x:
            encounters += 1
            total_time += flee
    total_time += toriel_turn_mash * 12
    hp = 20
    current_attack = 0
    nine_turn_setup = 0
    attacks = []
    while current_attack < 12:
        current_attack += 1
        attack = toriel_attacker()
        attacks.append(attack)
        if current_attack == 12 and hp > 2: # Simulate players lowering HP for the last turn
            total_time += hand_fast
            hp = 1
        elif hp == 1: # After exhausted hands
            total_time += other_ones
        else:
            if attack == "Wide A" or attack == "Wide B" or attack == "Clamped Fireball":
                if hp == 2:
                    total_time += hand_fast
                    hp = 1
                else:
                    total_time += other_ones
            elif attack == "One Hand":
                total_time += hand_slow
                if hp < 8:
                    hp -= 1
                else:
                    hp -= 3
            elif attack == "Two Hands":
                if nine_turn_setup == 2:
                    total_time += hand_fast
                    if hp <8:
                        hp -= 1
                    else:
                        hp -= 4
                elif nine_turn_setup < 2:
                    if hp < 8 :
                        hp -= 1
                    else:
                        total_time += hand_slow
                        hp -= 3
                        nine_turn_setup += 1
    if killed_whimsun:
        total_time += killed_whimsun_flowey
    else:
        total_time += no_whimsun_flowey
    total_time += flat_execution
    if total_time < desired_treshold:
        successful_attempts += 1
    if total_time < lowest_time:
        lowest_time = total_time
        best_attacks = attacks
        best_encounters = encounters
    elif total_time > highest_time:
        worst_attacks = attacks
        worst_encounters = encounters
        highest_time = total_time

print(framesToMinutes(lowest_time))
print(worst_attacks)
print(worst_encounters)
print(framesToMinutes(highest_time))
print(best_attacks)
print(best_encounters)
print(successful_attempts/total_attempts)
