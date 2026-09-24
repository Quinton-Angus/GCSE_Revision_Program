def round(questions):

    Qnum = 1

    score = 0

    for question in questions:
        print()
        print(f"Q{Qnum} - {question[0]}")
        print()
        print(f"(A) {question[1][0]}")
        print(f"(B) {question[1][1]}")
        print()
        userAnswer = input("> ").upper()
        print()
        result = userAnswer == question[2]

        if result == True:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

        print()

        print("------------------")

        print()

        Qnum += 1

    print("Compiling results...")
    print()
    print("#-------------------------------------------#")
    print()
    print(f"Results compiled, round score {score}/3")
    print("what would you like to do next?")
    print()
    print("[1] Exit program")
    print("[2] Start new round")
    print("[3] null")

    selectTrue = True

    while selectTrue:

        try:

            selected = int(input("> "))

            selectTrue = False

        except ValueError:

            print("Please enter a valid option!")