def getMode(theList) :
    countDictionary = {}
    # create countDictionary
    for num in theList :
        if(num in countDictionary.keys()) :
            countDictionary[num] += 1
        else :
            countDictionary[num] = 1
    # create list of mode/s
    maxFrequency = 1
    modes = []
    for key in countDictionary.keys() :
        if (countDictionary[key] > maxFrequency) :
            modes = [key]
            maxFrequency = countDictionary[key]
        elif (countDictionary[key] == maxFrequency) :
            modes.append(key)
    # if every value appears same amount of times
    if (len(modes) == len(countDictionary.keys())) :
        modes = []
    return modes

list1 = [ 5, 2, 7, 5, 7 ]
list2 = [ 8, 1, 2, 1, 8, 2 ]

print(getMode(list1))
print(getMode(list2))
