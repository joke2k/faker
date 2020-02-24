from ..en_US import Provider as EnUsProvider
from ..la import Provider as LoremProvider


class Provider(LoremProvider):
    """Provider for generating English or Latin lorem content"""

    english_word_list = EnUsProvider.word_list

    def english_word(self):
        return self.word(self.english_word_list)

    def english_words(self, nb=3, unique=False):
        return self.words(nb, self.english_word_list, unique)

    def english_sentence(self, nb_words=6, variable_nb_words=True):
        return self.sentence(nb_words, variable_nb_words, self.english_word_list)

    def english_sentences(self, nb=3):
        return self.sentences(nb, self.english_word_list)

    def english_paragraph(self, nb_sentences=3, variable_nb_sentences=True):
        return self.paragraph(nb_sentences, variable_nb_sentences, self.english_word_list)

    def english_paragraphs(self, nb=3):
        return self.paragraphs(nb, self.english_word_list)

    def english_text(self, max_nb_chars=200):
        return self.text(max_nb_chars, self.english_word_list)

    def english_texts(self, nb_texts=3, max_nb_chars=200):
        return self.texts(nb_texts, max_nb_chars, self.english_word_list)
