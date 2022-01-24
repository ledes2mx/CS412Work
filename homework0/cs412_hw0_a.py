"""
    name: Miguel Ledesma

"""
# All modules for CS412 must include a main method that allows it
# to imported and invoked from other python scripts
# LIST STRUCTURES ONLY

def main():
    animal_list = []
    sound_list = []
    heard_list = []
    sayings = input().split(" ")
    #print(sayings)
    n = int(input())
    lines = [input().split(" ") for _ in range(n)]
    for line in lines:
        animal_list.append(line[0])
        sound_list.append(line[2])
        #print(line[0] + " goes " + line[2])
    #print(anim_list)
    #print(sound_list)
    fox_says = sayings
    #print (fox_says)

    for sound in sayings:
        # if sound in sound_list and :
        if sound_list.count(sound) > 0 and heard_list.count(animal_list[sound_list.index(sound)]) == False:
            heard_list.append(animal_list[sound_list.index(sound)])
    #print(heard_list)

    for animal in heard_list:
        if fox_says.count(sound_list[animal_list.index(animal)]) > 0:
            for i in range(fox_says.count(sound_list[animal_list.index(animal)])):
                fox_says.remove(sound_list[animal_list.index(animal)])

    #print(fox_says)

    """
    THIS DOESN"T LIST ALSO HEARD IN THE RIGHT ORDER
    fox_words = sayings
    for sound in sound_list:
        if fox_words.count(sound) > 0:
            #print(fox_words.count(sound))
            for i in range(fox_words.count(sound)):
                fox_words.remove(sound)
                if heard_list.count(animal_list[sound_list.index(sound)]) == 0:
                    heard_list.append(animal_list[sound_list.index(sound)])
                
                    for heard in fox_words:
                        fox_words.remove(sound)
    """
    print("what the fox says: " + ' '.join(fox_says) + " ") 
    print("also heard:" + ' '.join(heard_list) + " ")

if __name__ == "__main__":
    main()