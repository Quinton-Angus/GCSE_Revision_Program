## IMPORTS ##

import generateQuestions
import round
import topicSelector
import configEditor

## IMPORTS ##

# start new round

def newRound():
    round.round(generateQuestions.generate())

# exit program

def exit():
    print()
    print("Exiting program...")
    print()

# select topic

def selectTopic():
    topicSelector.selectTopic()

# config editor

def openConfigEditor():
    configEditor.edit()

# Restart program

def startProgram():
    print("Press * for config editor.")
    print()
    print("Welcome, what are you going to revise today?")
    print()
    print("#-------------------------------------------#")

    configInp = input()

    if configInp == "*":
        openConfigEditor()
    else:
        selectTopic()
        newRound()