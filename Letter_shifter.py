# TASK: Write a function that shifts each letter in a string by a given number.

# Define a function that takes a string and an integer shift value as parameters  
def shifter(number: int, word: str) -> str:
    letter_list = list(word)
    for letter in letter_list:
        codes.append(chr(ord(letter) + number))
    print(codes)
    return codes

def deshifter(number: int) -> str:
    reword_list = []
    for code in codes:
        reword_list.append(chr(ord(code) - number))
    print(reword_list)

word = input("Please enter a word. ")
number = int(input("Pick a number. "))
codes = []
shifter(number, word)
deshifter(number)