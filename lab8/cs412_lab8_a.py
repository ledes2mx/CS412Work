def main():
    numInputs = int(input())
    routes = {}
    for i in range(numInputs):
        leave, to = input().split(" ")
        print(leave, to)

if __name__ == "__main__":
    main()