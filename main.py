import json
path = "userData.txt"

def loadUserData():
    try:
        with open(path, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data

def saveUserData(data):
    with open(path, "w") as file:
        json.dump(data, file, indent=4)

print("Welcome to the user database!")
userData = loadUserData()
userInput = int(input("1 - Start App | 2 - Stop App: "))
while userInput != 2:
    options = int(input("1 - List all users, 2 - Add user, 3 - Remove user, 4 - Search for a user by username: "))
    if options == 1:
        if userData:
            print("List of all users: ")
            print("--------------------")
            for username, userInfo in userData.items():
                print(f"Username: {username}")
                userInfo = userData[username]
                for key, value in userInfo.items():
                    print(f"{key}: {value}")
                print("--------------------")
        else:
            print("List currently empty...")
    elif options == 2:
        newUser = input("Enter username: ")
        if newUser in userData:
            print("Username already exists! ")
        else:
            fName = input("Enter first name: ")
            lName = input("Enter last name: ")
            hobbies = input("Enter hobbies(split with comma): ").split(',')
            age = int(input("Enter age: "))
            userData[newUser] = {
                "First Name": fName,
                "Last Name": lName,
                "Hobbies": hobbies,
                "Age": age,
            }
            saveUserData(userData)
            print("User added successfully!")
    elif options == 3:
        deleteUser = input("Enter username: ")
        if deleteUser in userData:
            userData.pop(deleteUser)
            saveUserData(userData)
            print("User deleted successfully!")
        else:
            print(f"User {deleteUser} was not found.")
    elif options == 4:
        searchUser = input("Enter username: ")
        if searchUser in userData:
            print(f"Here is all the info on the user {searchUser}: ")
            userInfo = userData[searchUser]
            for key, value in userInfo.items():
                 print(f"{key}: {value}")
        else:
            print(f"User {searchUser} was not found.")
    userInput = int(input("1 - Continue | 2 - Stop App: "))
print("Exiting the user database. Goodbye!")