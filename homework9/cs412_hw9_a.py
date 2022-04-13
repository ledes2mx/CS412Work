# (Original Currency) / Ending Amount (New Currency) = Exchange Rate
from curses import nonl
import sys
from queue import PriorityQueue
import math

def main():
    lines = int(input())
    connections = {}
    exchanges = {}
    negations = {}
    for i in range(lines):
        curr1, curr2, rate = input().split()
        if curr1 not in connections:
            connections[curr1] = set()
        connections[curr1].add(curr2)
        if curr2 not in connections:
            connections[curr2] = set()
        rate = float(rate)
        exchanges[(curr1, curr2)] = rate
    #print(connections)
    #print(exchanges)

    for key in list(exchanges.keys()):
        negations[key] = math.log(exchanges[key])
    #print(negations)

    def BellmanFord(start):
        sssp = {}
        def init_SSSP():
            for i in list(connections.keys()):
                if i == start: sssp[i] = [0, None]
                else: sssp[i] = [sys.maxsize, None]
        init_SSSP()
        #print(sssp)

        verts = list(connections.keys())
        edges = list(negations.keys())
        for i in range(len(verts)):
            for edge in edges:
                #print(edge)
                #print(edge[0], edge[1])
                u, v = edge[0], edge[1]
                #print(sssp[u][0], negations[edge], sssp[v][0])
                relax = sssp[u][0] + negations[edge]
                #print(edge, relax)
                if v == start:
                    sssp[v] = [relax, u]
                if relax < sssp[v][0]:
                    sssp[v] = [relax, u]
        #print(sssp)

        marked = set()
        negative = False
        past = start
        def findArbitrage(node):
            path = []
            nonlocal negative
            nonlocal past
            if node == start and node in marked:
                if sssp[node][0] < 0 and sssp[node][1] == past:
                    negative = True
                return [node]
            marked.add(node)
            for connect in connections[node]:
                if sssp[connect][1] == node:
                    if sssp[connect][0] < 0:
                        negative = True
                    past = node
                    path = [node] + findArbitrage(connect)
            if len(connections[node]) == 0:
                negative = False
            return path
        path = findArbitrage(start)

        adjust = 1
        if negative == True and path[0] == path[-1] and len(path) > 1:
            print("Arbitrage Detected")
            for i in range(len(path)):
                if i == len(path)-1:
                    print(path[i])
                else:
                    print(path[i], "=>", end=" ")
            for i in range(len(path)):
                if i == len(path)-2:
                    adjust = adjust * exchanges[path[i], path[i+1]]
                    break
                else:
                    #print(exchanges[path[i], path[i+1]])
                    adjust = adjust * exchanges[path[i], path[i+1]]
            adjust = round(adjust, 5)
            formatedAdjust = "{:.5f}".format(adjust)
            print(formatedAdjust)
        else:
            print("No Arbitrage Detected")

    start = list(connections.keys())[0]
    BellmanFord(start)





if __name__ == "__main__":
    main()