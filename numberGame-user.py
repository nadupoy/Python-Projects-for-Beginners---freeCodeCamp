import random

number_01 = random.randint(1, 5)
number_02 = input("Guess a number between 1 and 5. ")
number_02 = int(number_02)

while number_01 != number_02:
    print(number_01, number_02)
    print("The numbers are not a match. 😔\n")
    number_01 = random.randint(1, 5)
    number_02 = input("Guess a number between 1 and 5. ")
    number_02 = int(number_02)
else:
    print(number_01, number_02)
    print("The numbers are a match! 😃")