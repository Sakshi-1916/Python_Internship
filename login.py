
login = {}
print("welcome!! please enter your details.")
username = str(input("Enter a username:"))
password = str(input("Create password:"))
login['username'] = username
while len(password) != 8:
    print("weak password!!")
    password = str(input("please create a strong password:"))
    login['password'] = password
else:
    login['password'] = password
    print("Account created succesful!")
print(login)
choice=int(input("Do you wanna login?(1/0)"))
un=str(input("Enter your username:"))
pw=str(input("Enter your password:"))
if choice != 1:
    print("Bye")
else:
    while un != login.get('username') or pw != login.get('password'):
        print("username or password is incorrect!")
        choice=int(input("Do you wanna login?(1/0)"))
        if choice == 0:
            print("Bye")
            break
        un=str(input("Enter your username:"))
        pw=str(input("Enter your password:"))
    else:
        print("login success!")
        
