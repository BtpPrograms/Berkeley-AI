listOfStrings = ['Alec', 'Benny', 'Ashley', 'Spotts', 'Cheesecake']

newList = [string.lower() for string in listOfStrings if len(string) > 5]
newList += [string for string in listOfStrings if len(string) <= 5]

print newList
