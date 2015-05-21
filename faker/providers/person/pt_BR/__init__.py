# coding=utf-8
from __future__ import unicode_literals
from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats = (
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{prefix}} {{last_name}}',
        '{{first_name}} {{last_name}} {{last_name}}',
        '{{first_name}} {{first_name}} {{last_name}}',
    )

    first_names = (
        'Sofia', 'Julia', 'Isabella', 'Alice', 'Manuela', 'Maria Eduarda', 'Giovanna', 'Laura', 'Luiza', 'Beatriz',
        'Mariana',
        'Ana Clara', 'Maria Clara', 'Maria Luiza', 'Yasmin', 'Rafaela', 'Gabriela', 'Isabelly', 'Ana Julia',
        'Valentina',
        'Letícia', 'Lara', 'Ana Luiza', 'Lorena', 'Helena', 'Nicole', 'Isadora', 'Lívia', 'Sarah', 'Marina',
        'Ana Beatriz',
        'Melissa', 'Heloísa', 'Vitória', 'Cecília', 'Emanuelly', 'Lavínia', 'Maria Fernanda', 'Amanda', 'Gabrielly',
        'Larissa', 'Bianca', 'Esther', 'Clara', 'Rebeca', 'Eduarda', 'Alícia', 'Carolina', 'Emilly', 'Maria Julia',
        'Fernanda',
        'Pietra', 'Milena', 'Ana Laura', 'Catarina', 'Maria Alice', 'Ana Carolina', 'Agatha', 'Natália', 'Laís',
        'Elisa',
        'Camila', 'Maria Vitória', 'Luana', 'Olivia', 'Mirella', 'Maria', 'Maria Cecília', 'Marcela', 'Ana Sophia',
        'Kamilly', 'Joana', 'Eloah', 'Stella', 'Sophie', 'Maria Sophia', 'Bruna', 'Juliana', 'Bárbara', 'Maitê',
        'Clarice',
        'Ana Vitória', 'Caroline', 'Ana', 'Ana Lívia', 'Evelyn', 'Luna', 'Stephany', 'Isabel', 'Alexia', 'Mariane',
        'Brenda',
        'Alana', 'Maysa', 'Raquel', 'Nina', 'Sabrina', 'Emanuella', 'Daniela', 'Miguel', 'Arthur', 'Davi', 'Gabriel',
        'Lucas', 'Matheus', 'Pedro', 'Guilherme', 'Enzo', 'Rafael', 'Bernardo', 'Gustavo', 'Nicolas', 'Felipe',
        'Pedro Henrique',
        'João Pedro', 'Henrique', 'Samuel', 'Cauã', 'Eduardo', 'Vitor', 'Heitor', 'Murilo', 'Daniel', 'Pietro',
        'João Vitor',
        'Vinicius', 'Leonardo', 'Caio', 'Lorenzo', 'Thiago', 'Lucca', 'Isaac', 'Theo', 'Enzo Gabriel', 'João',
        'João Gabriel',
        'Emanuel', 'Yuri', 'Bryan', 'Luiz Felipe', 'Ryan', 'Joaquim', 'Antonio', 'Carlos Eduardo', 'Bruno',
        'Davi Lucas',
        'João Guilherme', 'Erick', 'Calebe', 'Benjamin', 'Vitor Hugo', 'Rodrigo', 'Ian', 'Fernando', 'Otávio', 'Breno',
        'Igor', 'Francisco', 'Thomas', 'André', 'Juan', 'Luiz Gustavo', 'Augusto', 'Kaique', 'Nathan', 'João Miguel',
        'João Lucas',
        'Pedro Lucas', 'Raul', 'Luiz Miguel', 'Cauê', 'Luiz Henrique', 'Benício', 'Anthony', 'Vitor Gabriel', 'Yago',
        'Marcelo', 'Luiz Otávio', 'Renan', 'Alexandre', 'Levi', 'Danilo', 'Thales', 'Lucas Gabriel', 'Diogo',
        'Davi Lucca',
        'Paulo', 'Enrico', 'Diego', 'Vicente', 'Marcos Vinicius', 'Luiz Fernando', 'Pedro Miguel', 'Gustavo Henrique',
        'Leandro',
        'Noah', 'Kevin', 'João Felipe', 'Luigi',

    )

    last_names = (
        'Silva', 'Santos', 'Oliveira', 'Souza', 'Pereira', 'Costela', 'Carvalho', 'Almeida', 'Ferreira', 'Ribeiro',
        'Rodrigues',
        'Gomes', 'Lima', 'Martins', 'Rocha', 'Alves', 'Araújo', 'Pinto', 'Barbosa', 'Castro', 'Fernandes', 'Melo',
        'Azevedo',
        'Barros', 'Cardoso', 'Correia', 'Cunha', 'Dias'
    )

    prefixes = ('de', 'da', 'do')

    @classmethod
    def prefix(cls):
        return cls.random_element(cls.prefixes)
