password = ""
attempts = 0

while attempts<3:
    password = input("Enter the password")
    if password == "Chethana143":
        print("Access granted.")
        break
    else:
        print("Wrong password.")
        attempt +=1
else:
        print("to many times.")
        