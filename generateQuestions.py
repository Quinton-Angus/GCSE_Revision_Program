from questions import questions
import random

def generate(topicId):

    questionsToGen = 3
    currentQuestionCount = 0

    questionList = questions[topicId]

    generatedQuestions = []

    while currentQuestionCount < questionsToGen:
        randomQuestionNumber =  random.randint(0, len(questionList) - 1)

        questionInfo = questionList[randomQuestionNumber]

        generatedQuestions.append(questionInfo)

        questionList.pop(randomQuestionNumber)

        currentQuestionCount += 1

    return generatedQuestions