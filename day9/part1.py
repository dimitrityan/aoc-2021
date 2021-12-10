#!/usr/bin/env python3
import functools

def main():
    with open("day9/input.txt", "r") as input:
        lines = input.read().splitlines()
        low_points =[]
        for r in range(0, len(lines)):
            for c in range(0, len(lines[r])):
                cur_depth = int(lines[r][c])
                if c-1 >= 0 and int(lines[r][c-1]) <= cur_depth:
                    continue
                if c+1 < len(lines[r]) and int(lines[r][c+1]) <= cur_depth:
                    continue
                if r-1 >= 0 and int(lines[r-1][c]) <= cur_depth:
                    continue
                if r+1 < len(lines) and int(lines[r+1][c]) <= cur_depth:
                    continue
                low_points.append(cur_depth)
        print(f"Result: {functools.reduce(lambda x, y: x+y, list(map(lambda x: x+1, low_points)))}")
main()