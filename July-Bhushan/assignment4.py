# Assignment for login user

uname1="aman"
uname2="sagar"
uname3="vijay"
uname4="akash"

pwd=7777

username=input("Enter the username: ")
#password=int(input("Enter a Password: "))

if uname1 == username:
    print(f"Hey {uname1},Welcome")
    password=int(input("Enter password: "))
    if password == pwd:
        print("You are Loged in!")
    else:
        print("Sorry!,Your PASSWORD is incorrect")
elif uname2 == username:
    print(f"Hey {uname2},Welcome")
    password = int(input("Enter password: "))
    if password == pwd:
        print("You are Loged in!")
    else:
        print("Sorry!,Your PASSWORD is incorrect")
elif uname3 == username:
    print(f"Hey {uname3},Welcome")
    password = int(input("Enter password: "))
    if password == pwd:
        print("You are Loged in!")
    else:
        print("Sorry!,Your PASSWORD is incorrect")
elif uname4 == username:
    print(f"Hey {uname4},Welcome")
    password = int(input("Enter password: "))
    if password == pwd:
        print("You are Loged in!")
    else:
        print("Sorry!,Your PASSWORD is incorrect")
else:
    print("Sorry!, You have enter valid USERNAME")