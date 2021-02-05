def makeList(x):
    wordList = []
    inc = 1
    for n,item in enumerate(x):
        if indicateChange(n,x):
            if n > 0:
                wordList.insert(len(wordList),(x[n-1],inc))
                if n == len(x) - 1:
                    wordList.insert(len(wordList),(x[n],1))
            elif n == 0:
                wordList.insert(len(wordList),(x[0],inc))
            inc = 1
        elif n > 0:
            inc += 1
            if n == len(x) - 1:
                wordList.insert(len(wordList),(x[n],inc))
    return wordList


def indicateChange(i,word):
    if i == 0:
        return False
    else:
        return str(word[i]) != str(word[i-1])
        

# Try like this:

output = makeList('aaaabbbccdad')
