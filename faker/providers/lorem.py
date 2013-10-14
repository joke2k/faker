import random
from . import BaseProvider



class Provider(BaseProvider):

    wordList = (
        'alias', 'consequatur', 'aut', 'perferendis', 'sit', 'voluptatem',
        'accusantium', 'doloremque', 'aperiam', 'eaque','ipsa', 'quae', 'ab',
        'illo', 'inventore', 'veritatis', 'et', 'quasi', 'architecto',
        'beatae', 'vitae', 'dicta', 'sunt', 'explicabo', 'aspernatur', 'aut',
        'odit', 'aut', 'fugit', 'sed', 'quia', 'consequuntur', 'magni',
        'dolores', 'eos', 'qui', 'ratione', 'voluptatem', 'sequi', 'nesciunt',
        'neque', 'dolorem', 'ipsum', 'quia', 'dolor', 'sit', 'amet',
        'consectetur', 'adipisci', 'velit', 'sed', 'quia', 'non', 'numquam',
        'eius', 'modi', 'tempora', 'incidunt', 'ut', 'labore', 'et', 'dolore',
        'magnam', 'aliquam', 'quaerat', 'voluptatem', 'ut', 'enim', 'ad',
        'minima', 'veniam', 'quis', 'nostrum', 'exercitationem', 'ullam',
        'corporis', 'nemo', 'enim', 'ipsam', 'voluptatem', 'quia', 'voluptas',
        'sit', 'suscipit', 'laboriosam', 'nisi', 'ut', 'aliquid', 'ex', 'ea',
        'commodi', 'consequatur', 'quis', 'autem', 'vel', 'eum', 'iure',
        'reprehenderit', 'qui', 'in', 'ea', 'voluptate', 'velit', 'esse',
        'quam', 'nihil', 'molestiae', 'et', 'iusto', 'odio', 'dignissimos',
        'ducimus', 'qui', 'blanditiis', 'praesentium', 'laudantium', 'totam',
        'rem', 'voluptatum', 'deleniti', 'atque', 'corrupti', 'quos',
        'dolores', 'et', 'quas', 'molestias', 'excepturi', 'sint',
        'occaecati', 'cupiditate', 'non', 'provident', 'sed', 'ut',
        'perspiciatis', 'unde', 'omnis', 'iste', 'natus', 'error',
        'similique', 'sunt', 'in', 'culpa', 'qui', 'officia', 'deserunt',
        'mollitia', 'animi', 'id', 'est', 'laborum', 'et', 'dolorum', 'fuga',
        'et', 'harum', 'quidem', 'rerum', 'facilis', 'est', 'et', 'expedita',
        'distinctio', 'nam', 'libero', 'tempore', 'cum', 'soluta', 'nobis',
        'est', 'eligendi', 'optio', 'cumque', 'nihil', 'impedit', 'quo',
        'porro', 'quisquam', 'est', 'qui', 'minus', 'id', 'quod', 'maxime',
        'placeat', 'facere', 'possimus', 'omnis', 'voluptas', 'assumenda',
        'est', 'omnis', 'dolor', 'repellendus', 'temporibus', 'autem',
        'quibusdam', 'et', 'aut', 'consequatur', 'vel', 'illum', 'qui',
        'dolorem', 'eum', 'fugiat', 'quo', 'voluptas', 'nulla', 'pariatur',
        'at', 'vero', 'eos', 'et', 'accusamus', 'officiis', 'debitis', 'aut',
        'rerum', 'necessitatibus', 'saepe', 'eveniet', 'ut', 'et',
        'voluptates', 'repudiandae', 'sint', 'et', 'molestiae', 'non',
        'recusandae', 'itaque', 'earum', 'rerum', 'hic', 'tenetur', 'a',
        'sapiente', 'delectus', 'ut', 'aut', 'reiciendis', 'voluptatibus',
        'maiores', 'doloribus', 'asperiores', 'repellat'
    )

    @classmethod
    def word(cls):
        """
        :example 'Lorem'
        """
        return cls.randomElement( cls.wordList )

    @classmethod
    def words(cls, nb=3):
        """
        Generate an array of random words
        :example array('Lorem', 'ipsum', 'dolor')
        :param integer $nb how many words to return
        """
        return [cls.word() for x in range(0, nb)]

    @classmethod
    def sentence(cls, nbWords=6, variableNbWords=True ):
        """
        Generate a random sentence
        :example 'Lorem ipsum dolor sit amet.'
        :param integer $nbWords around how many words the sentence should contain
        :param boolean $variableNbWords set to false if you want exactly $nbWords returned,
            otherwise $nbWords may vary by +/-40% with a minimum of 1
        """
        if nbWords <= 0:
            return ''

        if variableNbWords:
            nbWords = cls.randomizeNbElements( nbWords )

        words = cls.words( nbWords )
        words[0] = words[0].title()

        return " ".join( words ) + '.'

    @classmethod
    def sentences(cls, nb=3 ):
        """
        Generate an array of sentences
        :example array('Lorem ipsum dolor sit amet.', 'Consectetur adipisicing eli.')
        :param integer $nb how many sentences to return
        :return array
        """
        return [cls.sentence() for x in range(0, nb)]

    @classmethod
    def paragraph(cls, nbSentences=3, variablenbSentences=True ):
        """
        Generate a single paragraph
        :example 'Sapiente sunt omnis. Ut pariatur ad autem ducimus et. Voluptas rem voluptas sint modi dolorem amet.'
        :param integer $nbSentences around how many sentences the paragraph should contain
        :param boolean $variableNbSentences set to false if you want exactly $nbSentences returned,
            otherwise $nbSentences may vary by +/-40% with a minimum of 1
        :return string
        """
        if nbSentences <= 0 :
            return ''

        if variablenbSentences:
            nbSentences = cls.randomizeNbElements( nbSentences )

        return " ".join( cls.sentences(nbSentences) )

    @classmethod
    def paragraphs(cls, nb=3 ):
        """
        Generate an array of paragraphs
        :example array($paragraph1, $paragraph2, $paragraph3)
        :param integer $nb how many paragraphs to return
        :return array
        """
        return [cls.paragraph() for x in range(0, nb)]

    @classmethod
    def text(cls, maxNbChars=200 ):
        """
        Generate a text string.
        Depending on the $maxNbChars, returns a string made of words, sentences, or paragraphs.
        :example 'Sapiente sunt omnis. Ut pariatur ad autem ducimus et. Voluptas rem voluptas sint modi dolorem amet.'
        :param integer $maxNbChars Maximum number of characters the text should contain (minimum 5)
        :return string
        """
        text = []
        if maxNbChars < 5:
            raise ValueError('text() can only generate text of at least 5 characters')

        if maxNbChars < 25:
            # join words
            while not text:
                size = 0
                # determine how many words are needed to reach the $maxNbChars once;
                while size < maxNbChars:
                    word = (' ' if size else '') + cls.word()
                    text.append( word )
                    size += len(word)
                text.pop()
            text[0] = text[0][0].upper() + text[0][1:]
            last_index = len(text)-1
            text[ last_index ] = text[ last_index ] + '.'
        elif maxNbChars < 100 :
            # join sentences
            while not text:
                size = 0
                # determine how many sentences are needed to reach the $maxNbChars once
                while size < maxNbChars:
                    sentence = (' ' if size else '') + cls.sentence()
                    text.append( sentence )
                    size += len(sentence)
                text.pop()
        else:
            # join paragraphs
            while not text:
                size = 0
                # determine how many paragraphs are needed to reach the $maxNbChars once
                while ( size < maxNbChars ):
                    paragraph = ('\n' if size else '') + cls.paragraph()
                    text.append( paragraph )
                    size += len(paragraph)
                text.pop()

        return "".join(text)
