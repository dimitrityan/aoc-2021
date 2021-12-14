with open("input.txt", "r") as input:
    lines = input.readlines()

    prev_sum = None
    counter = 0

    for i in range(0, len(lines)):
        if i + 3 > len(lines):
            break
        current_sum = int(int(lines[i])) + int(lines[i + 1]) + int(lines[i + 2])
        if i == 0:
            prev_sum = current_sum
            continue
        if current_sum > prev_sum:
            counter += 1
        prev_sum = current_sum
        
    print (counter)