# TASK: Write a function that shifts each letter in a string by a given number.

# Define a function that takes a string and an integer shift value as parameters  
def shifter(number: int, word: str) -> str:
    letter_list = [letter for letter in word]
    codes = []
    for letter in letter_list:
        codes.append(ord(letter) + number)
    for code in codes:
        chr(code - number)
    print(codes)



word = input("Please enter a word. ")
number = int(input("Pick a number. "))
shifter(number, word)




fruits = ["banana", "apple", "pineapple"]
newcodes = []

for fruit in fruits:
    newcodes.append(ord(fruit) + 5)