#!/usr/bin/env python3

def main():
    with open("day10/input.txt", "r") as input:
        lines = input.read().splitlines()
        wrong_elems = []
        for line in lines:
            stack = []
            for sym in line:
                if sym in ["{", "[", "(", "<"]:
                    stack.append(sym)
                elif sym in ["}", "]", ")", ">"]:
                    prev_sym = stack.pop()
                    if (prev_sym == "{" and not sym == "}") or (prev_sym == "(" and not sym == ")") or (prev_sym == "<" and not sym == ">") or (prev_sym == "[" and not sym == "]"):
                        # Not sym.
                        wrong_elems.append(sym)
                        break
        sum = 0
        for x in wrong_elems:
            if x == ")":
                sum += 3
            elif x == "]":
                sum += 57
            elif x == "}":
                sum += 1197
            elif x == ">":
                sum += 25137
        print(wrong_elems)
        print(f"Score: {sum}")

main()