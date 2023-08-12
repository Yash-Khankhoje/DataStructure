userStatement = "Coding is cool addiction of coder tell it to your tuter"
statementList = userStatement.split(" ")

def subStrArrCreater(subStrArr):
    for word in subStrArr:
        for i in range(0, len(word)):
            for j in range(i+1, len(word)+1):
                subStr = word[i:j]
                if subStr not in subStrArr and len(subStr) > 1:
                    subStrArr.append(subStr)
    return(subStrArr)
subStrArray = subStrArrCreater(statementList)

for i in subStrArray:
    if userStatement.lower().count(i.lower()) > 1:
        print(i)
