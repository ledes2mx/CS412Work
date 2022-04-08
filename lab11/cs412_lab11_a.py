from queue import PriorityQueue
import sys

def main():
    nodes, connects, queries = input().split()
    nodes, connects, queries = int(nodes), int(connects), int(queries)
    connections = {}
    weights = {}

    for i in range(nodes):
        connections[i] = set()

    for i in range(connects):
        source, dest, weight = input().split()
        source, dest, weight = int(source), int(dest), int(weight)
        connections[source].add(dest)
        weights[(source, dest)] = weight
    #print(connections)
    #print(weights)

    def dijkstra(query):
        start, end = query
        current_node = start
        sssp = {}
        def init_SSSP():
            for i in range(len(connections)):
                if i == start: sssp[i] = [0, None]
                else: sssp[i] = [sys.maxsize, None]
        init_SSSP()
        #print(sssp)
        marked = set()
        pq = PriorityQueue()
        pq.put(start, 0)
            #print(weights[(source,node)])
        
        while pq:
            #print("CURRENT", current_node, "END", end)
            if current_node == end: return sssp[current_node][0]
            if len(connections[current_node]) == 0: 
                #print("HERE")
                return -1
            #print("THERE")
            marked.add(current_node)
            for node in connections[current_node]:
                #print(node)
                if node in marked:
                    continue
                #print("CURRENT, NEXT", current_node, nextNode)
                #print("WEIGHT", weights[(current_node,nextNode)])
                cost = sssp[current_node][0] + weights[(current_node,node)]
                #print("COST", cost)
                if sssp[node][0] > cost:
                    sssp[node] = [cost, current_node]
                    pq.put(node, cost)
                    current_node = node
        

            #print("PQ", pq)

    for i in range(queries):
        source, dest = input().split()
        source, dest = int(source), int(dest)
        query = (source, dest)
        cost = dijkstra(query)
        if cost == -1:
            print("Impossible")
        else:
            print(cost)

if __name__ == "__main__":
    main()