def main():
    n= int(input())
    nodes = {}
    for i in range(n):
        touching = input().split()
        node = touching[0]
        if node not in nodes:
            nodes[node] = set()
        for i in range(1, len(touching)):
            nodes[node].add(touching[i])
    marked = set()
    dfsOrder = input().split()

    def dfsALL(dfsOrder):
        node_parents = {}
        prePost = {}
        clock = 0

        def preVisit(vertex):
            nonlocal clock
            clock += 1
            prePost[vertex][0] = clock
        
        def postVisit(vertex):
            nonlocal clock
            clock += 1
            prePost[vertex][1] = clock

        for node in nodes:
            node_parents[node] = ()
            prePost[node] = [0,0]

        def dfs(vertex):
            marked.add(vertex)
            preVisit(vertex)
            for edge in nodes[vertex]:
                if edge not in marked:
                    node_parents[edge] = vertex
                    dfs(edge)
            postVisit(vertex)

        for node in marked:
            marked.remove(node)
        for node in dfsOrder:
            if node not in marked:
                dfs(node)

        return node_parents, prePost 

    node_parents, prePost = dfsALL(dfsOrder)

    print("NODE PARENTS", node_parents)
    print("PRE AND POST", prePost)

    m = int(input())

    for i in range(m):
        current, to = input().split()
        print(current, to)

if __name__ == "__main__":
    main()