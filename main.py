from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizUI

question_bank = list()

for index in question_data:
    question_text = index["question"]
    question_answer = index["correct_answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizUI(quiz_brain=quiz)

