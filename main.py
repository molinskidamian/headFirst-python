# Use list and methods

names = [] # create empty list
diffrentNames = ['Kate', 'Damian']

names.append('John')
names.append(diffrentNames)
names.append('Stanley')


print(names)

print('Użycie metody names.pop()')
last = names.pop()

print(names)

print('Ostatnia wartość tablicy, to: ' + last)





print('==============.extend()===============')
names.extend(['David', 'Gabrysia'])

print(names)