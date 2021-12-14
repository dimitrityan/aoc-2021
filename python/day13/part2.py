#!/usr/bin/env python3

def main():
    with open("day13/input.txt", "r") as input:
        lines = input.read().splitlines()
        fold_instructions = []
        dots = set()
        for line in lines:
            if "fold along" in line:
                fold_info = line.split("fold along ")[1]
                axis = fold_info.split("=")[0]
                val = int(fold_info.split("=")[1])
                fold_instructions.append((axis, val))
            elif "," in line:
                dot_coord = (int(line.split(",")[1]), int(line.split(",")[0]))
                dots.add(dot_coord)


        for fold_instruction in fold_instructions:
            axis = fold_instruction[1]
            to_remove = []
            to_add = []
            for dot_coord in dots:
                if fold_instruction[0] == "x":
                    if dot_coord[1] > axis:
                        to_add.append((dot_coord[0], 2*axis - dot_coord[1]))
                        to_remove.append((dot_coord[0], dot_coord[1]))
                elif fold_instruction[0] == "y":
                    if dot_coord[0] > axis:
                        to_add.append((2*axis - dot_coord[0], dot_coord[1]))
                        to_remove.append((dot_coord[0], dot_coord[1]))
            for rem in to_remove:
                dots.remove(rem)
            for add in to_add:
                dots.add(add)
        
        print(len(dots))
        s = ""
        for i in range(0, 50):
            for c in range(0,50):
                if (i,c) in dots:
                    s+="#"
                else:
                    s+="."
            s+="\n"                
        print(s)
main()