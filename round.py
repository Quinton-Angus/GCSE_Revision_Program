import config
import functionsHub

def round(questions):

    print()
    print("Starting round...")
    print()
    print("#-------------------------------------------#")

    Qnum = 1

    score = 0

    for question in questions:
        print()
        print(f"Q{Qnum} - {question[0]}")
        print()
        ASCIInumA = ord("A")
        posAnsNum = 0
        for posAns in question[1]:
            print(f"({chr(ASCIInumA + posAnsNum)}) {posAns}")
            posAnsNum += 1
        print()
        userAnswer = input("> ").upper()
        print()
        result = userAnswer == question[2]

        if result == True:
            print("Correct!")
            score += 1
            input()
        else:
            print("Incorrect!")
            print()
            print("Reveal correct answer? (Y/N):")
            print()
            revealAnsInp = input("> ")

            tryRevealAns = True

            while tryRevealAns:

                if revealAnsInp.upper() == "Y" or revealAnsInp.upper() == "N":
                    tryRevealAns = False
                    if revealAnsInp.upper() == "Y":
                        print()
                        print(f"The correct answer was: {question[2]}")
                        input()
            

        print()

        print("------------------")

        print()

        Qnum += 1

    print("Compiling results...")
    print()
    print("#-------------------------------------------#")
    print()
    print(f"Results compiled, round score {score}/{config.questionsPerRound}")
    print("what would you like to do next?")
    print()
    print("[1] Exit program")
    print("[2] Start new round")
    print("[3] Back to home")
    print()

    selectTrue = True

    selected = None

    while selectTrue:

        try:

            selected = int(input("> "))

            selectTrue = False

        except ValueError:

            print("Please enter a valid option!")

    if selected == 1:
        functionsHub.exit()
    elif selected == 2:
        functionsHub.newRound()
    elif selected == 3:
        functionsHub.startProgram()

    print()
    print("#-------------------------------------------#")
    print()
    
