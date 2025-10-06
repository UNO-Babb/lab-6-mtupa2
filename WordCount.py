#WordCount.py
#Name:
#Date:
#Assignment:

def main():
    lineCount = 0
    wordCount = 0
    characterCount = 0

    with open("gettysberg.txt", 'r') as textFile:
        for line in textFile:
            lineCount = lineCount + 1
            characterCount = characterCount + len(line)
            words = line.split()
            wordCount = wordCount + len(words)

    print("Lines:", lineCount)
    print("Words:", wordCount)
    print("Characters:", characterCount)

if __name__ == '__main__':
    main()
