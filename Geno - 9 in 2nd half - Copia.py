from random import random
from math import floor


# CONTROL VARIABLE
# Number of runs
simulations = 1000000

#Choose the area:
#1 = Ruins
#2 = Snowdin
#3 = Waterfall
#4 = Core
#5 = Full Game

area = 1

#Choose the percentage treshold (frames)

desired_treshold = (10*60)*30


def roundrandom(x): # Simulate Toby's usage of round(random()) in gamemaker
    return round(random()*x)

def scr_steps(argument0, argument1, argument2): # Remake of the gamemaker code
    global kills
    populationfactor = (argument2 / (argument2 - kills))
    if populationfactor > 8:
        populationfactor = 8
    steps = (argument0 + roundrandom(argument1)) * populationfactor
    return floor(steps)+1

# The following functions calculate the encounters based on their probability

def first_half_encounter(): # Ruins
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

def core_encounterer():
    probability = random()
    if probability < 0.1333:
        return "Final Froggit Astigmatism"
    elif probability < 0.3333:
        return "Whimsalot Final Froggit"
    elif probability < 0.5333:
        return "Whimsalot Astigmatism"
    elif probability < 0.7333:
        return "Knight Knight Madjick"
    elif probability < 0.8666:
        return "Core Triple"
    elif probability < 0.9333:
        return "Knight Knight"
    else:
        return "Madjick"

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

def encountering_time():
    return 47 + roundrandom(5)

#All times are written in frames by default, the following function converts to a more readable value

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

# At 18 and at 19 are ways to take into account that an encounter's course of actions change, if for example
# it has 3 monsters but you are at 18 kills

at_18 = 'at 18'
at_19 = 'at 19'

# The time for each encounter is from:
# - First frame in battle
# - First frame outside battle

ruins_encounters = {
#
# RUINS ENCOUNTERS
#
#
"Froggit" + "LV2": 346,
"Froggit" + "LV3": 328,
"Whimsun": 103 ,
"1x Moldsmall": 375,
"2x Moldsmall": 845,
"3x Moldsmall": 1326,
"Froggit Whimsun": 537,
"2x Froggit": 782,
# --------- Separating normal ones from "fleeing" ones
"2x Moldsmall" + at_19: 522,
"3x Moldsmall" + at_18: 1000,
"3x Moldsmall" + at_19: 522,
"2x Froggit" + at_19: 470,
"Froggit Whimsun" + at_19: 260
}


