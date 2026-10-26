from data import questions
import random
import config
import copy

def generate():

    topicId = config.selectedTopic

    questionsToGen = config.questionsPerRound
    currentQuestionCount = 0

    questionList = questions[topicId]

    avaliableQuestions = copy.deepcopy(questionList)

    generatedQuestions = []

    while currentQuestionCount < questionsToGen:
        randomQuestionNumber =  random.randint(0, len(avaliableQuestions) - 1)

        questionInfo = avaliableQuestions[randomQuestionNumber]

        generatedQuestions.append(questionInfo)

        avaliableQuestions.pop(randomQuestionNumber)

        currentQuestionCount += 1

    return generatedQuestions