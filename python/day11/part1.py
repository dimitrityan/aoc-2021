#!/usr/bin/env python3

SIMULATION_STEPS = 100

def main():
    with open("day11/input.txt", "r") as input:
        lines = input.read().splitlines()
        matrix = [[0 for x in range(0, len(lines))] for x in range(0, len(lines[0]))]
        for row in range(0, len(lines)):
            for col in range(0, len(lines[0])):
                matrix[row][col] = int(lines[row][col])

        num_flashes = 0
        for _ in range(0, SIMULATION_STEPS):
            flashed = set()
            queue = []
            for row in range(0, len(matrix)):
                for col in range(0, len(matrix[0])):
                    matrix[row][col] += 1
                    if matrix[row][col] > 9:
                        queue.append((row, col))
                        flashed.add((row,col))

            while len(queue) > 0:
                elem = queue.pop(0)
                r, c = elem[0], elem[1]
                # matrix[r][c] = 0

                if r-1 >= 0:
                    # r-1 c
                    matrix[r-1][c] += 1
                    if matrix[r-1][c] > 9 and (r-1, c) not in queue and (r-1, c) not in flashed:
                        flashed.add((r-1, c))
                        queue.append((r-1, c))
                    # r-1 c-1
                    if c-1 >= 0:
                        matrix[r-1][c-1] += 1
                        if matrix[r-1][c-1] > 9 and (r-1,c-1) not in queue and (r-1,c-1) not in flashed:
                            flashed.add((r-1, c-1))
                            queue.append((r-1, c-1))
                # r-1 c+1
                if r-1 >= 0 and c+1 < len(matrix[0]):
                    matrix[r-1][c+1] += 1
                    if matrix[r-1][c+1] > 9 and (r-1,c+1) not in queue and (r-1,c+1) not in flashed:
                        flashed.add((r-1, c+1))
                        queue.append((r-1, c+1))
                
                # r c-1
                if c-1 >= 0:
                    matrix[r][c-1] += 1
                    if matrix[r][c-1] > 9 and (r, c-1) not in queue and (r, c-1) not in flashed:
                        flashed.add((r, c-1))
                        queue.append((r, c-1))
                
                # r c+1
                if c+1 < len(matrix[0]):
                    matrix[r][c+1] += 1
                    if matrix[r][c+1] > 9 and (r, c+1) not in queue and (r, c+1) not in flashed:
                        flashed.add((r, c+1))
                        queue.append((r, c+1))

                # r+1
                if r+1 < len(matrix):
                    # r+1 c
                    matrix[r+1][c] += 1
                    if matrix[r+1][c] > 9 and (r+1, c) not in queue and (r+1, c) not in flashed:
                        flashed.add((r+1, c))
                        queue.append((r+1, c))
                    # r+1 c-1
                    if  c-1 >= 0:
                        matrix[r+1][c-1] += 1
                        if matrix[r+1][c-1] > 9 and (r+1,c-1) not in queue and (r+1,c-1) not in flashed:
                            flashed.add((r+1, c-1))
                            queue.append((r+1, c-1))
                    # r+1 c+1
                    if c+1 < len(matrix[0]):
                        matrix[r+1][c+1] += 1
                        if matrix[r+1][c+1] > 9 and (r+1,c+1) not in queue and (r+1,c+1) not in flashed:
                            flashed.add((r+1, c+1))
                            queue.append((r+1, c+1))
            num_flashes += len(flashed)
            for f in flashed:
                matrix[f[0]][f[1]] = 0
        print(num_flashes)
main()
