#WordIndex.py
#Name:
#Date:
#Assignment:

def main():
    words = {}  # create an empty dictionary
    lineNum = 0

    with open("fish.txt", 'r') as textFile:
        for line in textFile:
            lineNum += 1
            wordList = line.split()
            for w in wordList:
                w = w.lower().replace(",", "").replace(".", "").replace("!", "")
                if w in words:
                    if lineNum not in words[w]:
                        words[w].append(lineNum)
                else:
                    words[w] = [lineNum]

    for word in words:
        print(word, words[word])

if __name__ == '__main__':
    main()
