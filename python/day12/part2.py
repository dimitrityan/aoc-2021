#!/usr/bin/env python3

def main():
    with open("day12/input.txt", "r") as input:
        lines = input.read().splitlines()
        small_caves = set()
        graph = {}
        for line in lines:
            left = line.split("-")[0]
            right = line.split("-")[1]
            if left.islower():
                small_caves.add(left)
            if right.islower():
                small_caves.add(right)
            if left in graph:
                graph[left].append(right)
            else:
                graph[left] = [right]
            if right in graph:
                graph[right].append(left)
            else:
                graph[right] = [left]
        
        queue = [(["start"], False)]
        paths = []
        while len(queue) > 0:
            q_elem = queue.pop(0)
            path = q_elem[0]
            last_node = path[-1]
            if last_node == "end":
                paths.append(path)
                continue
            adj_nodes = graph[last_node]
            for adj in adj_nodes:
                if adj == "start" or (adj in small_caves and path.count(adj) == 2 and q_elem[1]):
                    continue
                if adj in small_caves and path.count(adj) == 1 and q_elem[1]:
                    continue
                p = path.copy()
                p.append(adj)
                if adj in small_caves and p.count(adj) == 2 or q_elem[1]:
                    queue.append((p, True))
                else:
                    queue.append((p, False))
        
        print(len(paths))

main()
        