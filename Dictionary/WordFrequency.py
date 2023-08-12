words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 

def countWordFrequency(wordsList):
    uniqueDict = {}
    for word in wordsList:
        print(word)
        uniqueDict[word] = wordsList.count(word)
    return uniqueDict

print(countWordFrequency(words))