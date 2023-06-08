import string
import difflib

class QuestionAnswer:
    """Main class for out Question Answer Quiz. Just like 'Wat weet je van ...?' uit 'De Slimste mens'"""

    def __init__(self,
                 id: int,
                 question: str,
                 answer: str,
                 keywords: ('list', 'tuple', 'set') = None):

        self._id = id
        self._question = question
        self._answer = answer
        if keywords is None:
            self._keywords = self.extract_keywords(answer)
        else:
            self._keywords = list(keywords)

    def __str__(self):
        return self._question

    def __repr__(self):
        return f'QuestionAnswer("{self._question}", "{self._answer}", "{self._keywords}")'

    @property
    def id(self):
        return self._id

    @property
    def question(self):
        return self._question

    @property
    def answer(self):
        return self._answer

    @property
    def keywords(self):
        return self._keywords

    @staticmethod
    def extract_keywords(text: str, minimal_word_length: int = 3):
        """Extract valid keywords from the input string"""
        WORDS_TO_IGNORE = {'de', 'het', 'een','en', 'met', 'is', 'je', 'door'}
        text = text.lower().translate(str.maketrans('', '', string.punctuation))
        words = {word for word in text.split() if len(word) >= minimal_word_length}
        words -= WORDS_TO_IGNORE
        return list(words)

    def compare_to_keyword(self, word, min_ratio = 0.7, keywords = None):
        if keywords is None:
            keywords = self._keywords
        for keyword in keywords:
            r = difflib.SequenceMatcher(None, word, keyword).ratio()
            if r > min_ratio:
                return keyword

    @staticmethod
    def rating(common_keywords, total_keywords):
        """A rating between 0 and 10"""
        return round(10 * common_keywords / total_keywords)

    def rate_response(self, response: str):
        """Compare words in input with keywords and return the corresponding rating"""
        response_keywords = self.extract_keywords(response)

        total_keywords = len(self._keywords)
        common_keywords = len(response_keywords & set(self._keywords))

        return self.rating(common_keywords, total_keywords)



# -----------------------------------------------------------

if __name__ == '__main__':

    qa = QuestionAnswer(id = 0,
                        question = 'Welke kleuren heeft de Nederlandse vlag?????',
                        answer = 'Rood, wit en blauw')

    print(repr(qa))

    response = input(qa)

    rating = qa.rate_response(response)

    print(rating)
