from random import random
from math import floor

def roundrandom(x):
    return round(random()*x)

setsteps_rng = 0.5 # from 0 to 1, floats

def scr_steps(argument0, argument1, argument2):
    global kills
    global setsteps_rng
    populationfactor = (argument2 / (argument2 - kills))
    if populationfactor > 8:
        populationfactor = 8
    steps = (argument0 + round(setsteps_rng*argument1)) * populationfactor
    return floor(steps)+1

def first_half_encounter():
    probability = random()
    if probability > 2:
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

def frogskip():
    probability = random()
    if probability < 0.405:
        return 1
    else:
        return 0

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

at_18 = 'at 18'
at_19 = 'at 19'

encounter_times = {
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
"Froggit Whimsun" + at_19: 270 # Approximation
    }

start_to_unnecessary = 4033 # Run Start ---- Unnecessary Long Hallway Exit (regaining movement in the following room)
toriel_phone_call = 36
falling_pit = 89
getting_up_pit = 50
one_rock_first_phone = 30
one_rock_second_phone = 29
check_sign = 6
talk_rock_part_1 = 112
talk_rock_part_2 = 26
third_half = 4590

flat_execution_time = start_to_unnecessary + toriel_phone_call + falling_pit + getting_up_pit + one_rock_first_phone + \
                      one_rock_second_phone + check_sign + talk_rock_part_1 + talk_rock_part_2 + third_half

first_half_transition = 70
second_half_transition = 70

total_time = 0
first_half_time = 0
second_half_time = 0

frog_skip_save = 91

total_attempts = 0
desired_treshold = 10*60*30
successful_attempts = 0

lowest_time = 20*60*30
highest_time = 0

while total_attempts < 100000:
    total_steps = 0
    encountereds = []
    total_time = 0
    if total_attempts % 1000 == 0:
        print(total_attempts)
    total_attempts += 1
    kills = 0
    while kills < 20:
        if kills < 13:
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
                total_time += (first_half_transition + encounter_time + steps + frogskip_count)
            else:
                total_time += (encounter_time + steps + frogskip_count)
            kills += 1
        else:
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
            total_time += second_half_transition + encounter_time + steps + frogskip_count
        total_steps += steps
    total_time += flat_execution_time
    if total_time < desired_treshold:
        successful_attempts += 1
    if total_time < lowest_time:
        lowest_time = total_time
        lowest_seed = encountereds
    elif total_time > highest_time:
        highest_time = total_time
        highest_seed = encountereds

print(framesToMinutes(lowest_time))
print(framesToMinutes(highest_time))
print(successful_attempts/total_attempts)
print(lowest_seed)
print(highest_seed)
print(total_steps)
