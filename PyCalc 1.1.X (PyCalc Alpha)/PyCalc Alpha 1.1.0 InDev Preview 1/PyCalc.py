#"Welcome to PyCalc's code! a, b, and d are inputs and c is result"
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
is_indevpreview="yes"
indevpreviewnumber=1
if (is_indevpreview=="yes"):
    version1=(majorversion) + " " + (version) + " InDev Preview " + str(indevpreviewnumber)
else:
    version1=(majorversion) + " " + (version)

def logo():
    print ("PPPPPPPPPPPPPPPPP                                    CCCCCCCCCCCCC                  lllllll                     ")
    print ("P::::::::::::::::P                                CCC::::::::::::C                  l:::::l                     ")
    print ("P::::::PPPPPP:::::P                             CC:::::::::::::::C                  l:::::l                     ")
    print ("PP:::::P     P:::::P                           C:::::CCCCCCCC::::C                  l:::::l                     ")
    print ("  P::::P     P:::::Pyyyyyyy           yyyyyyy C:::::C       CCCCCC  aaaaaaaaaaaaa    l::::l     cccccccccccccccc")
    print ("  P::::P     P:::::P y:::::y         y:::::y C:::::C                a::::::::::::a   l::::l   cc:::::::::::::::c")
    print ("  P::::PPPPPP:::::P   y:::::y       y:::::y  C:::::C                aaaaaaaaa:::::a  l::::l  c:::::::::::::::::c")
    print ("  P:::::::::::::PP     y:::::y     y:::::y   C:::::C                         a::::a  l::::l c:::::::cccccc:::::c")
    print ("  P::::PPPPPPPPP        y:::::y   y:::::y    C:::::C                  aaaaaaa:::::a  l::::l c::::::c     ccccccc")
    print ("  P::::P                 y:::::y y:::::y     C:::::C                aa::::::::::::a  l::::l c:::::c             ")
    print ("  P::::P                  y:::::y:::::y      C:::::C               a::::aaaa::::::a  l::::l c:::::c             ")
    print ("  P::::P                   y:::::::::y        C:::::C       CCCCCCa::::a    a:::::a  l::::l c::::::c     ccccccc")
    print ("PP::::::PP                  y:::::::y          C:::::CCCCCCCC::::Ca::::a    a:::::a l::::::lc:::::::cccccc:::::c")
    print ("P::::::::P                   y:::::y            CC:::::::::::::::Ca:::::aaaa::::::a l::::::l c:::::::::::::::::c")
    print ("P::::::::P                  y:::::y               CCC::::::::::::C a::::::::::aa:::al::::::l  cc:::::::::::::::c")
    print ("PPPPPPPPPP                 y:::::y                   CCCCCCCCCCCCC  aaaaaaaaaa  aaaallllllll    cccccccccccccccc")
    print ("                          y:::::y                                                                               ")
    print ("                         y:::::y                                                                                ")
    print ("                        y:::::y                                                                                 ")
    print ("                       y:::::y                                                                                  ")
    print ("                      yyyyyyy                                                                                   ")
    print ("")
logo()

print ("Welcome to " + (name) + " " + (version1) + " by " + (creator) + "!")
ok="n"
continue0="n"
while (continue0=="n"):
    try:
        d=input ("Input the first number (<first number> <action (+ or - or * or / or **)> <next digit>) to begin:")
        a=int(d)
        continue0="y"
    except:
        continue0="n"
        print ("Invalid input. Please input a number into this field.")
c=int(a)
continue1="y"
while (continue1=="y"):
    while (ok=="n"):
        continue0="n"
        while (continue0=="n"):
            try:
                d=input ("type in the next number:")
                b=int(d)
                continue0="y"
            except:
                continue0="n"
                print ("Invalid input. Please input a number into this field.")
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
        case "add":
            c=c + int(b)
            print(c)
            continue1=input("Do you want to continue your equation? Type [y]es or [n]o (Case Sensitive, first letter only)")
            if (continue1=="n"):
                print("Thank you for using " + (name) + " " + (version))
                break
            else:
                if (continue1=="y"):
                   ok="n"
                   continue
                else:
                   print("Invalid input.")
        case "+":
            c=c + int(b)
            print(c)
            continue1=input("Do you want to continue your equation? Type [y]es or [n]o (Case Sensitive, first letter only)")
            if (continue1=="n"):
                print("Thank you for using " + (name) + " " + (version))
                break
            else:
                if (continue1=="y"):
                   ok="n"
                   continue
                else:
                   print("Invalid input.")
        case "subtract":
            c=c - int(b)
            print(c)
            continue1=input("Do you want to continue this equation? Type [y]es or [n]o (Case Sensitive, first letter only)")
            if (continue1=="n"):
                print("Thank you for using " + (name) + " " + (version))
                break
            else:
                if (continue1=="y"):
                   ok="n"
                   continue
                else:
                   print("Invalid input.")
        case  "-":
            c=c - int(b)
            print(c)
            continue1=input("Do you want to continue this equation? Type [y]es or [n]o (Case Sensitive, first letter only)")
            if (continue1=="n"):
                print("Thank you for using " + (name) + " " + (version))
                break
            else:
                if (continue1=="y"):
                   ok="n"
                   continue
                else:
                   print("Invalid input.")
        case "multiply":
            c=c * int(b)
            print(c)
            continue1=input("Do you want to continue this equation? Type [y]es or [n]o (Case Sensitive, first letter only)")
            if (continue1=="n"):
                print("Thank you for using " + (name) + " " + (version))
                break
            else:
                if (continue1=="y"):
                   ok="n"
                   continue
                else:
                   print("Invalid input.")
        case "*":
            c=c * int(b)
            print(c)
            continue1=input("Do you want to continue this equation? Type [y]es or [n]o (Case Sensitive, first letter only)")
            if (continue1=="n"):
                print("Thank you for using " + (name) + " " + (version))
                break
            else:
                if (continue1=="y"):
                   ok="n"
                   continue
                else:
                   print("Invalid input.")
        case "divide":
            c=c / int(b)
            print(c)
            continue1=input("Do you want to continue this equation? Type [y]es or [n]o (Case Sensitive, first letter only)")
            if (continue1=="n"):
                print("Thank you for using " + (name) + " " + (version))
                break
            else:
                if (continue1=="y"):
                   ok="n"
                   continue
                else:
                   print("Invalid input.")
        case "/":
            c=c / int(b)
            print(c)
            continue1=input("Do you want to continue this equation? Type [y]es or [n]o (Case Sensitive, first letter only)")
            if (continue1=="n"):
                print("Thank you for using " + (name) + " " + (version))
                break
            else:
                if (continue1=="y"):
                   ok="n"
                   continue
                else:
                   print("Invalid input.")
        case "power":
            c=c ** int(b)
            print(c)
            continue1=input("Do you want to continue this equation? Type [y]es or [n]o (Case Sensitive, first letter only)")
            if (continue1=="n"):
                print("Thank you for using " + (name) + " " + (version))
                break
            else:
                if (continue1=="y"):
                   ok="n"
                   continue
                else:
                   print("Invalid input.")
        case "**":
            c=c ** int(b)
            print(c)
            continue1=input("Do you want to continue this equation? Type [y]es or [n]o (Case Sensitive, first letter only)")
            if (continue1=="n"):
                print("Thank you for using " + (name) + " " + (version))
                break
            else:
                if (continue1=="y"):
                   ok="n"
                   continue
                else:
                   print("Invalid input.")
input("All actions complete. Press enter to exit.")