from data import questions
import random
from config import questionsPerRound

def generate(topicId):

    print()
    print(f"Generating questions for topic id: [{topicId}]")
    print()

    questionsToGen = questionsPerRound
    currentQuestionCount = 0

    questionList = questions[topicId]

    avaliableQuestions = questionList.copy.deepcopy()


    print(f"Avaliable questions: [{questionList}]")

    generatedQuestions = []

    while currentQuestionCount < questionsToGen:
        randomQuestionNumber =  random.randint(0, len(avaliableQuestions) - 1)

        questionInfo = avaliableQuestions[randomQuestionNumber]

        generatedQuestions.append(questionInfo)

        questionList.pop(randomQuestionNumber)

        currentQuestionCount += 1

    return generatedQuestions