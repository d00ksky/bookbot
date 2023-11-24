def main():
    path = "books/frankenstein.txt"
    text = read_book(path)
    #print(text)
    count = word_count(text)
    print(count)
    


def read_book(path):
    with open(path) as f:
        return f.read()
    
def word_count(text):
    return len(text.split())

main()
