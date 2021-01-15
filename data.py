import requests
from question_model import Question
import html


class QuestionBank:

    def __init__(self, number_of_questions):

        self._number_of_questions = number_of_questions
        trivia_url = "https://opentdb.com/api.php"
        trivia_params = {
            'amount': number_of_questions,
            'type': 'boolean'
        }

        trivia_respond = requests.get(url=trivia_url, params=trivia_params)
        trivia_respond.raise_for_status()
        self._question_data = trivia_respond.json()['results']
        self._question_bank = []
        for item in self._question_data:
            question = html.unescape(item["question"])
            answer = html.unescape(item["correct_answer"])
            self._question_bank.append(Question(question, answer))

    def get_all_questions(self):
        return self._question_bank

