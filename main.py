vowels = ['a', 'e', 'i', 'o', 'u'] #vowels ang. samogłoski
found = []
words = []

word = 'none'
index = 0

while word != "stop":
    print('Wprowadź słowo: ')
    word = input()
    if word != "stop":
        words.append(word)
        for letter in word:
            if letter in vowels:
                if letter in found:
                    print("Litera --- " + letter + " --- jest już w naszym zbiorze, więc ją pomijam")
                else:
                    found.append(letter)
        index += 1

print('Wykonano ' + str(index) + ' sprawdzeń, a słowa, to:')
print('Wypisz sprawdzane słowa:')
for word in words:
    print(word)