encounter_times = {
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
"Sus Mold" : 253,
#
# CORE ENCOUNTERS
#
#
"Whimsalot Astigmatism": 430,
"Final Froggit Astigmatism": 431,
"Knight Knight Madjick": 435,
"Knight Knight": 150,
"Whimsalot Final Froggit": 433,
"Core Triple": 714,
"Madjick": 150,
"Astigmatism": 150
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

ruins_execution = 0

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

# HOTLAND TIMES
#--- (check the code above core)

# CORE TIMES
core_start = 840
walk_to_near_warriors = 96
warriors_path = 2311 # From exitting final encounter before warriors path to gaining movement in the room you can grind AFTER warriors path
exit_warriors_path_nobody_came = 471 # Gaining movement in the last room you can grind (coming back) --- Touching the door trigger to enter room with savepoint (INCLUDES BUT NOBODY CAME TIMES
walk_back_no_nobody_came = 143 # Gaining movement in the last room you can grind (coming back) --- Gaining movement in core bridge ( NO NOBODY CAMES IN HERE)
core_end = 874

# Transition times are a measurement of: Room transition + encountering animation

first_half_transition = 9
second_half_transition = 19
snowdin_right_side_transition = 31
snowdin_left_side_transition = 26
waterfall_transition = 10
core_transition = 20

# STEPS FOR WALKING ROOMS
leaf_pile_steps = 97

# MISCELANEOUS
frog_skip_save = 90 # How many frames running into the frog saves, comapared it from link's 1:03:38
greater_dog_fight = 483 # The fight with no dog skips
dog_skip_save = 74 #Greater Dog's attack time save
jerry_kill = 969 # If you need to kill jerry, the extra time taken

double_flee = 10 * 30
triple_flee_double = 10 * 30
triple_flee_single =  20 * 30

mushroom_maze_steps = 348
dark_crystal_steps = 642

total_attempts = 0 # Keep track of simulation number
successful_attempts = 0 # Runs that beat the treshold above


# high and low numbers so that we can find the lowest and highest times from each
lowest_time = 200*60*30
highest_time = 0

def RuinsSimulate(): # Ruins Code
    global all_encountereds
    global total_time
    global kills
    ruins_time = 0
    ruins_time += 4057 # Run Start ---- Unnecessary Long Hallway Exit (regaining movement in the first grindable room)
    encountereds = []
    kills = 0
    lv = 2
    exp = 10
    while kills < 20:
        if exp >= 30:
            lv = 3
        if kills < 11: # Code for first half
            steps = scr_steps(80, 40, 20)
            if kills == 0: #Exception for first encounter because you can get it before reaching end + phone call
                ruins_time += 28 # Time to mash the first toriel phone call
                if steps < leaf_pile_steps:
                    steps = leaf_pile_steps
            elif kills == 9: # Going to the right
                ruins_time += 90 # Time falling into the pit
                ruins_time += 50 # Time getting up from the pit
            elif kills == 10: # Going to the right
                ruins_time += 31 # Time to mash first phone call in 1 rock room
                ruins_time += 33 # Time to mash second phone call in 1 rock room
                ruins_time += 5 # Time to check the sign in 1 rock room
            encounter = first_half_encounter()
            encountereds.append(encounter)
            frogskip_count = 0
            if encounter == "Froggit":
                if lv == 2:
                    encounter += 'LV2'
                elif lv == 3:
                    encounter += 'LV3'
                frogskip_count = -(frog_skip_save * frogskip())
                exp += 4
            else:
                exp += 3
            encounter_time = ruins_encounters[encounter]
            if kills != 0: #First kill has no transition, basically
                ruins_time += (first_half_transition + steps + encountering_time() + encounter_time + frogskip_count)
            else:
                ruins_time += (steps + encountering_time() + encounter_time + frogskip_count)
            kills += 1
        else: # Code for 2nd half
            if kills == 13: # Going through the leaf maze
                ruins_time += 244 # Gaining movement from killing encounter before and gaining movement in leaf maze
                ruins_time += 116 # Time talking with the rock in 3 rock room (before going right)
                ruins_time += 27 # Time talking with the rock in 3 rock room (after going right)
                ruins_time -= second_half_transition # Transition is meaningless for this first one
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
                if kills == 19:
                    frogskip_count = -(frog_skip_save * (frogskip()))
                else:
                    frogskip_count = -(frog_skip_save * (frogskip() + frogskip()))
            encounter_time = ruins_encounters[encounter]
            ruins_time += second_half_transition + steps + encountering_time() + encounter_time + frogskip_count
    ruins_time += 4565 # First frame after killed last monster ----- Touch Toriel Door
    all_encountereds['Ruins'] = encountereds
    total_time += ruins_time
    return ruins_time

def SnowdinSimulate(): #Snowdin Code
    global all_encountereds
    global total_time
    global kills
    encountereds = []
    kills = 0
    snowdin_time = 0
    #Scripted snodrake
    steps = scr_steps(120, 30, 16)
    snowdin_time += encounter_times["Snowdrake"] + encountering_time() + steps
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
        snowdin_time += encountering_time()
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
    total_time += snowdin_time

def WaterfallSimulate(): # Waterfall Code
    global all_encountereds
    global total_time
    global kills
    kills = 0
    encountereds = []
    waterfall_time = waterfall_start
    waterfall_time += sgs_time
    waterfall_time += woshua_aaron_walk
    kills += 2 # Woshua and Aaron
    waterfall_time += spears1
    waterfall_time += punch_card_walk 
    ##Big Room encounter + steps RNG (with tough glove)
    waterfall_time += scr_steps(360, 30, 18) + tough_glove_moldsmall
    kills += 2 # Double Mold
    waterfall_time += shoes_segment
    #BIG ROOM encounter RNG
    encounter = waterfall_glowing_encounterer()
    encountereds.append(encounter)
    if encounter == 'Aaron' or encounter == 'Woshua':
        kills += 1
    else:
        kills += 2
    waterfall_time += encountering_time() + encounter_times[encounter]
    waterfall_time += up_to_grind
    kills += 2 # Shyren and Glad Dummy
    # Scripted Temmie
    waterfall_time += scr_steps(60, 20, 18)
    waterfall_time += encounter_times['Temmie'] + encountering_time() 
    # First scripted encounter
    waterfall_time += scr_steps(120, 50, 18)
    kills += 1 # Temmie (need to computer it after this steps)
    encounter = "Sus Mold"
    waterfall_time += encountering_time() + encounter_times[encounter]
    kills += 2 # Moldsmall and Moldbygg
    scripted_encounters = 1
    current_room = 'L' # for right, the room you grinded the PREVIOUS encounter
    first_maze = False
    second_maze = False
    while kills < 18:
        waterfall_time += waterfall_transition + encountering_time() # Standard time for each encounter
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
                        steps = scr_steps(120, 50, 18)
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
            encounter = waterfall_grind()
            encountereds.append(encounter)
            if encounter == 'Temmie':
                kills += 1
            else:
                kills += 2
            waterfall_time += encounter_times[encounter]
            if (kills - 2) == 17 and encounter != 'Temmie':
                waterfall_time -= double_flee
    waterfall_time += post_grind
    all_encountereds['Waterfall'] = encountereds
    total_time += waterfall_time

def HotlandSimulate():
    global total_time
    total_time += 7161 # touching leaving undyne door  --- touch leaving muffet door

def CoreSimulate():
    global total_time
    global all_encountereds
    global kills
    core_time = 0
    kills = 5
    core_time += core_start
    encountereds = []
    #
    near_elevator = True
    near_warriors = False
    warriors_kills = 0
    while kills < 40:
        if kills < 14:
            steps = scr_steps(70, 50, 40)
            if kills == 5: # Special case because just got here
                core_time += steps + encountering_time() + encounter_times["Astigmatism"]
                kills = 6
            else:
                if kills == 6:
                    encounter = "Whimsalot Final Froggit"
                    kills = 8
                elif kills == 8:
                    encounter = "Whimsalot Astigmatism"
                    kills = 10
                elif kills == 10:
                    encounter = "Final Froggit Astigmatism"
                    kills = 12
                elif kills == 12:
                    encounter = "Knight Knight Madjick"
                    kills = 14
                core_time += core_transition + steps + encountering_time() + encounter_times[encounter]
        elif kills < 32 or kills == 39:
            if kills > 26:
                if near_elevator:
                    near_elevator = False
                else:
                    if not near_warriors:
                        near_warrios = True
                        core_time += walk_to_near_warriors - core_transition # Remove core_transition cuz its meaningless
            elif kills == 39:
                core_time += walk_back_no_nobody_came - core_transition
            steps = scr_steps(70, 50, 40)
            encounter = core_encounterer()
            core_time += core_transition + steps + encountering_time() + encounter_times[encounter]
            if encounter == "Madjick" or encounter == "Knight Knight":
                kills += 1
            elif encounter == "Core Triple":
                if kills == 39:
                    core_time -= triple_flee_single
                if kills == 31:
                    core_time -= triple_flee_double
                kills += 3
            else:
                if kills == 39:
                    core_time -= double_flee
                kills += 2
            encountereds.append(encounter)
        elif kills >= 32:
            if warriors_kills == 0:
                core_time += warriors_path
                kills += 7
                if kills == 40:
                    core_time += exit_warriors_path_nobody_came
    core_time += core_end
    all_encountereds["Core"] = encountereds
    total_time += core_time

def EndGameSimulate():
    global total_time
    new_home_time = 20473 # Exit mettaton room (touch door) --- exit sans hallway
    chara_time = 5004 # Exit sans hallway -- End run
    total_time += new_home_time + chara_time # touching leaving undyne door  --- touch leaving muffet door

while total_attempts < simulations:
    all_encountereds = {} # Keep track of the encounters this seed
    total_time = 0 # This will be the time for this simulation
    if total_attempts % 10000 == 0: # Printing out the progress
        print(total_attempts)
    total_attempts += 1
    if area == 1:
        RuinsSimulate()
    elif area == 2:
        SnowdinSimulate()
    elif area == 3:
        WaterfallSimulate()
    elif area == 4:
        CoreSimulate()
    elif area == 5:
        RuinsSimulate()
        SnowdinSimulate()
        WaterfallSimulate()
        HotlandSimulate()
        CoreSimulate()
        EndGameSimulate()
    if total_time < desired_treshold:
        successful_attempts += 1
    if total_time < lowest_time:
        lowest_time = total_time
        lowest_seed = all_encountereds
    elif total_time > highest_time:
        highest_time = total_time
        highest_seed = all_encountereds
    
# Results

print('------------', simulations, ' runs results', '------------')
print('Fatest Time:', framesToMinutes(lowest_time))
print('Slowest Time:', framesToMinutes(highest_time))
print('Percentage of runs below', framesToMinutes(desired_treshold),'=', str((successful_attempts/total_attempts) * 100) + "%")
for x in [lowest_seed, highest_seed]:
    if x == lowest_seed:
        print('\nEncounters for the fastest time\n')
    else:
        print('\nEncounters for the slowest time\n')
    if area == 1:
        areas = ['Ruins']
    elif area == 2:
        areas = ['Snowdin']
    elif area == 3:
        alreas = ['Waterfall']
    elif area == 4:
        areas = ['Core']
    elif area == 5:
        areas = ['Ruins', 'Snowdin', 'Waterfall', 'Core']
    for y in areas:
        these_encounters = x[y]
        string_encounters = ''
        for z in these_encounters:
            string_encounters += z + ', '
        string_encounters = string_encounters[:-2]
        print(y, '        ', string_encounters)
