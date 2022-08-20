from random import random
from math import floor


# NUMBER OF SIMULATIONS
simulations = 1

def roundrandom(x): # Simulate Toby's usage of round(random()) in gamemaker
    return round(random()*x)

def scr_steps(argument0, argument1, argument2): # Remake of the gamemaker code
    global kills
    populationfactor = (argument2 / (argument2 - kills))
    if populationfactor > 8:
        populationfactor = 8
    steps = (argument0 + round(0.5 * argument1)) * populationfactor
    return floor(steps)+1

# The following two functions calculate the encounters based on their probability

def first_half_encounter():
    probability = random()
    if probability > 0.5:
        return "Froggit"
    else:
        return "Whimsun"

def second_half_encounter():
    probability = random()
    if probability < 0.25:
        return "Froggit Whimsun"
    elif probability < 0.5:
        return "1x Moldsmall"
    elif probability < 0.75:
        return "3x Moldsmall"
    elif probability < 0.9:
        return "2x Froggit"
    else:
        return "2x Moldsmall"

def snowdin_encounterer():
    probability = random()
    if probability < 0.5333:
        return "Icecap Jerry"
    else:
        return "Snowdrake Jerry"

def waterfall_glowing_encounterer():
    probability = random()
    if probability < 0.2667:
        return "Woshua"
    elif probability < 0.5334:
        return "Shoes Moldsmall"
    elif probability < 0.7334:
        return "Aaron"
    else:
        return "Woshua Aaron"

def waterfall_grind():
    probability = random()
    if probability < 0.3333:
        return "Woshua Aaron"
    elif probability < 0.7333:
        return "Woshua Moldbygg"
    else:
        return "Temmie"

def frogskip(): # Rolls for frogskip and returns 1 if you get it, 0 if not (this result is used as an integer)
    probability = random()
    if probability < 0.405:
        return 1
    else:
        return 0

def dogskip():
    probability = random()
    if probability < 0.5:
        return 1
    else:
        return 0

#All times are written in frames by default, the following function converts to a more readable value

def ftm(x):
    seconds = x/30
    minutes = floor(seconds/60)
    seconds = seconds - minutes * 60
    if seconds < 10:
        seconds = '0' + str(seconds)
    else:
        seconds = str(seconds)
    minutes = str(minutes)
    return minutes + ":" + seconds

# At 18 and at 19 are ways to take into account that an encounter's course of actions change, if for example
# it has 3 monsters but you are at 18 kills

at_18 = 'at 18'
at_19 = 'at 19'

# The time for each encounter is from:
# - First frame in battle
# - First frame outside battle

encounter_times = {
#
# RUINS ENCOUNTERS
#
#
"Froggit": 368, #link's run
"Whimsun": 104 ,#link's run
"1x Moldsmall": 369, #TGH's 1:05:37
"2x Moldsmall": 840, #Approximation
"3x Moldsmall": 1319, # link's run
"Froggit Whimsun": 520, # link's run
"2x Froggit": 747, # From link in this race https://www.twitch.tv/videos/1565078950?t=00h11m13s
# --------- Separating normal ones from "at x" ones
"2x Moldsmall" + at_19: 630, # Approximation
"3x Moldsmall" + at_18: 1080, # Approximation
"3x Moldsmall" + at_19: 630, # Approximation
"2x Froggit" + at_19: 630, # Approximation
"Froggit Whimsun" + at_19: 270, # Approximation
#
# SNOWDIN ENCOUNTERS
#
#
"Snowdrake": 340,
"Icecap Jerry": 128,
"Snowdrake Jerry": 691,
#
# WATERFALL ENCOUNTERS
#
#
"Shoes Moldsmall": 381,
"Aaron": 357, # These are the BALLET SHOES times, tough glove ones aren't considered
"Woshua": 127,
"Woshua Aaron": 624,
"Woshua Aaron Scripted": 648,
"Temmie": 108,
"Woshua Moldbygg": 430 ,
"Sus Mold" : 253
    }

