import random
import json
import time

from interruptingcow import timeout

from models.question_answer import QuestionAnswer
from models.ranking import Ranking

class Game:

    def __init__(self, name = None, id = None):
        self._name = name

        if id is None:
            qa_dict = random.choice(self.get_data())
        else:
            for qa_dict in self.get_data():
                if qa_dict['id'] == int(id):
                    break

        self._qa = QuestionAnswer(id=qa_dict['id'],
                                  question=qa_dict['question'],
                                  answer=qa_dict['answer'],
                                  keywords=qa_dict.get('keywords', None))
        self._total_score = 0
        self._timeout_set = False



    @property
    def qa(self):
        return self._qa

    def get_data(self):
        filename = 'data/data.json'
        with open(filename) as f:
            return json.load(f)

    def start(self, max_tijd = 30):
        PUNTEN_LADDER = [10, 20, 30, 40, 50]

        guessed_keywords = set()
        number_correct = 0

        t0 = time.time()

        if self._name:
            print(self._name)

        while True:
            time_remaining = round(max_tijd - (time.time() - t0))

            try:
                with timeout(time_remaining, exception=RuntimeError):
                    response = input(f'{self._qa.question} Met nog {time_remaining}s te gaan. ')

            except RuntimeError:
                print('\nDe tijd is voorbij.')
                break

            # if time.time() - t0 > max_tijd:
            #     print('De tijd is voorbij.')
            #     break

            if response == 'stop':
                break

            # elif response in guessed_keywords:
            elif self._qa.compare_to_keyword(response, keywords = guessed_keywords):
                print('Dat heb je al opgegeven.')
                continue

            keyword = self._qa.compare_to_keyword(response)

            if keyword:
                guessed_keywords.add(keyword)
                number_correct += 1
                punten = PUNTEN_LADDER[number_correct-1]
                self._total_score += punten
                print(f'Ja. {punten} punten.')

            else:
                print('NEE')

            if number_correct == 5:
                print('Alle vijf goed.')
                break

        if self._name:
            print(f'{self._name}. ', end = '')

        print(f'Je hebt {self._total_score} punten behaald.')

        return self._total_score, round(min(time.time() - t0, max_tijd), 1)


# ---------------------------------------

if __name__ == '__main__':

    name = input('Hoe heet je? ')

    game = Game(name)

    score, duration = game.start()

    ranking = Ranking()
    # ranking.add_score(name, duration, score)
    # ranking.store()
    ranking.append_to_sqlite({'name': name, 'duration': duration, 'score': score})

