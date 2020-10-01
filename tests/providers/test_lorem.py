import re

import pytest


class TestLoremProvider:
    """Test lorem provider methods"""
    custom_word_list = [
        'danish', 'cheesecake', 'sugar', 'lollipop',
        'wafer', 'gummies', 'jelly', 'pie',
    ]

    def test_word_with_defaults(self, faker, num_samples):
        for _ in range(num_samples):
            word = faker.word()
            assert isinstance(word, str)

    def test_word_with_custom_list(self, faker, num_samples):
        for _ in range(num_samples):
            word = faker.word(ext_word_list=self.custom_word_list)
            assert isinstance(word, str)
            assert word in self.custom_word_list

    def test_words_with_zero_nb(self, faker, num_samples):
        for _ in range(num_samples):
            assert faker.words(0) == []

    def test_words_with_defaults(self, faker, num_samples):
        num_words = 5
        for _ in range(num_samples):
            words = faker.words(num_words)
            assert isinstance(words, list)
            assert len(words) == 5
            assert all(isinstance(word, str) for word in words)

    def test_words_with_custom_word_list(self, faker, num_samples):
        num_words = 5
        for _ in range(num_samples):
            words = faker.words(num_words, ext_word_list=self.custom_word_list)
            assert isinstance(words, list)
            assert len(words) == 5
            assert all(isinstance(word, str) and word in self.custom_word_list for word in words)

    def test_words_with_unique_sampling(self, faker, num_samples):
        num_words = 5
        for _ in range(num_samples):
            words = faker.words(num_words, ext_word_list=self.custom_word_list, unique=True)
            assert isinstance(words, list)
            assert len(words) == 5

            checked_words = []
            for word in words:
                assert isinstance(word, str)
                assert word in self.custom_word_list
                assert word not in checked_words
                checked_words.append(word)

    def test_sentence_no_words(self, faker, num_samples):
        for _ in range(num_samples):
            assert faker.sentence(0) == ''

    def test_sentence_with_inexact_word_count(self, faker, num_samples):
        num_words = 10
        for _ in range(num_samples):
            sentence = faker.sentence(nb_words=num_words)
            words = sentence.lower().replace('.', '').split()
            assert int(num_words * 0.6) <= len(words) <= int(num_words * 1.4)

    def test_sentence_with_exact_word_count(self, faker, num_samples):
        num_words = 10
        for _ in range(num_samples):
            sentence = faker.sentence(nb_words=num_words, variable_nb_words=False)
            words = sentence.lower().replace('.', '').split()
            assert len(words) == num_words

    def test_sentence_with_custom_word_list(self, faker, num_samples):
        for _ in range(num_samples):
            sentence = faker.sentence(ext_word_list=self.custom_word_list)
            words = sentence.lower().replace('.', '').split()
            assert all(isinstance(word, str) and word in self.custom_word_list for word in words)

    def test_sentences(self, faker, num_samples):
        num_sentences = 5
        for _ in range(num_samples):
            sentences = faker.sentences(nb=num_sentences, ext_word_list=self.custom_word_list)
            assert len(sentences) == num_sentences
            for sentence in sentences:
                words = sentence.lower().replace('.', '').split()
                assert all(isinstance(word, str) and word in self.custom_word_list for word in words)

    def test_paragraph_no_sentences(self, faker, num_samples):
        for _ in range(num_samples):
            assert faker.paragraph(0) == ''

    def test_paragraph_with_inexact_sentence_count(self, faker, num_samples):
        num_sentences = 10
        for _ in range(num_samples):
            paragraph = faker.paragraph(nb_sentences=num_sentences)
            sentences = paragraph.split('. ')
            assert int(num_sentences * 0.6) <= len(sentences) <= int(num_sentences * 1.4)

    def test_paragraph_with_exact_sentence_count(self, faker, num_samples):
        num_sentences = 10
        for _ in range(num_samples):
            paragraph = faker.paragraph(nb_sentences=num_sentences, variable_nb_sentences=False)
            sentences = paragraph.split('. ')
            assert len(sentences) == num_sentences

    def test_paragraph_with_custom_word_list(self, faker, num_samples):
        for _ in range(num_samples):
            paragraph = faker.paragraph(ext_word_list=self.custom_word_list)
            words = paragraph.lower().replace('.', '').split()
            assert all(isinstance(word, str) and word in self.custom_word_list for word in words)

    def test_paragraphs(self, faker, num_samples):
        num_paragraphs = 5
        for _ in range(num_samples):
            paragraphs = faker.paragraphs(nb=num_paragraphs, ext_word_list=self.custom_word_list)
            assert len(paragraphs) == num_paragraphs
            for paragraph in paragraphs:
                words = paragraph.lower().replace('.', '').split()
                assert all(isinstance(word, str) and word in self.custom_word_list for word in words)

    def test_text_with_less_than_four_characters(self, faker, num_samples):
        for _ in range(num_samples):
            with pytest.raises(ValueError):
                faker.text(max_nb_chars=4)

    @pytest.mark.parametrize('num_chars', [10, 50, 150, 10000], ids=[
        'max_nb_chars < 25',
        '25 <= max_nb_chars < 100',
        'max_nb_chars >= 100',
        'max_nb_chars >> 100',
    ])
    def test_text_with_valid_character_count(self, faker, num_samples, num_chars):
        for _ in range(num_samples):
            text = faker.text(max_nb_chars=num_chars)
            assert len(text) <= num_chars

    def test_text_with_custom_word_list(self, faker, num_samples):
        for _ in range(num_samples):
            text = faker.text(ext_word_list=self.custom_word_list)
            words = re.sub(r'[.\n]+', ' ', text.lower()).split()
            assert all(word in self.custom_word_list for word in words)

    def test_texts(self, faker, num_samples):
        num_texts = 5
        num_chars = 25
        for _ in range(num_samples):
            texts = faker.texts(
                max_nb_chars=num_chars, nb_texts=num_texts,
                ext_word_list=self.custom_word_list,
            )
            assert len(texts) == num_texts
            for text in texts:
                assert len(text) <= num_chars
                words = re.sub(r'[.\n]+', ' ', text.lower()).split()
                assert all(word in self.custom_word_list for word in words)
