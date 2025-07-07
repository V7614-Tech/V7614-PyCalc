def input1(asentence):
    continue0="n"
    while (continue0=="n"):
        try:
            ainput=input (asentence)
            anumber=int(ainput)
            continue0="y"
        except:
            continue0="n"
            print ("Invalid input. Please input a number into this field.")
    return anumber

def logo():
    print ("PPPPPPPPPPPPPPPPP                                    CCCCCCCCCCCCC                  lllllll")
    print ("P::::::::::::::::P                                CCC::::::::::::C                  l:::::l")
    print ("P::::::PPPPPP:::::P                             CC:::::::::::::::C                  l:::::l")
    print ("PP:::::P     P:::::P                           C:::::CCCCCCCC::::C                  l:::::l")
    print ("  P::::P     P:::::Pyyyyyyy           yyyyyyy C:::::C       CCCCCC  aaaaaaaaaaaaa    l::::l     cccccccccccccccc")
    print ("  P::::P     P:::::P y:::::y         y:::::y C:::::C                a::::::::::::a   l::::l   cc:::::::::::::::c")
    print ("  P::::PPPPPP:::::P   y:::::y       y:::::y  C:::::C                aaaaaaaaa:::::a  l::::l  c:::::::::::::::::c")
    print ("  P:::::::::::::PP     y:::::y     y:::::y   C:::::C                         a::::a  l::::l c:::::::cccccc:::::c")
    print ("  P::::PPPPPPPPP        y:::::y   y:::::y    C:::::C                  aaaaaaa:::::a  l::::l c::::::c     ccccccc")
    print ("  P::::P                 y:::::y y:::::y     C:::::C                aa::::::::::::a  l::::l c:::::c")
    print ("  P::::P                  y:::::y:::::y      C:::::C               a::::aaaa::::::a  l::::l c:::::c")
    print ("  P::::P                   y:::::::::y        C:::::C       CCCCCCa::::a    a:::::a  l::::l c::::::c     ccccccc")
    print ("PP::::::PP                  y:::::::y          C:::::CCCCCCCC::::Ca::::a    a:::::a l::::::lc:::::::cccccc:::::c")
    print ("P::::::::P                   y:::::y            CC:::::::::::::::Ca:::::aaaa::::::a l::::::l c:::::::::::::::::c")
    print ("P::::::::P                  y:::::y               CCC::::::::::::C a::::::::::aa:::al::::::l  cc:::::::::::::::c")
    print ("PPPPPPPPPP                 y:::::y                   CCCCCCCCCCCCC  aaaaaaaaaa  aaaallllllll    cccccccccccccccc")
    print ("                          y:::::y")
    print ("                         y:::::y")
    print ("                        y:::::y")
    print ("                       y:::::y")
    print ("                      yyyyyyy")
    print ("")
    return

