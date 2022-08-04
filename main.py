import requests


def getWords() -> list:
    d = requests.get("https://www.mit.edu/~ecprice/wordlist.10000")
    words = d.text.split("\n")
    return words


def getLetters() -> str:
    letters = input("Enter letters: ")
    letters.strip()
    return letters


def findWords(letters: str, words: list) -> list:
    possibleWords = []
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

    return sorted(possibleWords, key=len, reverse=True)


if __name__ == "__main__":
    dictionary = getWords()
    letters = getLetters()

    print(findWords(letters, dictionary))
