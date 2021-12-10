#!/usr/bin/env python3

with open("input.txt", "r") as input:
    lines = input.readlines()

    prev = None
    counter = 0

    for i in range(0, len(lines)):
        depth = int(lines[i])
        if i == 0:
            prev = depth
            continue
        if depth > prev:
            counter += 1
        prev = depth
        
    print (counter)