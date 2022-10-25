from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    storage = Question(question["text"], question["answer"])
    question_bank.append(storage)

quizbrain = QuizBrain(question_bank)
correct_number = 0
wrong_number = 0
while quizbrain.still_has_question():
    if quizbrain.next_question() == quizbrain.question_list[quizbrain.question_number-1].answer:
        correct_number += 1
    else:
        wrong_number += 1
    print(f"Your correct rate is {correct_number}:{wrong_number}")


