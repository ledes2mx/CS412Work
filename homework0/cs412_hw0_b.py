"""
    name: Miguel Ledesma

"""
# All modules for CS412 must include a main method that allows it
# to imported and invoked from other python scripts# DICTIONARIES ALLOWED

def main():
    animal_sound = {}
    heard = {}
    sounds = input().split(" ")
    n = int(input())
    lines = [input().split(" ") for _ in range(n)]
    for line in lines:
        animal_sound[line[2]] = line[0]
    for sound in sounds:
        if sound in animal_sound and sound not in heard:
            heard[animal_sound[sound]] = 1
    print(heard)

if __name__ == "__main__":
    main()