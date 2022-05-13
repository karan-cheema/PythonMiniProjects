import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

random = random.randint(0,1)
if random == 1:
    print("heads")
else:
    print("tails")
