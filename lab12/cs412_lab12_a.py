# USE A QUEUE TO FIND EDGES IN WHATEVER FIRST SEARCH
# VERTS THAT ARE REACHABLE ARE INCLUDED IN THE LIST
# EDGES WHERE NO FLOW CAN GO THROUGH ARE CUT
from collections import deque
import sys

def main():
    verts, edges = input().split()
    verts, edges = int(verts), int(edges)
    connections = {}
    capacities = {}
    for i in range(verts):
        connections[i] = set()
    for i in range(edges):
        start, end, capacity = input().split()
        start, end, capacity = int(start), int(end), int(capacity)
        connections[start].add(end)
        capacities[(start, end)] = [0, capacity]
    nodes = list(connections.keys())

    def bfs():
        visited = set()
        visiting = set()
        queue = deque()
        queue.append((0,0))
        search = []
        reachable = False
        nodesReached = set()
        while queue:
            past, current = queue[0]
            visited.add(current)
            if current == nodes[-1]:
                reachable = True
                search.append((past, current))
                break
            queue.popleft()
            for node in connections[current]:
                if capacities[(current, node)][0] < capacities[(current, node)][1]:
                    if node not in visited and node not in visiting:
                        queue.append((current, node))
                        visiting.add(node)
                        nodesReached.add(node)
            search.append((past,current))

        path = []
        smallVolume = sys.maxsize
        if reachable:
            front, back = search[-1]
            while front != nodes[0]:
                for i in reversed(range(len(search))):
                    if search[i][1] == front:
                        if smallVolume > capacities[(front, back)][1]-capacities[(front, back)][0]:
                            smallVolume = capacities[(front, back)][1]-capacities[(front, back)][0]
                        path.append((front,back))
                        back = front
                        front = search[i][0]
            for item in path:
                capacities[item][0] = smallVolume
        return reachable, nodesReached
    reachable, reached = bfs()
    while reachable:
        reachable, reached = bfs()
    flow = 0
    cuts = []
    for reach in reached:
        for node in connections[reach]:
            if node not in reached:
                cuts.append((reach, node))
                num = capacities[(reach, node)][0]
                flow += num
    print(flow)
    for cut in cuts:
        print(cut[0], cut[1])

if __name__ == "__main__":
    main()