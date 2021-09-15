vowels = ['a', 'e', 'i', 'o', 'u'] #vowels ang. samogłoski
found = []
word = "Miliard"



for letter in word:
    if letter in vowels:
        if letter in found:
            print("Litera --- " + letter + " --- jest już w naszym zbiorze, więc ją pomijam")
        else:
            found.append(letter)
print(found)
