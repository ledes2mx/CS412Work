# MAKE CHILDREN THE PARENTS TO MAKE TOPOLOGICAL SORT

def main():
    n = int(input())
    nodes = {}
    for i in range(n):
        touching = input().split()
        node = touching[0]
        if node not in nodes:
            nodes[node] = set()
        for i in range(1, len(touching)):
            nodes[node].add(touching[i])
    reverse = {}
    for node in nodes:
        for touching in nodes[node]:
            if touching not in reverse:
                reverse[touching] = set()
            reverse[touching].add(node)
    for node in nodes:
        if node not in reverse:
            reverse[node] = set()
    #print(nodes)
    #print(reverse)

    node_parents = {}
    for node in reverse:
        node_parents[node] = ()
    prePost = {}
    for node in reverse:
        prePost[node] = [0,0]
    marked = set()
    clock = 0
    ordering = [None] * n

    def DFSAll():
        for node in marked:
            marked.remove(node)
        for node in reverse:
            if node not in marked:
                DFS(node)

    def DFS(vertex):
        marked.add(vertex)
        preVisit(vertex)
        for edge in reverse[vertex]:
            if edge not in marked:
                node_parents[edge] = vertex
                DFS(edge)
        postVisit(vertex)
        for i in range(len(ordering)):
            if ordering[i] == None:
                ordering[i] = vertex
                break


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
    for node in reverse:
        for edge in reverse[node]:
            if prePost[edge][pre] < prePost[node][pre] < prePost[node][post] < prePost[edge][post]:
                acyclic = False
    
    for i in range(len(ordering)):
        if i >= len(ordering)-1:
            print(ordering[i])
        else:
            print(ordering[i], end=" ")
    #print(prePost)
    #print(acyclic)
    """
    reverse = {}
    for child in node_parents:
        print(child)
        for parent in node_parents:
            if node_parents[child] == parent:
                if parent not in reverse:
                    reverse[parent] = set()
                reverse[parent].add(child)
    for node in node_parents:
        if node not in reverse:
            reverse[node] = set()
    print(node_parents)
    print(reverse)

    
    for node in reverse:
    """


if __name__ == "__main__":
    main()