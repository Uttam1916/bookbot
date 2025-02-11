def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    prin(char(text))


def get_num_words(text):
    words = text.split()
    return len(words)

def char(text):
    dic={}
    words=text.split()
    for word in words:
        for letter in word:
            if letter.lower() not in dic:
                dic[letter.lower()]=1
            else:
                dic[letter.lower()]+=1
    return dic
def prin(dic):
    for key,value in dic.items():
        print("the character",key,"has been found",value,"times")
def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
