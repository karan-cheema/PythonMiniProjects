import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
names_len = len(names)
name_random = random.randint(0, names_len -1)
person_paying = names[name_random]
print(f"{person_paying} is going to buy the meal today!")
