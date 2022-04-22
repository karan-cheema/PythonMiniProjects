print("Welcome to the rollercoaster!")
name = input("What is your name?")
height = int(input(f"What is your height in centimeters, {name}?"))
bill = 0
if height >= 120:
    print(f"Just one more step before you can ride the rollercoaster, {name}")
    age = int(input("Can you tell us your age?"))
    if age <= 12:
        bill = 5
        print("Your ticket costs $5")
    elif age <=18:
        bill = 7
        print("Your ticket costs $7")
    else:
        bill = 12
        print("Your ticket costs $12")
    photo = input("Do you want a photo for $3? 'Y' for yes and 'N' for no")
    if photo == "Y":
        bill += 3

print(f"Your final bill is {bill}")

else:
    print("We are sorry, but you are too short to ride the rollercoaster.")
