from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = list()

for index in question_data:
    question_text = index["question"]
    question_answer = index["correct_answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")

