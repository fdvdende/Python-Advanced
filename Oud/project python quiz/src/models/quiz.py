import os
import json
import random
from datetime import datetime

from question_answer import QuestionAnswer
from ranking import Ranking

class Quiz:
    def __init__(self, name = 'unknown'):
        self._name = name
        self._question_answers = self.get_data()
        self._number_of_questions = 0
        self._total_rating = 0
        self._start = None


    def __repr__(self):
        return str(self._question_answers)

    @property
    def name(self):
        return self._name

    def get_data(self):
        filename = '../data/data.json'
        with open(filename) as f:
            return json.load(f)

    def select_question_answers(self, k = 10):
        return random.sample(self._question_answers, k = min(k, len(self._question_answers)))

    def start(self, k = 10):
        self._start = datetime.now()

        for qa_dict in self.select_question_answers(k):
            qa = QuestionAnswer(id = qa_dict['id'],
                                question=qa_dict['question'],
                                answer=qa_dict['answer'],
                                keywords=qa_dict.get('keywords', None))

            response = input(qa)
            rating = qa.rate_response(response)

            self._number_of_questions += 1
            self._total_rating += rating

        return self._start, self._number_of_questions, self._total_rating


# --------------------

if __name__ == '__main__':

    name = input('Hoe heet je? ')

    quiz = Quiz(name)

    started, number_of_questions, total_rating = quiz.start(2)

    score = total_rating / number_of_questions

    print(f'{quiz._name}. Jouw score is {score}. Gestart om {started}')

    ranking = Ranking()
    ranking.add_score(quiz._name, started, score)
    ranking.store()

    # for quiz in ranking.top_ten():
    #     print(quiz)