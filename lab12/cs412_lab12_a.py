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
        # IT GOES AUGMENTED, CAPACITY (CAPACITY SHOULD NEVER CHANGE)
        capacities[(start, end)] = [0, capacity]
        
    #print(connections)
    #print(capacities)

    nodes = list(connections.keys())
    #print(nodes)

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
                        #print(current, node)
            search.append((past,current))
        #print(reachable)
        #print(search)
        #print(visited)

        path = []
        smallVolume = sys.maxsize
        if reachable:
            front, back = search[-1]
            #path.append(back)
            while front != 0:
                for i in reversed(range(len(search))):
                    if search[i][1] == front:
                        if smallVolume > capacities[(front, back)][1]-capacities[(front, back)][0]:
                            smallVolume = capacities[(front, back)][1]-capacities[(front, back)][0]
                        path.append((front,back))
                        #print(front, back)
                        #capacities[(front, back)][0]
                        back = front
                        front = search[i][0]
            #print(smallVolume)
            #print(path)
            for item in path:
                capacities[item][0] = smallVolume
        #print(capacities)
        return reachable, nodesReached
    reachable = True
    while reachable:
        reachable, reached = bfs()
    #print(reached)
    flow = 0
    cuts = []
    for reach in reached:
        for node in connections[reach]:
            #print(capacities[(reach, node)])
            if node not in reached:
                cuts.append((reach, node))
                num = capacities[(reach, node)][0]
                flow += num
    print(flow)
    for cut in cuts:
        print(cut[0], cut[1])

if __name__ == "__main__":
    main()