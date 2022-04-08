from connected_components import count_and_label
#TUPLE OF BEGINNING EDGE AND END EDGE AS KEY, VALUE IS WEIGHT
def main():
    lines = int(input())
    coord_list = {}
    connections = {}
    distances = {}
    for i in range(lines):
        x, y = input().split()
        x, y = float(x), float(y)
        coord_list[i] = (x, y)
    #print(coord_list[0])
    
    for i in range(len(coord_list)):
        for j in range(len(coord_list)):
            if i!=j:
                #print("CHECKED", coord_list[i], coord_list[j])
                if coord_list[i] not in connections:
                    connections[coord_list[i]] = set()
                    #print("NOT THERE YET", connections)
                connections[coord_list[i]].add(coord_list[j])
                #print("IN THERE", connections)
                x1, y1 = coord_list[i]
                x2, y2 = coord_list[j]
                distance = round(((((x2-x1)**2) + ((y2-y1)**2)) ** 0.5), 1)
                #print(coord_list[i], coord_list[j], distance)
                distances[(coord_list[i], coord_list[j])] = distance


    print(connections[coord_list[0]])

    count, labels = count_and_label(list(connections))
    print("COUNT", count)
    print("LABEL", labels)


if __name__ == "__main__":
    main()