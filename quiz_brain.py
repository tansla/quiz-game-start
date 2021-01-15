class QuizBrain:

    def __init__(self, questions):
        self.question_number = 0
        self.score = 0
        self.question_list = questions

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        if len(self.question_list) >= self.question_number:
            question = self.question_list[self.question_number]
            user_answer = input(f"Q.{self.question_number}: {question.text} (True/False)?").lower()
            self.question_number += 1
            self.check_answer(user_answer, question.answer)
        else:
            return "There is no more questions"

    def check_answer(self, u_answer, correct_answer):
        if u_answer.lower() == str(correct_answer).lower():
            self.score += 1
            print("You right!")
        else:
            print(f"You're wrong! The answer was: {str(correct_answer)}")
        print(f"Your current score: {self.score}/{len(self.question_list)}")
        print("\n")

    def final_score(self):
        return f"You're final score: {self.score}/{len(self.question_list)}"
