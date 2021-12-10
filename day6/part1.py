#!/usr/bin/env python3

RESET_TIME = 6
NEW_FISH_TIME = 8

def init_first_map(initial_times):
    map = {}
    for time in initial_times:
        if time in map:
            map[time] += 1
        else:
            map[time] = 1
    return map

def main():
    with open("input.txt", "r") as input:
        lines = input.read().splitlines()[0]
        initial_times = lines.split(",")
        initial_times = list(map(int, initial_times))
        
        # How many laternfish after 80 days
        times_to_num = init_first_map(initial_times)
        for _ in range(0, 80):
            new_times_to_num = {}
            for time in times_to_num.keys():
                num_of_fish = times_to_num[time]
                if time == 0:
                    if RESET_TIME in new_times_to_num:
                        new_times_to_num[RESET_TIME] += times_to_num[time]
                    else:
                        new_times_to_num[RESET_TIME] = times_to_num[time]
                    new_times_to_num[NEW_FISH_TIME] = times_to_num[time]
                else:
                    new_time = time - 1
                    if new_time in new_times_to_num:
                        new_times_to_num[new_time] += times_to_num[time]
                    else:
                        new_times_to_num[new_time] = times_to_num[time]
            times_to_num = new_times_to_num
        
        fish_counter = 0
        for time in times_to_num.keys():
            fish_counter += times_to_num[time]
        print(f"Number of fish: {fish_counter}")

main()