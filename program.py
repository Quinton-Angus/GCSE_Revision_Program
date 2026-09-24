# Import functions

import messages
from topicSelector import selectTopic
from generateQuestions import generate
from round import round

# Backend

selectedTopic = None

# Functions

def runRound():
    selectedTopic = selectTopic()
    questions = generate(selectedTopic)
    round(questions)

# Main program script

messages.welcomeMes()
runRound()








