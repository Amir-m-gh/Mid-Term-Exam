import json
from collections import OrderedDict

islogin = False


def submit():
    if islogin:
        print("You are logged in. Please logout of this account first.")
        return
    user = input("Please Enter your user name:\n===> ")
    dct = jsRead()
    if user in dct:
        print("Username already exists! Please try a new username.")
        return
    passw = input("Please enter a password with at least 8 characters:\n===> ")
    if len(passw) < 8:
        print("Your password is too short. Please try again")
        return
    dct = jsRead()
    dct[user] = passw
    jsWrite(dct)
    print("Submit completed successfully")
    with open("userScore.txt") as f:
        dct2 = json.load(f)
    with open("userScore.txt", "w") as f:
        dct2[user] = 0
        json.dump(dct2, f)
    with open("shop.json") as f:
        dct3 = json.load(f)
    with open("shop.json", "w") as f:
        dct3[user] = []
        json.dump(dct3, f)


def login():
    global islogin
    if islogin:
        print("You are already logged in!")
        return
    global logUser
    logUser = input("Please enter your Username:\n===> ")
    dct = jsRead()
    if logUser not in dct:
        print("Username does not exist. PLease enter a valid username.")
        return
    passw = input("PLease enter your Password:\n===> ")
    dct = jsRead()
    if dct[logUser] == passw:
        print("Welcome", logUser, "!")
        islogin = True
    else:
        print("Wrong password! Please try again.")


def shop():
    global islogin
    global logUser
    if not islogin:
        print("You need to log into your account first.")
        return
    print("Welcome to shop", logUser)
    with open("product.json") as f:
        dct = json.load(f)
        print("Here is our Products")
        print(dct)
    buy = input("Please enter the name of the product you want to purchase:\n===>")
    if buy in dct:
        x = int(dct[buy])
        if x == 0:
            print("Product is out of stocks. Please try again later or buy another product.")
            return
        else:
            y = x - 1
            dct[buy] = y
        with open("product.json", "w") as f:
            json.dump(dct, f)
        with open("shop.json") as f:
            stat = json.load(f)
        with open("shop.json", "w") as f:
            stat[logUser].append(buy)
            json.dump(stat, f)
        with open("score.json") as f:
            score = json.load(f)
            a = int(score[buy])
            a += 1
            score[buy] = a
        with open("score.json", "w") as f:
            json.dump(score, f)

        with open("userScore.txt") as f:
            userScore = json.load(f)
        with open("userScore.txt", "w") as f:
            x2 = int(userScore[logUser])
            x2 += 1
            userScore[logUser] = x2
            json.dump(userScore, f)
            print(x2)


def shopList():
    with open("shop.json") as f:
        dct = json.load(f)
        print(dct)


def OutOfStuck():
    lst = []
    with open("product.json") as f:
        dct = json.load(f)
        for item in dct:
            if dct[item] == 0:
                lst.append(item)
    print(lst)


def popular():
    with open("score.json") as f:
        dct = json.load(f)
        largest = max(dct, key=dct.get)
        x = dct[largest]
        dct2 = {}
        dct2[largest] = x
        print(dct2)


def elitUser():
    with open("userScore.txt") as f:
        dct = json.load(f)
        largest = max(dct, key=dct.get)
        x = dct[largest]
        dct2 = {}
        dct2[largest] = x
        print(dct2)


def logout():
    global islogin
    global logUser
    if not islogin:
        print("You are already logged out!")
        return
    confirm = input("Are you sure?(yes/no):\n===> ")
    if confirm == "yes":
        print("Logout successful. Bye", logUser)
        islogin = False


def jsRead():
    with open("info.json") as f:
        dct = json.load(f)
    return dct


def jsWrite(dct):
    with open('info.json', 'w') as f:
        json.dump(dct, f)


while True:
    demand = input('''What do you want to do?
(submit, login, shop, shopList, outstock, popular, eliteUsers, logout, exit)\n===> ''')

    if demand == "submit":
        submit()
    elif demand == "login":
        login()
    elif demand == "shop":
        shop()
    elif demand == "shopList":
        shopList()
    elif demand == "outstock":
        OutOfStuck()
    elif demand == "popular":
        popular()
    elif demand == "eliteUser":
        elitUser()
    elif demand == "logout":
        logout()
    elif demand == "exit":
        break
    else:
        print("Invalid input! Please try again.")