# These are the execution times, all adjusted from link's 1:03:38

# RUINS TIMES

start_to_unnecessary = 4033 # Run Start ---- Unnecessary Long Hallway Exit (regaining movement in the following room)
toriel_phone_call = 36 # Time to mash the first toriel phone call
falling_pit = 89 # Time falling into the pit
getting_up_pit = 50 # Time getting up from the pit
one_rock_first_phone = 30 # Time to mash first phone call in 1 rock room
one_rock_second_phone = 29 # Time to mash second phone call in 1 rock room
check_sign = 6 # Time to check the sign in 1 rock room
talk_rock_part_1 = 112 # Time talking with the rock in 3 rock room (before going right)
talk_rock_part_2 = 26 # Time talking with the rock in 3 rock room (after going right)
third_half = 4590 # First frame after killed last monster ----- Touch Toriel Door

ruins_execution = start_to_unnecessary + toriel_phone_call + falling_pit + getting_up_pit + one_rock_first_phone + \
                      one_rock_second_phone + check_sign + talk_rock_part_1 + talk_rock_part_2 + third_half

# SNOWDIWN TIMES

snowdin_strat = 3290 # Touch Ruins Door ----- First frame of movement in Snowdin Tough Glove box
savepointinteract = 6 # Savepoint in room with box
equip_glove = 39 # Equip item + get from box
snowding_rock_to_dogi = 3037 # From leaving Snowdrake's scripted encounter to entering the dogi room
dogi_to_greater = 3270 # From leaving first non scripted encoutner to encountering greaterdog
deadly_bridge = 1159 # leaving greater dog to touching snowdin town enter door
exit_snowdin = 2238 # movement from last encounter to splitting Snowdin)

snowdin_execution = snowdin_strat + savepointinteract + equip_glove + snowding_rock_to_dogi + \
                    dogi_to_greater + deadly_bridge + exit_snowdin

# WATERFALL TIMES
waterfall_start = 497 #Touch Out of Snowdin Transition - Touch before SGS transition
sgs_time = 566 # Touch door before SGS transition --- have movement in the room after SGS
woshua_aaron_walk = 1761 # Have movement in the room after SGS --- Have movement in the first spears 1 room
spears1 = 830 # Have movement in the first spears 2 room --- Have movement in the last spears 2 room (with seagrass)
punch_card_walk = 1720# have movement in the last spears 2 room --- Have movement in the BIG ROOM (pre onionsan)
tough_glove_moldsmall = 388 # get encounter alert --- gain movement post battle
shoes_segment = 756 # gaing movement post moldsmall battle, equip shoes, leave room + the step counter of the BIG ROOM
up_to_grind = 7377 # from touching the room transition into onion sans ---- gaining movement in the room with scritped temmie
post_grind = 8739 # touching room transition OUT OF CRYSTAL MAZE ---- Touching room transition outside of Undyne battle (quick kill segment)

# Transition times are a measurement of: Room transition + encountering animation

first_half_transition = 70
second_half_transition = 70
snowdin_right_side_transition = 31
snowdin_left_side_transition = 26
waterfall_transition = 10

frog_skip_save = 91 # How many frames running into the frog saves, comapared it from link's 1:03:38
greater_dog_fight = 483 # The fight with no dog skips
dog_skip_save = 74 #Greater Dog's attack time save
jerry_kill = 969 # If you need to kill jerry, the extra time taken
encountering_time = 52 # Time you get notified and start battle

mushroom_maze_steps = 348
dark_crystal_steps = 642

total_attempts = 0 # Keep track of simulation number
desired_treshold = (22*60)*30 # To calculate the probability of the treshold you want, by default I put 10 minutes here
successful_attempts = 0 # Runs that beat the treshold above


# high and low numbers so that we can find the lowest and highest times from each
lowest_time = 200*60*30
highest_time = 0

