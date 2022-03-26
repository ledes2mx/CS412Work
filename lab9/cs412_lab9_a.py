from collections import deque

def main():
    numNodes = int(input())
    nodes = {}
    for i in range(numNodes):
        touching = input().split()
        node = touching[0]
        if node not in nodes:
                nodes[node] = set()
        for i in range(1, len(touching)):
            nodes[node].add(touching[i])
        #print(nodes)
    node_parents = {}
    for node in nodes:
        node_parents[node] = ()
    prePost = {}
    for node in nodes:
        prePost[node] = [0,0]
    #prePost['0'][0] = 1
    #print("THIS IS THE CHANGED VALUE",prePost['0'][0])
    #print(prePost)
    #print(node_parents)
    marked = set()
    clock = 0
    def DFSAll():
        #preProcess()
        for node in marked:
            marked.remove(node)
        for node in nodes:
            if node not in marked:
                DFS(node)

        #print(node_parents)
    def DFS(vertex):
        marked.add(vertex)
        preVisit(vertex)
        # for each edge vw
        for edge in nodes[vertex]:

            # if w is unmarked
            if edge not in marked:
                # parent(w) = v
                node_parents[edge] = vertex
                # DFS(w)
                DFS(edge)
        postVisit(vertex)

    def preVisit(vertex):
        nonlocal clock 
        clock += 1
        # add the pre to the incoming node
        prePost[vertex][0] = clock
    
    def postVisit(vertex):
        nonlocal clock
        clock += 1
        # add the post to the incoming node
        prePost[vertex][1] = clock
    
    DFSAll()

    acyclic = True
    # U(VERTEX) -> V(EDGE) 
    pre = 0
    post = 1
    for node in nodes:
        #print("NODE", node)
        for edge in nodes[node]:
            #print("EDGE",edge)
            if prePost[edge][pre] < prePost[node][pre] < prePost[node][post] < prePost[edge][post]:
                acyclic = False
    print(acyclic)
        


if __name__ == "__main__":
    main()