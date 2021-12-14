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
        
        queue = [["start"]]
        paths = []
        while len(queue) > 0:
            path = queue.pop(0)
            last_node = path[-1]
            if last_node == "end":
                paths.append(path)
                continue
            adj_nodes = graph[last_node]
            for adj in adj_nodes:
                if adj in small_caves and adj in path:
                    continue
                p = path.copy()
                p.append(adj)
                queue.append(p)
        
        print(paths)
        print(len(paths))
main()
        