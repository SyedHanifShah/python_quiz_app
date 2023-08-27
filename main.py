from data import question_data
from question_model import Question
from quiz_brain import QuiBrain

question_bank = []

for question in question_data:
    ques_text = question["text"]
    ques_answer = question["answer"]
    question_data = Question(text=ques_text, answer=ques_answer)
    question_bank.append(question_data)

quiz = QuiBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print(f"You've compeleted the quiz")
print(f"Your final score is:{quiz.score} / {quiz.question_number}")