while total_attempts < simulations:
    encountereds = [] # Keep track of the encounters this seed
    total_time = 0 # This will be the time for this simulation
    if total_attempts % 1000 == 0: # Printing out the progress
        print(total_attempts)
    total_attempts += 1
    # RUINS CODE
    #
    #
    ruins_time = 0
    kills = 0
    while kills < 20:
        if kills < 13: # Code for the first half
            steps = scr_steps(80, 40, 20)
            if kills == 0 and steps > 97: #Exception for first encounter because you can get it before reaching end
                steps = 97
            encounter = first_half_encounter()
            encountereds.append(encounter)
            frogskip_count = 0
            if encounter == "Froggit":
                frogskip_count = -(frog_skip_save * frogskip())
            encounter_time = encounter_times[encounter]
            if kills != 0: #First kill has no transition, basically
                ruins_time += (first_half_transition + encounter_time + steps + frogskip_count)
            else:
                ruins_time += (encounter_time + steps + frogskip_count)
            kills += 1
        else: # Code for 2nd half
            steps = scr_steps(60, 60, 20)
            encounter = second_half_encounter()
            encountereds.append(encounter)
            if encounter == "2x Moldsmall" or encounter == "2x Froggit" or encounter == "Froggit Whimsun":
                if kills == 19:
                    encounter += at_19
                kills += 2
            elif encounter == "3x Moldsmall":
                if kills == 18:
                    encounter += at_18
                elif kills == 19:
                    encounter += at_19
                kills += 3
            if encounter == "1x Moldsmall":
                kills += 1
            frogskip_count = 0
            if encounter == "Froggit Whimsun" or encounter == "2x Froggit":
                frogskip_count = -(frog_skip_save * (frogskip() + frogskip()))
            encounter_time = encounter_times[encounter]
            ruins_time += second_half_transition + encounter_time + steps + frogskip_count
    ruins_time += ruins_execution
    all_encountereds = {}
    all_encountereds['Ruins'] = encountereds
    # SNOWDIN CODE
    #
    #
    encountereds = []
    kills = 0
    snowdin_time = 0
    #Scripted snodrake
    steps = scr_steps(120, 30, 16)
    snowdin_time += encounter_times["Snowdrake"] + encountering_time + steps
    encounter = snowdin_encounterer() # Scripted at dogi
    kills = 3
    snowdin_time += scr_steps(220, 30, 16)
    if encounter == "Icecap Jerry":
        encountereds.append(encounter)
        snowdin_time += encounter_times[encounter]
        kills += 1
    elif encounter == "Snowdrake Jerry":
        encountereds.append(encounter)
        snowdin_time += encounter_times[encounter]
        kills += 2
    snowdin_time += greater_dog_fight - (dog_skip_save * (dogskip() + dogskip())) # Greater Dog Fight
    while kills < 16: # Bridge grind
        snowdin_time += encountering_time
        encounter = snowdin_encounterer()
        steps = scr_steps(120, 30, 16)
        encountereds.append(encounter)
        if kills < 10:
            snowdin_time += snowdin_right_side_transition
        else:
            snowdin_time += snowdin_left_side_transition
        snowdin_time += steps
        if encounter == 'Snowdrake Jerry':
            snowdin_time += encounter_times['Snowdrake Jerry']
            kills += 2
            if (kills - 2) == 13:
                snowdin_time += jerry_kill
                kills += 1
        elif encounter == 'Icecap Jerry':
            snowdin_time += encounter_times[encounter]
            kills += 1
            if (kills - 1) == 14:
                kills += 1
                snowdin_time += jerry_kill
    snowdin_time += snowdin_execution
    all_encountereds["Snowdin"] = encountereds
    #
    # WATERFALL CODE
    #
    #
    #
    SEED = ['Shoes Moldsmall', 'Temmie', 'Woshua Moldbygg']
    kills = 0
    encountereds = []
    waterfall_time = waterfall_start
    print("Start (enter sgs)", ftm(waterfall_time))
    waterfall_time += sgs_time
    print("SGS (exit", ftm(waterfall_time))
    waterfall_time += woshua_aaron_walk
    print("Enter spears 1", ftm(waterfall_time))
    kills += 2 # Woshua and Aaron
    waterfall_time += spears1
    print("Exit main spears 1", ftm(waterfall_time))
    waterfall_time += punch_card_walk
    print("Enter big room",ftm(waterfall_time))
    ##Big Room encounter + steps RNG (with tough glove)
    waterfall_time += scr_steps(360, 30, 18) + tough_glove_moldsmall
    print("Exit scripted double mold", ftm(waterfall_time))
    kills += 2 # Double Mold
    waterfall_time += shoes_segment
    #BIG ROOM encounter RNG
    encounter = SEED[0]
    if encounter == 'Aaron' or encounter == 'Woshua':
        kills += 1
    else:
        kills += 2
    waterfall_time += encountering_time + encounter_times[encounter]
    print("Enter onion sans", ftm(waterfall_time))
    waterfall_time += up_to_grind
    print("Enter Grind room", ftm(waterfall_time))
    kills += 2 # Shyren and Glad Dummy
    # Scripted Temmie
    waterfall_time += scr_steps(60, 20, 18)
    waterfall_time += encounter_times['Temmie'] + encountering_time
    print("Kills cripted temmie", ftm(waterfall_time))
    # First scripted encounter
    waterfall_time += scr_steps(120, 50, 18)
    kills += 1 # Temmie (need to computer it after this steps)
    encounter = "Sus Mold"
    waterfall_time += encountering_time + encounter_times[encounter]
    print("Kill scripted sus mold", ftm(waterfall_time))
    kills += 2 # Moldsmall and Moldbygg
    scripted_encounters = 1
    current_room = 'L' # for right, the room you grinded the PREVIOUS encounter
    first_maze = False
    second_maze = False
    encounters = 0
    while kills < 18:
        waterfall_time += waterfall_transition + encountering_time # Standard time for each encounter
        if kills > 13:
            if first_maze == False:
                first_maze = True
                if current_room == 'R':
                    waterfall_time += waterfall_transition # EXTRA TRANSITION
                steps = scr_steps(60, 20, 18)
                if steps < mushroom_maze_steps:
                    steps = mushroom_maze_steps
            else:
                if second_maze == False:
                    waterfall_time += waterfall_transition # EXTRA TRANSITION
                    if kills > 15:
                        second_maze = True
                        steps = scr_steps(60, 20, 18)
                        if steps < dark_crystal_steps:
                            steps = dark_crystal_steps
                    else:
                        steps = scr_steps(60, 20, 18)
        else:
            steps = scr_steps(60, 20, 18)
        waterfall_time += steps
        if scripted_encounters == 1:
            current_room = 'R'
            waterfall_time += encounter_times["Woshua Aaron Scripted"]
            scripted_encounters = 2
            kills += 2
        elif scripted_encounters == 2:
            current_room = 'L'
            waterfall_time += encounter_times["Woshua Moldbygg"]
            scripted_encounters = 3
            kills += 2
        else:
            if first_maze == False:
                if current_room == 'R':
                    current_room = 'L'
                else:
                    current_room = 'R'
            encounters += 1
            encounter = SEED[1]
            if encounter == 'Temmie':
                kills += 1
            else:
                kills += 2
            waterfall_time += encounter_times[encounter]
        print(kills, 'Kills', ftm(waterfall_time))
    waterfall_time += post_grind
    print("Post Grind", ftm(waterfall_time))
    all_encountereds['Waterfall'] = encountereds
    ruins_time = 0
    snowdin_time = (21*60+47.3)*30
    total_time = ruins_time + snowdin_time + waterfall_time
    if total_time < desired_treshold:
        successful_attempts += 1
    if total_time < lowest_time:
        lowest_time = total_time
        lowest_seed = all_encountereds
    elif total_time > highest_time:
        highest_time = total_time
        highest_seed = all_encountereds
    
# Results

print(framesToMinutes(lowest_time))
print(framesToMinutes(highest_time))
print(successful_attempts/total_attempts)
print(lowest_seed)
print(highest_seed)
