from collections import deque


def main():
    numInputs = int(input())
    routes = {}
    for i in range(numInputs):
        leave, to = input().split(" ")
        #print(leave, to)
        if leave not in routes:
            routes[leave] = {to}
        else:
            routes[leave].add(to)
        if to not in routes:
            routes[to] = {leave}
        else:
            routes[to].add(leave)
    init, finish = input().split(" ")
    #print(routes)

    visited = set()

    def findRoutes():
        stack = deque([(0,init)])
        path = deque([])
        while len(stack) != 0:
            #print(stack)
            past, current = stack[-1]
            stack.pop()
            if current not in visited:
                path.append(current)
                if path[-1] == finish:
                    break
                visited.add(current)
                for nextStop in routes[current]:
                    stack.append((current,nextStop))
        #print("PATH", path)
        return path
        


    route = findRoutes()
    if finish not in route:
        print("no route possible")
    else:
        for path in route:
            if path != route[-1]:
                print(path, end=" ")
            else:
                print(path)
    
if __name__ == "__main__":
    main()