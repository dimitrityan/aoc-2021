#!/usr/bin/env python3

with open("input.txt", "r") as input:
    lines = input.read().splitlines()
    rows_to_check = range(0, len(lines))
    row_list = range(0, len(lines))
    oxy_value = -1
    scrubber_value = -1

    for c in range(0, len(lines[0])):
        list_0 = []
        list_1 = []
        count_0 = 0
        count_1 = 0
        for r in row_list:
            bit = int(lines[r][c])
            if bit == 0:
                count_0 += 1
                list_0.append(r)
            elif bit == 1:
                count_1 += 1
                list_1.append(r)
        if count_0 > count_1:
            row_list = list_0
        elif count_1 >= count_0:
            row_list = list_1
        if len(row_list) == 1:
            oxy_value = int(lines[row_list[0]], 2)
    
    # Reset initial row list to all input lines
    row_list = range(0, len(lines))
    for c in range(0, len(lines[0])):
        list_0 = []
        list_1 = []
        count_0 = 0
        count_1 = 0
        for r in row_list:
            bit = int(lines[r][c])
            if bit == 0:
                count_0 += 1
                list_0.append(r)
            elif bit == 1:
                count_1 += 1
                list_1.append(r)
        if count_0 > count_1:
            row_list = list_1
        elif count_1 >= count_0:
            row_list = list_0
        if len(row_list) == 1:
            scrubber_value = int(lines[row_list[0]], 2)
    res = oxy_value * scrubber_value
    print(f"Result: {res}")
