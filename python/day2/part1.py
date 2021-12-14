#!/usr/bin/env python3

with open("input.txt", "r") as input:
    lines = input.readlines()
    
    horiz = 0
    depth = 0

    for line in lines:
        dir, val = line.split(" ")
        dir = dir
        val = int(val)
        if dir == "forward":
            horiz += val
        elif dir == "down":
            depth += val
        elif dir == "up":
            depth -= val

    print(f"Horizontal position: {horiz}")
    print(f"Depth: {depth}")
    print(f"{horiz * depth}")
