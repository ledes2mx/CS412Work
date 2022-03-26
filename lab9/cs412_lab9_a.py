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
    node_parents = {}
    for node in nodes:
        node_parents[node] = ()
    prePost = {}
    for node in nodes:
        prePost[node] = [0,0]
    marked = set()
    clock = 0

    def DFSAll():
        for node in marked:
            marked.remove(node)
        for node in nodes:
            if node not in marked:
                DFS(node)

    def DFS(vertex):
        marked.add(vertex)
        preVisit(vertex)
        for edge in nodes[vertex]:
            if edge not in marked:
                node_parents[edge] = vertex
                DFS(edge)
        postVisit(vertex)

    def preVisit(vertex):
        nonlocal clock 
        clock += 1
        prePost[vertex][0] = clock
    
    def postVisit(vertex):
        nonlocal clock
        clock += 1
        prePost[vertex][1] = clock
    
    DFSAll()

    acyclic = True
    pre = 0
    post = 1
    for node in nodes:
        for edge in nodes[node]:
            if prePost[edge][pre] < prePost[node][pre] < prePost[node][post] < prePost[edge][post]:
                acyclic = False
    print(acyclic)
        


if __name__ == "__main__":
    main()