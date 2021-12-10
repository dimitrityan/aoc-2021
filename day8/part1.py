#!/usr/bin/env python3

def main():
    with open("input.txt", "r") as input:
        lines = input.read().splitlines()
        counter = 0
        for line in lines:    
            for sig in line.split("|")[1][1:].split(" "):
                if len(sig) in [2, 3, 4, 7]:
                    counter += 1
        print(counter)
main()
                