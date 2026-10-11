from data import questions
import random
from config import questionsPerRound
import copy

def generate(topicId):

    print()
    print(f"Generating questions for topic id: [{topicId}]")
    print()

    questionsToGen = questionsPerRound
    currentQuestionCount = 0

    questionList = questions[topicId]

    avaliableQuestions = copy.deepcopy(questionList)


    print(f"Avaliable questions: [{questionList}]")

    generatedQuestions = []

    while currentQuestionCount < questionsToGen:
        randomQuestionNumber =  random.randint(0, len(avaliableQuestions) - 1)

        questionInfo = avaliableQuestions[randomQuestionNumber]

        generatedQuestions.append(questionInfo)

        avaliableQuestions.pop(randomQuestionNumber)

        currentQuestionCount += 1

    return generatedQuestions