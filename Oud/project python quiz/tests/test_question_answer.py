import unittest

from ..src.models.question_answer import QuestionAnswer


class TestQuestionAnswer(unittest.TestCase):

    def test_instantiation(self):
        qa = QuestionAnswer(id=0,
                            question='...',
                            answer='...',
                            keywords=[])

        self.assertIsInstance(qa, QuestionAnswer)

    def test_rank_correct_response(self):
        qa = QuestionAnswer(id=0,
                            question='Welke kleuren heeft de Nederlandse vlag?',
                            answer='Rood, wit en blauw',
                            keywords=['rood', 'wit', 'blauw'])

        response = 'rood, wit en blauw'

        actual = qa.rate_response(response)
        expected = 10

        self.assertEqual(expected, actual)

    def test_rank_incorrect_response(self):
        qa = QuestionAnswer(id=0,
                            question='Welke kleuren heeft de Nederlandse vlag?',
                            answer='Rood, wit en blauw',
                            keywords=['rood', 'wit', 'blauw'])

        response = 'geen idee'

        actual = qa.rate_response(response)
        expected = 0

        self.assertEqual(expected, actual)

    def test_extract_keywords(self):
        qa = QuestionAnswer(id=0,
                            question='Welke kleuren heeft de Nederlandse vlag?',
                            answer='Rood, wit en blauw')

        actual = qa.keywords
        expected = {'rood', 'wit', 'blauw'}

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
