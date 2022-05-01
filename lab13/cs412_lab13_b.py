def main():
    lines = int(input())
    connections = {}
    for line in range(lines):
        line = input().split()
        connections[line[0]] = line[1:]
    #print(connections)
    query = input().split()
    independent = True

    for node in query:
        for check in query:
            if check in connections[node]:
                independent = False
    print(independent)     

if __name__ == "__main__":
    main()