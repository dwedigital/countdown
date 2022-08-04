import requests


def getWords() -> list:
    data = requests.get("https://www.mit.edu/~ecprice/wordlist.10000")
    words: list = data.text.split("\n")
    return words


def getLetters() -> str:
    letters: str = input("Enter letters: ")
    letters.strip()
    return letters


def findWords(letters: str, words: list) -> set:
    possibleWords: list = []
    for word in words:
        for letter in word:
            if letter not in letters:
                break
        else:
            possibleWords.append(word)

    for word in possibleWords:
        for letter in letters:
            if word.count(letter) > 1 or len(word) > len(letters):
                possibleWords.remove(word)
                break

    possibleWords = sorted(possibleWords, key=len, reverse=True)
    finalList:set = set(possibleWords)
    return finalList


if __name__ == "__main__":
    dictionary:list = getWords()
    letters:list = getLetters()

    print(findWords(letters, dictionary))
