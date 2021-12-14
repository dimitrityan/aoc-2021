#!/usr/bin/env python3

def main():
    with open("day10/input.txt", "r") as input:
        lines = input.read().splitlines()
        wrong_elems = []
        scores = []
        for line in lines:
            stack = []
            is_corrupt = False
            for sym in line:
                if sym in ["{", "[", "(", "<"]:
                    stack.append(sym)
                elif sym in ["}", "]", ")", ">"]:
                    prev_sym = stack.pop()
                    if (prev_sym == "{" and not sym == "}") or (prev_sym == "(" and not sym == ")") or (prev_sym == "<" and not sym == ">") or (prev_sym == "[" and not sym == "]"):
                        # Not sym.
                        wrong_elems.append(sym)
                        is_corrupt = True
                        break
            if is_corrupt:
                continue
            # Incomplete sequences:
            score = 0
            for x in reversed(stack):
                score *= 5
                if x == "(":
                    score += 1
                elif x == "[":
                    score += 2
                elif x == "{":
                    score += 3
                elif x == "<":
                    score += 4
            scores.append(score)
            print(stack)
        print(scores)
        print(f"Score: {sorted(scores)[int(len(scores)/2)]}")

main()