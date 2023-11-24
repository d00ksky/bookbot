def main():
    path = "books/frankenstein.txt"
    text = read_book(path)
    count = word_count(text)
    char = char_count(text)
    report_print = report(path, count, char)
    print(report_print)
    
    
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

def report(path, count, char):
    print(f"--- Begin report of {path} ---")
    print(f"\nThe text contains {count} words \n")
    for c in char:
        if c.isalpha():
            print(f"The '{c}' character was found {char[c]} times")
    return "\n--- End of report ---"

main()