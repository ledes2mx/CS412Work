from collections import deque

def main():
    lines = int(input())
    scan = [[None]] * lines
    visited = set()
    for i in range(lines):
        scan[i] = input().split(" ")
        for j in range(lines):
            scan[i][j] = int(scan[i][j])

    largest = 0

    def findSize(i,j):
        size = 0
        stack = deque([(0,(i,j))])

        while len(stack) != 0:
            past, current = stack[-1]
            #print(current[0], current[1])
            x,y = current[0], current[1]
            posX, posY = current[0]+1, current[1]+1
            negX, negY = current[0]-1, current[1]-1
            stack.pop()
            #print(stack)
            if current not in visited:
                visited.add(current)
                size += 1
                if negX >= 0:
                    if scan[negX][y] == 1:
                        stack.append((current, (negX, y)))
                if negY >= 0:
                    if scan[x][negY] == 1:
                        stack.append((current, (x, negY)))
                if posY < lines:
                    if scan[x][posY] == 1:
                        stack.append((current, (x, posY)))
                if posX < lines:
                    if scan[posX][y] == 1:
                        stack.append((current, (posX, y)))
        return size

    for i in range(lines):
        for j in range(lines):
            if scan[i][j] == 1 and (i,j) not in visited:
                size = findSize(i,j)
                if size > largest:
                    largest = size

    print(largest)


if __name__ == "__main__":    
    main()