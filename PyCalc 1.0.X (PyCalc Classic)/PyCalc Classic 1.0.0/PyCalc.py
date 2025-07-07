#"Welcome to PyCalc's code! a, b, and d are inputs and c is result"
a = 0
b = 0
c = 0
d = 0
name=str

name="PyCalc"
input ("Welcome to PyCalc Classic 1.0.0! Press Enter to begin calculating.")
ok="n"
continue0="no"
while (continue0=="no"):
    try:
        d=input ("type in the first number:")
        a=int(d)
        continue0="yes"
    except:
        continue0="no"
        print ("Invalid input. Please input a number into this field.")
c=int(a)
continue1="yes"
while (continue1=="yes"):
    while (ok=="n"):
        continue0="no"
        while (continue0=="no"):
            try:
                d=input ("type in the next number:")
                b=int(d)
                continue0="yes"
            except:
                continue0="no"
                print ("Invalid input. Please input a number into this field.")
        do = input("what should PyCalc do with these numbers?: choices are add, +, subtract, -, multiply, *, divide, /, power, and **")
        if (do=="add") or (do=="+") or (do=="subtract") or (do=="-") or (do=="multiply") or (do=="*") or (do=="divide") or (do=="/") or (do=="power") or (do=="**"):
            ok="y"
    match do:
        case "add":
            c=c + int(b)
            print(c)
            continue1=input("Would you like to continue this equation? Type yes or no (Case Sensitive)")
            if (continue1=="no"):
                print("Thank you for using PyCalc")
                break
            else:
                ok="n"
                continue
        case "+":
            c=c + int(b)
            print(c)
            continue1=input("Would you like to continue this equation? Type yes or no (Case Sensitive)")
            if (continue1=="no"):
                print("Thank you for using PyCalc")
                break
            else:
                ok="n"
                continue
        case "subtract":
            c=c - int(b)
            print(c)
            continue1=input("Would you like to continue this equation? Type yes or no (Case Sensitive)")
            if (continue1=="no"):
                print("Thank you for using PyCalc")
                break
            else:
                ok="n"
                continue
        case  "-":
            c=c - int(b)
            print(c)
            continue1=input("Would you like to continue this equation? Type yes or no (Case Sensitive)")
            if (continue1=="no"):
                print("Thank you for using PyCalc")
                break
            else:
                ok="n"
                continue
        case "multiply":
            c=c * int(b)
            print(c)
            continue1=input("Would you like to continue this equation? Type yes or no (Case Sensitive)")
            if (continue1=="no"):
                print("Thank you for using PyCalc")
                break
            else:
                ok="n"
                continue
        case "*":
            c=c * int(b)
            print(c)
            continue1=input("Would you like to continue this equation? Type yes or no (Case Sensitive)")
            if (continue1=="no"):
                print("Thank you for using PyCalc")
                break
            else:
                ok="n"
                continue
        case "divide":
            c=c / int(b)
            print(c)
            continue1=input("Would you like to continue this equation? Type yes or no (Case Sensitive)")
            if (continue1=="no"):
                print("Thank you for using PyCalc")
                break
            else:
                ok="n"
                continue
        case "/":
            c=c / int(b)
            print(c)
            continue1=input("Would you like to continue this equation? Type yes or no (Case Sensitive)")
            if (continue1=="no"):
                print("Thank you for using PyCalc")
                break
            else:
                ok="n"
                continue
        case "power":
            c=c ** int(b)
            print(c)
            continue1=input("Would you like to continue this equation? Type yes or no (Case Sensitive)")
            if (continue1=="no"):
                print("Thank you for using PyCalc")
                break
            else:
                ok="n"
                continue
        case "**":
            c=c ** int(b)
            print(c)
            continue1=input("Would you like to continue this equation? Type yes or no (Case Sensitive)")
            if (continue1=="no"):
                print("Thank you for using PyCalc")
                break
            else:
                ok="n"
                continue
        case _:
            print ("Invalid operation. Please check your spelling and rerun " + (name))
            ok="n"
input("Type anything to close this window")