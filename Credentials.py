print("Enter Details to Play!")
while True:
    ID = input("Choose a Username - ")
    pwd = input("Choose a pwd -  ")
    pwd_confirm = input("pwd confirmation required -  ")

    if pwd != pwd_confirm:
        print("pwd incorrect. Try Again!")

    if pwd == pwd_confirm:
        print("Account creation successful!")
        text_file = open("name.txt","a")
        text_file.write("\n")
        text_file.write(ID)
        text_file.write("\n")
        text_file.write(pwd)
        text_file.close()
        break
