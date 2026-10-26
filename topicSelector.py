import config
from data import topics

def invalidTopic():
    print("Invalid topic, please try again!")

def printTopics():

    num = 1

    for topic in topics:
        print(f"[{num}] {topic}")
        num = num + 1


def verifyInput(input):
    if input >= 0 and input <= (len(topics) - 1):
        return(True)
    else: 
        return(False)


def selectTopic() :
    print()
    print("Select a topic:")
    print()
    printTopics()
    print()

    topicSelected = False

    while topicSelected == False:
        
        try:

            topic = int(input("> ")) - 1

            verify = verifyInput(topic)

            if verify == True: 
                topicSelected = True 
            else:
                invalidTopic() 

        except ValueError:
            invalidTopic()

    print()
    ("------------------")

    config.selectedTopic = topic

    return