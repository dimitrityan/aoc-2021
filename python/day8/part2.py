#!/usr/bin/env python3

def add_to_map(my_map, signal):
    if len(signal) not in my_map:
        if len(signal) in [2,3,4,7]:
            my_map[len(signal)] = signal
        elif len(signal):
            my_map[len(signal)] = [signal]
    else:
        my_map[len(signal)].append(signal)

def main():
    with open("input.txt", "r") as input:
        lines = input.read().splitlines()

        segments_9 = ""
        segments_0 = ""
        segments_6 = ""
        segments_3 = ""
        segments_5 = ""
        segments_2 = ""

        total_res = 0
        for line in lines:
            my_map = {}
            for sig in line.split("|")[0][:-1].split(" "):
                sig = "".join(sorted(sig))
                add_to_map(my_map, sig)
            
            found_segments_6 = False
            # First step: find 9 by checking in segments with length 6 if 1 is in that signal
            for sig_6 in my_map[6]:
                signal_4 = set(my_map[4])
                if signal_4.issubset(set(sig_6)):
                    segments_9 = sig_6
                    my_map[6].remove(sig_6)
                    break

            for sig_6 in my_map[6]:
                signal_1 = set(my_map[2])
                if signal_1.issubset(set(sig_6)):
                    segments_0 = sig_6
                    my_map[6].remove(sig_6)
                    break
            segments_6 = my_map[6][0]

            for sig_5 in my_map[5]:
                signal_1 = set(my_map[2])
                if signal_1.issubset(set(sig_5)):
                    segments_3 = sig_5
                    my_map[5].remove(sig_5)
                    break
                
            for sig_5 in my_map[5]:
                a = set(sig_5).union(set(my_map[2]))
                if a.issubset(segments_9):
                    segments_5 = sig_5
                    my_map[5].remove(sig_5)
            segments_2 = my_map[5][0]

            decoded_list = {
                segments_0: 0,
                segments_2: 2,
                segments_3: 3,
                segments_5: 5,
                segments_6: 6,
                segments_9: 9,
                my_map[2]: 1,
                my_map[3]: 7,
                my_map[4]: 4,
                my_map[7]: 8
            }
            output = line.split("|")[1][1:].split(" ")
            res = ""
            for out_sig in output:
                out_sig = "".join(sorted(out_sig))
                if out_sig in decoded_list:
                   res += str(decoded_list[out_sig])
            
            total_res += int(res)

        print(total_res)
main()