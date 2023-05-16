import random

number_01 = random.randint(1, 100)
number_02 = random.randint(1, 100)

while number_01 != number_02:
    print(number_01, number_02)
    print("The numbers are not a match. 😔\n")
    number_01 = random.randint(1, 100)
    number_02 = random.randint(1, 100)
else:
    print(number_01, number_02)
    print("The numbers are a match! 😃")