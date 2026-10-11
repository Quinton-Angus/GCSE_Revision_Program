## IMPORTS ##

import generateQuestions
import round
import topicSelector

## IMPORTS ##

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

# Restart program

def restart():
    print()
    print("Welcome, what are you going to revise today?")
    print()
    print("#-------------------------------------------#")
    
    newRound(selectTopic())