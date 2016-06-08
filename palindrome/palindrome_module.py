def palindrome(str):
    word_without_space = str.replace(" ", "")
    kutya = word_without_space.lower()
    if kutya == kutya[::-1]:
        return True
    else:
        return False


def main():
    word = input("Give me a word plz!")
    if palindrome(word):
        print("AAAAAhhhh yeah BABY!")
    else:
        print("LOSER")


if __name__ == '__main__':
    main()
