def main():
    path = "books/frankenstein.txt"
    text = read_book(path)
    #print(text)
    count = word_count(text)
    print(count)
    char = char_count(text)
    print(char)


def read_book(path):
    with open(path) as f:
        return f.read()
    
def word_count(text):
    return len(text.split())

def char_count(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    count = {}
    low_text = text.lower()
    for char in alphabet:
        count[char] = 0
    for char in low_text:
        if char in alphabet:
            count[char] += 1
        else:
            count[char] = 1
    return count




main()
