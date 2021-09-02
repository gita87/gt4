# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
sp = 0
mp = 0
lp = 0
if size == "S":
    sp += 15
    if add_pepperoni == "Y" :
        sp += 2
        if extra_cheese == "Y" :
            sp += 1
            print(f"Your bill is ${sp}")
        else:
            print(f"Your bill is ${sp}")
    elif extra_cheese == "Y" :
        sp += 1
        print(f"Your bill is ${sp}")
    else :
        print(f"Your bill is ${sp}")
elif size == "M" :
    mp += 20
    if add_pepperoni == "Y":
        mp += 3
        if extra_cheese == "Y":
            mp += 1
            print(f"Your bill is ${mp}")
        else:
            print(f"Your bill is ${mp}")
    elif extra_cheese == "Y":
        mp += 1
        print(f"Your bill is ${mp}")
    else:
        print(f"Your bill is ${mp}")
elif size == "L" :
    lp += 25
    if add_pepperoni == "Y":
        lp += 3
        if extra_cheese == "Y":
            lp += 1
            print(f"Your bill is ${lp}")
        else:
            print(f"Your bill is ${lp}")
    elif extra_cheese == "Y":
        lp += 1
        print(f"Your bill is ${lp}")
    else:
        print(f"Your bill is ${lp}")
else :
    print ("Dont waste my time")



