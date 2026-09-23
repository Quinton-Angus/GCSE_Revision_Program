# Import functions

import messages
from topicSelector import selectTopic
from generateQuestions import generate

# Backend

selectedTopic = None

# Main program script

messages.welcomeMes()
selectedTopic = selectTopic()

questions = generate(selectedTopic)

print(questions)



