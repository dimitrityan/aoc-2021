#!/usr/bin/env python3

with open("input.txt", "r") as input:
    lines = input.readlines()
    
    horiz = 0
    depth = 0
    aim = 0

    for line in lines:
        dir, val = line.split(" ")
        dir = dir
        val = int(val)
        if dir == "forward":
            horiz += val
            depth += aim * val
        elif dir == "down":
            aim += val
        elif dir == "up":
            aim -= val

    print(f"Horizontal position: {horiz}")
    print(f"Depth: {depth}")
    print(f"{horiz * depth}")
