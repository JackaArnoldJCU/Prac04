import random
how_many_generated = int(input("How many quick select:"))

def random_numbers():
    numbers = []
    for i in range(5):
        numbers.append(random.randint(1,45))

    print(numbers)



for i in range(how_many_generated):

    random_numbers()