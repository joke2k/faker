localized = True
default_locale = 'la'

from .. import BaseProvider
import re


class Provider(BaseProvider):
    @classmethod
    def word(cls):
        """
        Generate a random word
        :example 'lorem'
        """
        return cls.random_element(cls.word_list)

    @classmethod
    def words(cls, nb=3):
        """
        Generate an array of random words
        :example array('Lorem', 'ipsum', 'dolor')
        :param nb how many words to return
        """
        return [cls.word() for _ in range(0, nb)]

    @classmethod
    def sentence(cls, nb_words=6, variable_nb_words=True):
        """
        Generate a random sentence
        :example 'Lorem ipsum dolor sit amet.'
        :param nb_words around how many words the sentence should contain
        :param variable_nb_words set to false if you want exactly $nbWords returned,
            otherwise $nbWords may vary by +/-40% with a minimum of 1
        """
        if nb_words <= 0:
            return ''

        if variable_nb_words:
            nb_words = cls.randomize_nb_elements(nb_words)

        words = cls.words(nb_words)
        words[0] = words[0].title()

        return " ".join(words) + '.'

    @classmethod
    def sentences(cls, nb=3):
        """
        Generate an array of sentences
        :example array('Lorem ipsum dolor sit amet.', 'Consectetur adipisicing eli.')
        :param nb how many sentences to return
        :return list
        """
        return [cls.sentence() for _ in range(0, nb)]

    @classmethod
    def paragraph(cls, nb_sentences=3, variable_nb_sentences=True):
        """
        Generate a single paragraph
        :example 'Sapiente sunt omnis. Ut pariatur ad autem ducimus et. Voluptas rem voluptas sint modi dolorem amet.'
        :param nb_sentences around how many sentences the paragraph should contain
        :param variable_nb_sentences set to false if you want exactly $nbSentences returned,
            otherwise $nbSentences may vary by +/-40% with a minimum of 1
        :return string
        """
        if nb_sentences <= 0:
            return ''

        if variable_nb_sentences:
            nb_sentences = cls.randomize_nb_elements(nb_sentences)

        return " ".join(cls.sentences(nb_sentences))

    @classmethod
    def paragraphs(cls, nb=3):
        """
        Generate an array of paragraphs
        :example array($paragraph1, $paragraph2, $paragraph3)
        :param nb how many paragraphs to return
        :return array
        """
        return [cls.paragraph() for _ in range(0, nb)]

    @classmethod
    def text(cls, min_nb_chars=5, max_nb_chars=200):
        """
        Generate a text string.
        Depending on the $maxNbChars, returns a string made of words, sentences, or paragraphs.
        :example 'Sapiente sunt omnis. Ut pariatur ad autem ducimus et. Voluptas rem voluptas sint modi dolorem amet.'
        :param max_nb_chars Maximum number of characters the text should contain (inclusive; default=200)
        :param min_nb_chars Minimum number of characters the text should contain (inclusive; default=0; minimum 5)
        :return string
        """
        text = []
        if max_nb_chars < min_nb_chars:
            raise ValueError('minimum length cannot exceed maximum length')
        if min_nb_chars < 5:
            raise ValueError('text() can only generate text of at least 5 characters')
        text_len = cls.random_int(min=min_nb_chars, max=max_nb_chars)
        size = 0

        if text_len < 25:
            # join words
            while not text:
                # determine how many words are needed to reach the $max_nb_chars once;
                while text_len > size:
                    word = (' ' if size else '') + cls.word()
                    text.append(word)
                    size += len(word)
            text[0] = text[0][0].upper() + text[0][1:]
            last_index = len(text) - 1
            text[last_index] += '.'
            size += 1
        elif text_len < 100:
            # join sentences
            while not text:
                # determine how many sentences are needed to reach the $max_nb_chars once
                while text_len > size:
                    sentence = (' ' if size else '') + cls.sentence()
                    text.append(sentence)
                    size += len(sentence)
        else:
            # join paragraphs
            while not text:
                # determine how many paragraphs are needed to reach the $max_nb_chars once
                while text_len > size:
                    paragraph = ('\n' if size else '') + cls.paragraph()
                    text.append(paragraph)
                    size += len(paragraph)

        if size > max_nb_chars:
            if size - len(text[-1]) > min_nb_chars:
                text.pop()
                string = "".join(text)
            else:
                string = "".join(text)[0:text_len - 1]
                # handle situations when the sliced text would end with ' ', '.', or other unnature ways
                str2replace_len = 0
                if re.findall(r'\.\s[A-Z][a-z]*[\.]*[\s]*$', string):
                    str2replace_len = len(re.findall(r'\.\s[A-Z][a-z]*[\.]*[\s]*$', string)[0])
                elif string[-1] == ' ':
                    if string[-2].islower():
                        str2replace_len = 1
                    elif string[-2].isupper():
                        str2replace_len = 4
                    elif string[-2] == '.':
                        str2replace_len = 2
                elif string[-1] == '.':
                    str2replace_len = 1
                if str2replace_len > 0:
                    word_stitch = cls.word()
                    while len(word_stitch) < str2replace_len:
                        word_stitch += cls.word()
                    string = string[:-str2replace_len] + word_stitch[:str2replace_len] + '.'
        else:
            string = "".join(text)

        if string[-1] != '.':
            string += '.'

        return string
