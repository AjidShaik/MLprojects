age = int(input("enter the age:"))
has_ticket = True

if age >= 18 and not has_ticket:
    print("You may allowed to watch the movie.")
elif age >= 18 and  has_ticket:
    print("You need a ticket to enter.")
elif age <=18 and  has_ticket:
    print("You are too young to enter.")
