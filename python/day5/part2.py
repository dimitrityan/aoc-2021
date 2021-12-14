#!/usr/bin/env python3

def main():
    with open("input.txt", "r") as input:
        lines = input.read().splitlines()
        matrix = [[0 for i in range(1000)] for i in range(1000)]
        for line in lines:
            left = line.split("->")[0].strip()
            right = line.split("->")[1].strip()
            x0 = int(left.split(",")[0])
            y0 = int(left.split(",")[1])
            x1 = int(right.split(",")[0])
            y1 = int(right.split(",")[1])

            dist_x = x0 - x1
            dist_y = y0 - y1

            if dist_x == 0:
                start_y = 0
                if dist_y < 0:
                    dist_y = dist_y * -1 + 1
                    start_y = y0
                else:
                    dist_y += 1
                    start_y = y1
                for i in range(0, dist_y):
                    matrix[start_y + i][x0] += 1
            elif dist_y == 0:
                start_x = 0
                if dist_x < 0:
                    dist_x = dist_x * -1 + 1
                    start_x = x0
                else:
                    dist_x += 1
                    start_x = x1
                for i in range(0, dist_x):
                    matrix[y0][start_x + i] += 1
            else:
                # Diagonal line
                start_x = x0
                start_y = y0
                if x1 > x0:
                    dist_x = x1 - x0 + 1
                else:
                    dist_x = x0 - x1 + 1
                if y0 > y1:
                    dist_y = y0 - y1 + 1
                else:
                    dist_y = y1 - y0 + 1
                for i in range(0, dist_x):
                    c = i
                    r = i
                    if x0 > x1:
                        c *= -1
                    if y0 > y1:
                        r *= -1
                    matrix[start_y + r][start_x + c] += 1
        counter = 0
        for r in range(0, len(matrix)):
            for c in range(0, len(matrix[0])):
                if matrix[r][c] >= 2:
                    counter += 1
        print(counter)
main()