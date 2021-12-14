#!/usr/bin/env python3

# Naive approach
# Column-wise count of 1 and 0, comparison at the end
# Runtime: c * r, num of columns = c, num of rows = r

with open("input.txt", "r") as input:
    lines = input.readlines()
    first_val = lines[0]
    gamma = "0b"
    epsilon = "0b"
    for c in range(0, len(first_val)):
        if lines[0][c] == "\n": continue
        num_0 = 0
        num_1 = 0
        for r in range(0, len(lines)):
            bit = int(lines[r][c])
            if bit == 0: num_0 += 1
            elif bit == 1: num_1 += 1
        
        if num_0 > num_1:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    print(gamma * epsilon)