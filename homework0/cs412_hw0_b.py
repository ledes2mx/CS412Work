"""
    name: Miguel Ledesma

    In an effort to make this faster, I made it slower, but at least I know where it's slowest
    it is slower by 4 seconds

"""
# All modules for CS412 must include a main method that allows it
# to imported and invoked from other python scripts# DICTIONARIES ALLOWED
@profile
def main():
    animal_sound = {}
    heard = {}
    fox_says = []
    also_heard = []
    sounds = input().split(" ")
    n = int(input())
    lines = [input().split(" ") for _ in range(n)]
    for line in lines:
        animal_sound[line[2]] = line[0]
    for sound in sounds:
        #if sound in animal_sound and sound not in heard:
        if sound not in heard:
            #heard[sound] = animal_sound[sound]
            #also_heard.append(heard[sound])
            heard[sound] = animal_sound.get(sound, "???")
            also_heard.append(heard[sound])
        if sound not in animal_sound:
            fox_says.append(sound)

    print("what the fox says: " + ' '.join(fox_says) + " ")
    if also_heard:
        print("also heard: " + ' '.join(also_heard) + " ")
    else:
        print("also heard: ")


if __name__ == "__main__":
    main()