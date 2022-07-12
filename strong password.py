password=input("enter your password:-")
if len(password)>=6 and len(password)<=9:
    if "@" in password or "#" in password or "$" in password:
        if "a" or "z" in password:
            if "A" or "Z" in password:
                print("strong password")
            else:
                print("your password is weak use uppercase")
        else:
            print("your password is weak use lower case")
    else:
        print("your password is weak use special characters")
else:
    print("weak password")
