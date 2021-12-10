#!/usr/bin/env python3

def main():
    with open("input.txt", "r") as input:
        lines = input.read().splitlines()[0]
        positions = list(map(int, lines.split(",")))
        pos_to_times = {}
        min = positions[0]
        max = positions[0]

        for position in positions:
            if position < min:
                min = position
            if position > max:
                max = position    
            if position in pos_to_times:
                pos_to_times[position] += 1
            else:
                pos_to_times[position] = 1
        
        current_min = None
        current_min_pos = 0
        for x in range(min, max + 1):
            dist = 0
            for pos in pos_to_times.keys():
                occ = pos_to_times[pos]
                if x > pos:
                    dist += (x - pos) * occ
                if x <= pos:
                    dist += (pos - x) * occ
            if current_min is None:
                current_min = dist
                current_min_pos = x
            else:
                if dist < current_min:
                    current_min = dist
                    current_min_pos = x
        print(f"Minimal fuel usage ({current_min}) at position {current_min_pos}")

main()