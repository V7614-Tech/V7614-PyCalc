#"Welcome to PyCalc's code!"
import PyCalc_functions
a = 0
b = 0
c = 0
d = 0
name=str
version=str
majorversion=str
creator=str
is_indevpreview=str
indevpreviewnumber=int
version1=str

name="PyCalc"
majorversion="Alpha"
version="1.1.0"
creator="V7614"
is_indevpreview="no"
indevpreviewnumber=1
if (is_indevpreview=="yes"):
    version1=(majorversion) + " " + (version) + " InDev Preview " + str(indevpreviewnumber)
else:
    version1=(majorversion) + " " + (version)

PyCalc_functions.logo()

print ("Welcome to " + (name) + " " + (version1) + " by " + (creator) + "!")
ok="n"
a = PyCalc_functions.input1("Input the first number (<first number> <action (+ or - or * or / or **)> <next digit>) to begin:")
c=int(a)
continue1="y"
while (continue1=="y"):
    while (ok=="n"):
        b = PyCalc_functions.input1("type in the next number:")
        operation_ok="n"
        while (operation_ok=="n"):
            print ("Here are the options " + (name) + " can do below. All options including text form and symbols work")
            do = input("add (+), subtract (-), multiply (*), divide (/), and power (**): ")
            if (do=="add") or (do=="+") or (do=="subtract") or (do=="-") or (do=="multiply") or (do=="*") or (do=="divide") or (do=="/") or (do=="power") or (do=="**"):
                ok="y"
                operation_ok="y"
            else:
                print ("Invalid input. Please type one of the options to the side of the prompt.")
    match do:
        case "add" | "+":
            c=c + int(b)
            print(c)
            continue1=input("Do you want to continue your equation? Type [y]es or [n]o (Case Sensitive, first letter only)")
            if (continue1=="n"):
                print("Thank you for using " + (name) + " " + (version1))
                break
            else:
                if (continue1=="y"):
                   ok="n"
                   continue
                else:
                   print("Invalid input.")
        case "subtract" | "-":
            c=c - int(b)
            print(c)
            continue1=input("Do you want to continue this equation? Type [y]es or [n]o (Case Sensitive, first letter only)")
            if (continue1=="n"):
                print("Thank you for using " + (name) + " " + (version1))
                break
            else:
                if (continue1=="y"):
                   ok="n"
                   continue
                else:
                   print("Invalid input.")
        case "multiply" | "*":
            c=c * int(b)
            print(c)
            continue1=input("Do you want to continue this equation? Type [y]es or [n]o (Case Sensitive, first letter only)")
            if (continue1=="n"):
                print("Thank you for using " + (name) + " " + (version1))
                break
            else:
                if (continue1=="y"):
                   ok="n"
                   continue
                else:
                   print("Invalid input.")
        case "divide" | "/":
            c=c / int(b)
            print(c)
            continue1=input("Do you want to continue this equation? Type [y]es or [n]o (Case Sensitive, first letter only)")
            if (continue1=="n"):
                print("Thank you for using " + (name) + " " + (version1))
                break
            else:
                if (continue1=="y"):
                   ok="n"
                   continue
                else:
                   print("Invalid input.")
        case "power" | "**":
            c=c ** int(b)
            print(c)
            continue1=input("Do you want to continue this equation? Type [y]es or [n]o (Case Sensitive, first letter only)")
            if (continue1=="n"):
                print("Thank you for using " + (name) + " " + (version1))
                break
            else:
                if (continue1=="y"):
                   ok="n"
                   continue
                else:
                   print("Invalid input.")
input("All actions complete. Press enter to exit.")