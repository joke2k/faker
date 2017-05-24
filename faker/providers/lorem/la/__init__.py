# coding=utf-8

from __future__ import unicode_literals
from .. import Provider as LoremProvider


class Provider(LoremProvider):

    def __init__(self, ext_word_list=None):
        #verify the type of the variable
        self.word_list = words
        if isanstance(ext_word_list, None):
            return self.word_list
        elif isinstance(ext_word_list, list) or isinstance(ext_word_list, tuple):
            return self.word_list = ext_word_list
        #difficulty how the user will choose ??? have a class variable or __init__

    words = (
        'a', 'ab', 'accusamus', 'accusantium', 'ad', 'adipisci', 'alias',
        'aliquam', 'aliquid', 'amet', 'animi', 'aperiam', 'architecto',
        'asperiores', 'aspernatur', 'assumenda', 'at', 'atque', 'aut', 'autem',
        'beatae', 'blanditiis', 'commodi', 'consectetur', 'consequatur',
        'consequuntur', 'corporis', 'corrupti', 'culpa', 'cum', 'cumque',
        'cupiditate', 'debitis', 'delectus', 'deleniti', 'deserunt', 'dicta',
        'dignissimos', 'distinctio', 'dolor', 'dolore', 'dolorem', 'doloremque',
        'dolores', 'doloribus', 'dolorum', 'ducimus', 'ea', 'eaque', 'earum',
        'eius', 'eligendi', 'enim', 'eos', 'error', 'esse', 'est', 'et', 'eum',
        'eveniet', 'ex', 'excepturi', 'exercitationem', 'expedita', 'explicabo',
        'facere', 'facilis', 'fuga', 'fugiat', 'fugit', 'harum', 'hic', 'id',
        'illo', 'illum', 'impedit', 'in', 'incidunt', 'inventore', 'ipsa',
        'ipsam', 'ipsum', 'iste', 'itaque', 'iure', 'iusto', 'labore',
        'laboriosam', 'laborum', 'laudantium', 'libero', 'magnam', 'magni',
        'maiores', 'maxime', 'minima', 'minus', 'modi', 'molestiae',
        'molestias', 'mollitia', 'nam', 'natus', 'necessitatibus', 'nemo',
        'neque', 'nesciunt', 'nihil', 'nisi', 'nobis', 'non', 'nostrum',
        'nulla', 'numquam', 'occaecati', 'odio', 'odit', 'officia', 'officiis',
        'omnis', 'optio', 'pariatur', 'perferendis', 'perspiciatis', 'placeat',
        'porro', 'possimus', 'praesentium', 'provident', 'quae', 'quaerat',
        'quam', 'quas', 'quasi', 'qui', 'quia', 'quibusdam', 'quidem', 'quis',
        'quisquam', 'quo', 'quod', 'quos', 'ratione', 'recusandae',
        'reiciendis', 'rem', 'repellat', 'repellendus', 'reprehenderit',
        'repudiandae', 'rerum', 'saepe', 'sapiente', 'sed', 'sequi',
        'similique', 'sint', 'sit', 'soluta', 'sunt', 'suscipit', 'tempora',
        'tempore', 'temporibus', 'tenetur', 'totam', 'ullam', 'unde', 'ut',
        'vel', 'velit', 'veniam', 'veritatis', 'vero', 'vitae', 'voluptas',
        'voluptate', 'voluptatem', 'voluptates', 'voluptatibus', 'voluptatum'
    )
