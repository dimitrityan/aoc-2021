#!/usr/bin/env python3
import functools

def get_low_points(lines):
    low_points = []
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
            low_points.append(((r, c), cur_depth))
    return low_points

def main():
    with open("day9/input.txt", "r") as input:
        lines = input.read().splitlines()
        low_points = get_low_points(lines)
        basin_sizes = []
        visited = [[False for c in range(len(lines[0]))] for r in range(len(lines))]
        for low_point in low_points:
            queue = []
            queue.append(((low_point[0][0], low_point[0][1]), low_point[1]))
            counter = 0
            while len(queue) > 0:
                left, right, up, down = None, None, None, None
                p = queue.pop(0)
                r = p[0][0]
                c = p[0][1]
                val = p[1]
                if visited[r][c]:
                    continue
                counter += 1
                visited[r][c] = True
                if c-1 >= 0:
                    left = int(lines[r][c-1])
                if c+1 < len(lines[r]):
                    right = int(lines[r][c+1])
                if r-1 >= 0:
                    up = int(lines[r-1][c])
                if r+1 < len(lines):
                    down = int(lines[r+1][c])
                if left != None and left > val and left != 9 and ((r,c-1), left) not in queue:
                    queue.append(((r,c-1), left))
                if right != None and right > val and right != 9 and ((r,c+1), right) not in queue:
                    queue.append(((r,c+1), right))
                if up != None and up > val and up != 9 and ((r-1,c), up) not in queue:
                    queue.append(((r-1,c), up))
                if down != None and down > val and down != 9 and ((r+1,c), down) not in queue:
                    queue.append(((r+1,c), down))
            basin_sizes.append(counter)
        print(functools.reduce(lambda x, y: x*y, sorted(basin_sizes)[-3:]))
main()