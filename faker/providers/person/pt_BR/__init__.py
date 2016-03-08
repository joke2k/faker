# coding=utf-8
from __future__ import unicode_literals
from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats_female = (
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{prefix_female}} {{first_name_female}} {{last_name}}'
    )

    formats_male = (
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{prefix_male}} {{first_name_male}} {{last_name}}'

    )

    formats = formats_male + formats_female

    first_names_female = (
        'Agatha', 'Alana', 'Alexia', 'Alice', 'Alícia', 'Amanda',
        'Ana Beatriz', 'Ana Carolina', 'Ana Clara', 'Ana Julia', 'Ana Laura',
        'Ana Luiza', 'Ana Lívia', 'Ana Sophia', 'Ana Vitória', 'Ana',
        'Beatriz', 'Bianca', 'Brenda', 'Bruna', 'Bárbara', 'Camila',
        'Carolina', 'Caroline', 'Catarina', 'Cecília', 'Clara', 'Clarice',
        'Daniela', 'Eduarda', 'Elisa', 'Fernanda', 'Eloah', 'Emanuella',
        'Emanuelly', 'Emilly', 'Esther', 'Evelyn', 'Gabriela', 'Gabrielly',
        'Giovanna', 'Helena', 'Heloísa', 'Isabel', 'Isabella', 'Isabelly',
        'Isadora', 'Joana', 'Julia', 'Juliana', 'Kamilly', 'Lara', 'Larissa',
        'Laura', 'Lavínia', 'Laís', 'Letícia', 'Lorena', 'Luana', 'Luiza',
        'Luna', 'Lívia', 'Maitê', 'Manuela', 'Marcela', 'Maria Alice',
        'Maria Cecília', 'Maria Clara', 'Maria Eduarda', 'Maria Fernanda',
        'Maria Julia', 'Maria Luiza', 'Maria Sophia', 'Maria Vitória',
        'Maria', 'Mariana', 'Mariane', 'Marina', 'Maysa', 'Melissa', 'Milena',
        'Mirella', 'Natália', 'Nicole', 'Nina', 'Olivia', 'Pietra', 'Rafaela',
        'Raquel', 'Rebeca', 'Sabrina', 'Sarah', 'Sofia', 'Sophie', 'Stella',
        'Stephany', 'Valentina', 'Vitória', 'Yasmin'
    )

    first_names_male = (
        'Alexandre', 'André', 'Anthony', 'Antonio', 'Arthur', 'Augusto',
        'Benjamin', 'Benício', 'Bernardo', 'Breno', 'Bruno', 'Bryan', 'Caio',
        'Calebe', 'Carlos Eduardo', 'Cauã', 'Cauê', 'Daniel', 'Danilo',
        'Davi Lucas', 'Davi Lucca', 'Davi', 'Diego', 'Diogo', 'Eduardo',
        'Emanuel', 'Enrico', 'Enzo Gabriel', 'Enzo', 'Erick', 'Felipe',
        'Fernando', 'Francisco', 'Gabriel', 'Guilherme', 'Gustavo Henrique',
        'Gustavo', 'Heitor', 'Henrique', 'Ian', 'Igor', 'Isaac', 'Joaquim',
        'João Felipe', 'João Gabriel', 'João Guilherme', 'João Lucas',
        'João Miguel', 'João Pedro', 'João Vitor', 'João', 'Juan', 'Kaique',
        'Kevin', 'Leandro', 'Leonardo', 'Levi', 'Lorenzo', 'Lucas Gabriel',
        'Lucas', 'Lucca', 'Luigi', 'Luiz Felipe', 'Luiz Fernando',
        'Luiz Gustavo', 'Luiz Henrique', 'Luiz Miguel', 'Luiz Otávio',
        'Marcelo', 'Marcos Vinicius', 'Matheus', 'Miguel', 'Murilo', 'Nathan',
        'Nicolas', 'Noah', 'Otávio', 'Paulo', 'Pedro Henrique', 'Pedro Lucas',
        'Pedro Miguel', 'Pedro', 'Pietro', 'Rafael', 'Raul', 'Renan',
        'Rodrigo', 'Ryan', 'Samuel', 'Thales', 'Theo', 'Thiago', 'Thomas',
        'Vicente', 'Vinicius', 'Vitor Gabriel', 'Vitor Hugo', 'Vitor', 'Yago',
        'Yuri'
    )

    first_names = first_names_male + first_names_female

    last_names = (
        'Almeida', 'Alves', 'Araújo', 'Azevedo', 'Barbosa', 'Barros',
        'Cardoso', 'Carvalho', 'Castro', 'Correia', 'Costela', 'Cunha', 'Dias',
        'Fernandes', 'Ferreira', 'Gomes', 'Lima', 'Martins', 'Melo',
        'Oliveira', 'Pereira', 'Pinto', 'Ribeiro', 'Rocha', 'Rodrigues',
        'Santos', 'Silva', 'Souza'
    )

    prefixes_female = ('Srta.', 'Sra.', 'Dra.')
    prefixes_male = ('Sr.', 'Dr.')
