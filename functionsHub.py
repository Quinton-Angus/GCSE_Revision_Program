## IMPORTS ##

import program
import generateQuestions
import round
import topicSelector

## IMPORTS ##


# Restart program

def restart():
    print()
    print("Welcome, what are you going to revise today?")
    print()
    print("#-------------------------------------------#")

# start new round

def newRound(topic):
    round.round(generateQuestions.generate(topic))

# exit program

def exit():
    print()
    print("Exiting program...")
    print()

# select topic

def selectTopic():
    return topicSelector.selectTopic()