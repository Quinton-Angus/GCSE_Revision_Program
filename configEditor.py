import functionsHub
import config

def edit():
    print()
    print("#-------------------------------------------#")
    print()
    print("Welcome to the config editor! choose an option to continue:")

    configUsrInp = True
    configInp = None

    while configUsrInp:

        print()
        print("[1] Close editor an retrun to home")
        print("[2] Edit questions per round")
        print("[3] Edit debug mode")
        print()
        configInp = input("> ")

        if configInp != "1" and configInp != "2" and configInp != "3":
            print("Invalid input, please try again!")
        else:
            configUsrInp = False


    if configInp == "1":

        print()
        print("#-------------------------------------------#")
        print()

        functionsHub.startProgram()

    elif configInp == "2":

        newQPRUsrInp = True
        
        newQPRInp = True

        while newQPRUsrInp == True:

            try:
                print()
                print("Enter new number of questions per round:")
                print()
                newQPRInp = int(input("> "))
                print()
                newQPRUsrInp = False
            except ValueError:
                print("Invalid input, please try again!")
                print()

        config.questionsPerRound = newQPRInp
        print("New value accepted, exiting config editor...")
        print()
        functionsHub.startProgram()
    else:
        newDebugModeUsrInp = True

        while newDebugModeUsrInp:

            print()
            print("Select a debug mode (True / False): ")
            print()
            newDebugModeInp = input("> ")
            print()

            if newDebugModeInp != "True" and newDebugModeInp != "False":
                print("Invalid value, please try again!")
            else:
                newDebugModeUsrInp = False

        config.debug = bool(newDebugModeInp)
        print("New value accepted, exiting config editor...")
        print()
        functionsHub.startProgram()

        
