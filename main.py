from data import QuestionBank
from quiz_brain import QuizBrain
from ui import QuizInterface

number_of_questions = 10

question_bank = QuestionBank(number_of_questions).get_all_questions()
quiz = QuizBrain(question_bank)

# while quiz.still_has_questions():
#     quiz.next_question()

# print(quiz.final_score())

quizUI = QuizInterface(quiz)