<<<<<<< HEAD
name = input("Hi, welcome to the pizza place, what is your name?")
=======
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("INVALID INPUT: Please start again!")

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    elif size == "M":
        bill += 3
    elif size == "L":
        bill += 3
    else:
        print("INVALID INPUT: Please start again!")

if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}.")
>>>>>>> 0e413b6924c9a01245c04e12cbda65f35f9a471e