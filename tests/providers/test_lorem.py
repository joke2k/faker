import re

import pytest

from faker.providers.lorem.az_AZ import Provider as AzAzLoremProvider
from faker.providers.lorem.bn_BD import Provider as BnBdLoremProvider
from faker.providers.lorem.cs_CZ import Provider as CsCzLoremProvider
from faker.providers.lorem.de_AT import Provider as DeAtLoremProvider
from faker.providers.lorem.de_DE import Provider as DeDeLoremProvider
from faker.providers.lorem.en_US import Provider as EnUsLoremProvider
from faker.providers.lorem.fa_IR import Provider as FaIrLoremProvider
from faker.providers.lorem.it_IT import Provider as ItItLoremProvider
from faker.providers.lorem.nl_BE import Provider as NlBeLoremProvider
from faker.providers.lorem.uk_UA import Provider as UkUaLoremProvider
from faker.providers.lorem.vi_VN import Provider as ViVNLoremProvider


class TestLoremProvider:
    """Test lorem provider methods"""

    custom_word_list = ["danish", "cheesecake", "sugar", "lollipop", "wafer", "gummies", "jelly", "pie"]

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
            assert faker.sentence(0) == ""

    def test_sentence_with_inexact_word_count(self, faker, num_samples):
        num_words = 10
        for _ in range(num_samples):
            sentence = faker.sentence(nb_words=num_words)
            words = sentence.lower().replace(".", "").split()
            assert int(num_words * 0.6) <= len(words) <= int(num_words * 1.4)

    def test_sentence_with_exact_word_count(self, faker, num_samples):
        num_words = 10
        for _ in range(num_samples):
            sentence = faker.sentence(nb_words=num_words, variable_nb_words=False)
            words = sentence.lower().replace(".", "").split()
            assert len(words) == num_words

    def test_sentence_with_custom_word_list(self, faker, num_samples):
        for _ in range(num_samples):
            sentence = faker.sentence(ext_word_list=self.custom_word_list)
            words = sentence.lower().replace(".", "").split()
            assert all(isinstance(word, str) and word in self.custom_word_list for word in words)

    def test_sentences(self, faker, num_samples):
        num_sentences = 5
        for _ in range(num_samples):
            sentences = faker.sentences(nb=num_sentences, ext_word_list=self.custom_word_list)
            assert len(sentences) == num_sentences
            for sentence in sentences:
                words = sentence.lower().replace(".", "").split()
                assert all(isinstance(word, str) and word in self.custom_word_list for word in words)

    def test_sentence_single_word(self, faker):
        word = faker.sentence(1)
        assert str.isupper(word[0])

    def test_paragraph_no_sentences(self, faker, num_samples):
        for _ in range(num_samples):
            assert faker.paragraph(0) == ""

    def test_paragraph_with_inexact_sentence_count(self, faker, num_samples):
        num_sentences = 10
        for _ in range(num_samples):
            paragraph = faker.paragraph(nb_sentences=num_sentences)
            sentences = paragraph.split(". ")
            assert int(num_sentences * 0.6) <= len(sentences) <= int(num_sentences * 1.4)

    def test_paragraph_with_exact_sentence_count(self, faker, num_samples):
        num_sentences = 10
        for _ in range(num_samples):
            paragraph = faker.paragraph(nb_sentences=num_sentences, variable_nb_sentences=False)
            sentences = paragraph.split(". ")
            assert len(sentences) == num_sentences

    def test_paragraph_with_custom_word_list(self, faker, num_samples):
        for _ in range(num_samples):
            paragraph = faker.paragraph(ext_word_list=self.custom_word_list)
            words = paragraph.lower().replace(".", "").split()
            assert all(isinstance(word, str) and word in self.custom_word_list for word in words)

    def test_paragraphs(self, faker, num_samples):
        num_paragraphs = 5
        for _ in range(num_samples):
            paragraphs = faker.paragraphs(nb=num_paragraphs, ext_word_list=self.custom_word_list)
            assert len(paragraphs) == num_paragraphs
            for paragraph in paragraphs:
                words = paragraph.lower().replace(".", "").split()
                assert all(isinstance(word, str) and word in self.custom_word_list for word in words)

    def test_text_with_less_than_four_characters(self, faker, num_samples):
        for _ in range(num_samples):
            with pytest.raises(ValueError):
                faker.text(max_nb_chars=4)

    @pytest.mark.parametrize(
        "num_chars",
        [10, 50, 150, 10000],
        ids=["max_nb_chars < 25", "25 <= max_nb_chars < 100", "max_nb_chars >= 100", "max_nb_chars >> 100"],
    )
    def test_text_with_valid_character_count(self, faker, num_samples, num_chars):
        for _ in range(num_samples):
            text = faker.text(max_nb_chars=num_chars)
            assert len(text) <= num_chars

    def test_text_with_custom_word_list(self, faker, num_samples):
        for _ in range(num_samples):
            text = faker.text(ext_word_list=self.custom_word_list)
            words = re.sub(r"[.\n]+", " ", text.lower()).split()
            assert all(word in self.custom_word_list for word in words)

    def test_texts(self, faker, num_samples):
        num_texts = 5
        num_chars = 25
        for _ in range(num_samples):
            texts = faker.texts(max_nb_chars=num_chars, nb_texts=num_texts, ext_word_list=self.custom_word_list)
            assert len(texts) == num_texts
            for text in texts:
                assert len(text) <= num_chars
                words = re.sub(r"[.\n]+", " ", text.lower()).split()
                assert all(word in self.custom_word_list for word in words)

    def test_get_default_words_list(self, faker):
        words_list = faker.get_words_list()
        assert all(word in EnUsLoremProvider.word_list for word in words_list)

    @pytest.mark.parametrize("part_of_speech", [("verb"), ("adverb"), ("noun")], ids=["verb", "adverb", "noun"])
    def test_get_words_list_part_of_speech(self, faker, part_of_speech):
        words_list = faker.get_words_list(part_of_speech=part_of_speech)
        assert (word in EnUsLoremProvider.parts_of_speech[part_of_speech] for word in words_list)

    def test_get_words_list_invalid_part_of_speech(self, faker):
        part_of_speech = "invalid part of speech"

        with pytest.raises(ValueError) as exc_info:
            faker.get_words_list(part_of_speech=part_of_speech)

        assert exc_info.type is ValueError
        assert exc_info.value.args[0] == f"{part_of_speech} is not recognized as a part of speech."

    def test_get_words_list_part_of_speech_ignored(self, faker):
        words = faker.get_words_list(part_of_speech="ignored part of speech", ext_word_list=self.custom_word_list)
        assert all(word in self.custom_word_list for word in words)


class TestCsCz:
    """Test cs_CZ lorem provider"""

    word_list = [word.lower() for word in CsCzLoremProvider.word_list]

    def test_paragraph(self, faker, num_samples):
        num_sentences = 10
        for _ in range(num_samples):
            paragraph = faker.paragraph(nb_sentences=num_sentences)
            assert isinstance(paragraph, str)
            words = paragraph.replace(".", "").split()
            assert all(word.lower() in self.word_list for word in words)

    def test_paragraphs(self, faker, num_samples):
        num_paragraphs = 5
        for _ in range(num_samples):
            paragraphs = faker.paragraphs(nb=num_paragraphs)
            for paragraph in paragraphs:
                assert isinstance(paragraph, str)
                words = paragraph.replace(".", "").split()
                assert all(word.lower() in self.word_list for word in words)

    def test_sentence(self, faker, num_samples):
        num_words = 10
        for _ in range(num_samples):
            sentence = faker.sentence(nb_words=num_words)
            assert isinstance(sentence, str)
            words = sentence.replace(".", "").split()
            assert all(word.lower() in self.word_list for word in words)

    def test_sentences(self, faker, num_samples):
        num_sentences = 5
        for _ in range(num_samples):
            sentences = faker.sentences(nb=num_sentences)
            for sentence in sentences:
                assert isinstance(sentence, str)
                words = sentence.replace(".", "").split()
                assert all(word.lower() in self.word_list for word in words)

    def test_text(self, faker, num_samples):
        num_chars = 25
        for _ in range(num_samples):
            text = faker.text(max_nb_chars=num_chars)
            assert isinstance(text, str)
            words = re.sub(r"[.\n]+", " ", text).split()
            assert all(word.lower() in self.word_list for word in words)

    def test_texts(self, faker, num_samples):
        num_texts = 5
        num_chars = 25
        for _ in range(num_samples):
            texts = faker.texts(max_nb_chars=num_chars, nb_texts=num_texts)
            for text in texts:
                assert isinstance(text, str)
                words = re.sub(r"[.\n]+", " ", text).split()
                assert all(word.lower() in self.word_list for word in words)

    def test_word(self, faker, num_samples):
        for _ in range(num_samples):
            word = faker.word()
            assert isinstance(word, str) and word in CsCzLoremProvider.word_list

    def test_words(self, faker, num_samples):
        num_words = 5
        for _ in range(num_samples):
            words = faker.words(num_words)
            assert all(isinstance(word, str) and word in CsCzLoremProvider.word_list for word in words)


class TestAzAz:
    """Test az_AZ lorem provider"""

    word_list = [word.lower() for word in AzAzLoremProvider.word_list]

    def test_paragraph(self, faker, num_samples):
        num_sentences = 10
        for _ in range(num_samples):
            paragraph = faker.paragraph(nb_sentences=num_sentences)
            assert isinstance(paragraph, str)
            words = paragraph.replace(".", "").split()
            assert all(word.lower() in self.word_list for word in words)

    def test_paragraphs(self, faker, num_samples):
        num_paragraphs = 5
        for _ in range(num_samples):
            paragraphs = faker.paragraphs(nb=num_paragraphs)
            for paragraph in paragraphs:
                assert isinstance(paragraph, str)
                words = paragraph.replace(".", "").split()
                assert all(word.lower() in self.word_list for word in words)

    def test_sentence(self, faker, num_samples):
        num_words = 10
        for _ in range(num_samples):
            sentence = faker.sentence(nb_words=num_words)
            assert isinstance(sentence, str)
            words = sentence.replace(".", "").split()
            assert all(word.lower() in self.word_list for word in words)

    def test_sentences(self, faker, num_samples):
        num_sentences = 5
        for _ in range(num_samples):
            sentences = faker.sentences(nb=num_sentences)
            for sentence in sentences:
                assert isinstance(sentence, str)
                words = sentence.replace(".", "").split()
                assert all(word.lower() in self.word_list for word in words)

    def test_text(self, faker, num_samples):
        num_chars = 25
        for _ in range(num_samples):
            text = faker.text(max_nb_chars=num_chars)
            assert isinstance(text, str)
            words = re.sub(r"[.\n]+", " ", text).split()
            assert all(word.lower() in self.word_list for word in words)

    def test_texts(self, faker, num_samples):
        num_texts = 5
        num_chars = 25
        for _ in range(num_samples):
            texts = faker.texts(max_nb_chars=num_chars, nb_texts=num_texts)
            for text in texts:
                assert isinstance(text, str)
                words = re.sub(r"[.\n]+", " ", text).split()
                assert all(word.lower() in self.word_list for word in words)

    def test_word(self, faker, num_samples):
        for _ in range(num_samples):
            word = faker.word()
            assert isinstance(word, str) and word in AzAzLoremProvider.word_list

    def test_words(self, faker, num_samples):
        num_words = 5
        for _ in range(num_samples):
            words = faker.words(num_words)
            assert all(isinstance(word, str) and word in AzAzLoremProvider.word_list for word in words)


class TestFaIr:
    """Test fa_IR lorem provider"""

    word_list = [word.lower() for word in FaIrLoremProvider.word_list]

    def test_paragraph(self, faker, num_samples):
        num_sentences = 10
        for _ in range(num_samples):
            paragraph = faker.paragraph(nb_sentences=num_sentences)
            assert isinstance(paragraph, str)
            words = paragraph.replace(".", "").split()
            assert all(word.lower() in self.word_list for word in words)

    def test_paragraphs(self, faker, num_samples):
        num_paragraphs = 5
        for _ in range(num_samples):
            paragraphs = faker.paragraphs(nb=num_paragraphs)
            for paragraph in paragraphs:
                assert isinstance(paragraph, str)
                words = paragraph.replace(".", "").split()
                assert all(word.lower() in self.word_list for word in words)

    def test_sentence(self, faker, num_samples):
        num_words = 10
        for _ in range(num_samples):
            sentence = faker.sentence(nb_words=num_words)
            assert isinstance(sentence, str)
            words = sentence.replace(".", "").split()
            assert all(word.lower() in self.word_list for word in words)

    def test_sentences(self, faker, num_samples):
        num_sentences = 5
        for _ in range(num_samples):
            sentences = faker.sentences(nb=num_sentences)
            for sentence in sentences:
                assert isinstance(sentence, str)
                words = sentence.replace(".", "").split()
                assert all(word.lower() in self.word_list for word in words)

    def test_text(self, faker, num_samples):
        num_chars = 25
        for _ in range(num_samples):
            text = faker.text(max_nb_chars=num_chars)
            assert isinstance(text, str)
            words = re.sub(r"[.\n]+", " ", text).split()
            assert all(word.lower() in self.word_list for word in words)

    def test_texts(self, faker, num_samples):
        num_texts = 5
        num_chars = 25
        for _ in range(num_samples):
            texts = faker.texts(max_nb_chars=num_chars, nb_texts=num_texts)
            for text in texts:
                assert isinstance(text, str)
                words = re.sub(r"[.\n]+", " ", text).split()
                assert all(word.lower() in self.word_list for word in words)

    def test_word(self, faker, num_samples):
        for _ in range(num_samples):
            word = faker.word()
            assert isinstance(word, str) and word in FaIrLoremProvider.word_list

    def test_words(self, faker, num_samples):
        num_words = 5
        for _ in range(num_samples):
            words = faker.words(num_words)
            assert all(isinstance(word, str) and word in FaIrLoremProvider.word_list for word in words)


class TestBnBd:
    """Test bn_BD lorem provider"""

    word_list = BnBdLoremProvider.word_list

    def test_paragraph(self, faker, num_samples):
        num_sentences = 10
        for _ in range(num_samples):
            paragraph = faker.paragraph(nb_sentences=num_sentences)
            assert isinstance(paragraph, str)
            words = paragraph.replace("।", "").split()
            assert all(word in self.word_list for word in words)

    def test_paragraphs(self, faker, num_samples):
        num_paragraphs = 5
        for _ in range(num_samples):
            paragraphs = faker.paragraphs(nb=num_paragraphs)
            for paragraph in paragraphs:
                assert isinstance(paragraph, str)
                words = paragraph.replace("।", "").split()
                assert all(word in self.word_list for word in words)

    def test_sentence(self, faker, num_samples):
        num_words = 10
        for _ in range(num_samples):
            sentence = faker.sentence(nb_words=num_words)
            assert isinstance(sentence, str)
            words = sentence.replace("।", "").split()
            assert all(word in self.word_list for word in words)

    def test_sentences(self, faker, num_samples):
        num_sentences = 5
        for _ in range(num_samples):
            sentences = faker.sentences(nb=num_sentences)
            for sentence in sentences:
                assert isinstance(sentence, str)
                words = sentence.replace("।", "").split()
                assert all(word in self.word_list for word in words)


class TestDeDe:
    """Test ```de_DE``` lorem provider"""

    word_list = [word.lower() for word in DeDeLoremProvider.word_list]

    def test_paragraph(self, faker, num_samples):
        num_sentences = 10
        for _ in range(num_samples):
            paragraph = faker.paragraph(nb_sentences=num_sentences)
            assert isinstance(paragraph, str)
            words = paragraph.replace(".", "").split()
            assert all(word.lower() in self.word_list for word in words)

    def test_paragraphs(self, faker, num_samples):
        num_paragraphs = 5
        for _ in range(num_samples):
            paragraphs = faker.paragraphs(nb=num_paragraphs)
            for paragraph in paragraphs:
                assert isinstance(paragraph, str)
                words = paragraph.replace(".", "").split()
                assert all(word.lower() in self.word_list for word in words)

    def test_sentence(self, faker, num_samples):
        num_words = 10
        for _ in range(num_samples):
            sentence = faker.sentence(nb_words=num_words)
            assert isinstance(sentence, str)
            words = sentence.replace(".", "").split()
            assert all(word.lower() in self.word_list for word in words)

    def test_sentences(self, faker, num_samples):
        num_sentences = 5
        for _ in range(num_samples):
            sentences = faker.sentences(nb=num_sentences)
            for sentence in sentences:
                assert isinstance(sentence, str)
                words = sentence.replace(".", "").split()
                assert all(word.lower() in self.word_list for word in words)

    def test_text(self, faker, num_samples):
        num_chars = 25
        for _ in range(num_samples):
            text = faker.text(max_nb_chars=num_chars)
            assert isinstance(text, str)
            words = re.sub(r"[.\n]+", " ", text).split()
            assert all(word.lower() in self.word_list for word in words)

    def test_texts(self, faker, num_samples):
        num_texts = 5
        num_chars = 25
        for _ in range(num_samples):
            texts = faker.texts(max_nb_chars=num_chars, nb_texts=num_texts)
            for text in texts:
                assert isinstance(text, str)
                words = re.sub(r"[.\n]+", " ", text).split()
                assert all(word.lower() in self.word_list for word in words)

    def test_word(self, faker, num_samples):
        for _ in range(num_samples):
            word = faker.word()
            assert isinstance(word, str) and word in DeDeLoremProvider.word_list

    def test_words(self, faker, num_samples):
        num_words = 5
        for _ in range(num_samples):
            words = faker.words(num_words)
            assert all(isinstance(word, str) and word in DeDeLoremProvider.word_list for word in words)


class TestDeAt:
    """Test ```de_AT``` lorem provider"""

    word_list = [word.lower() for word in DeAtLoremProvider.word_list]

    def test_paragraph(self, faker, num_samples):
        num_sentences = 10
        for _ in range(num_samples):
            paragraph = faker.paragraph(nb_sentences=num_sentences)
            assert isinstance(paragraph, str)
            words = paragraph.replace(".", "").split()
            assert all(word.lower() in self.word_list for word in words)

    def test_paragraphs(self, faker, num_samples):
        num_paragraphs = 5
        for _ in range(num_samples):
            paragraphs = faker.paragraphs(nb=num_paragraphs)
            for paragraph in paragraphs:
                assert isinstance(paragraph, str)
                words = paragraph.replace(".", "").split()
                assert all(word.lower() in self.word_list for word in words)

    def test_sentence(self, faker, num_samples):
        num_words = 10
        for _ in range(num_samples):
            sentence = faker.sentence(nb_words=num_words)
            assert isinstance(sentence, str)
            words = sentence.replace(".", "").split()
            assert all(word.lower() in self.word_list for word in words)

    def test_sentences(self, faker, num_samples):
        num_sentences = 5
        for _ in range(num_samples):
            sentences = faker.sentences(nb=num_sentences)
            for sentence in sentences:
                assert isinstance(sentence, str)
                words = sentence.replace(".", "").split()
                assert all(word.lower() in self.word_list for word in words)

    def test_text(self, faker, num_samples):
        num_chars = 25
        for _ in range(num_samples):
            text = faker.text(max_nb_chars=num_chars)
            assert isinstance(text, str)
            words = re.sub(r"[.\n]+", " ", text).split()
            assert all(word.lower() in self.word_list for word in words)

    def test_texts(self, faker, num_samples):
        num_texts = 5
        num_chars = 25
        for _ in range(num_samples):
            texts = faker.texts(max_nb_chars=num_chars, nb_texts=num_texts)
            for text in texts:
                assert isinstance(text, str)
                words = re.sub(r"[.\n]+", " ", text).split()
                assert all(word.lower() in self.word_list for word in words)

    def test_word(self, faker, num_samples):
        for _ in range(num_samples):
            word = faker.word()
            assert isinstance(word, str) and word in DeAtLoremProvider.word_list

    def test_words(self, faker, num_samples):
        num_words = 5
        for _ in range(num_samples):
            words = faker.words(num_words)
            assert all(isinstance(word, str) and word in DeAtLoremProvider.word_list for word in words)


class TestNlBe:
    """Test ```nl_BE``` lorem provider

    Copied from the TestDeDe class, but with the word_list from the NlBeLoremProvider.
    """

    word_list = [word.lower() for word in NlBeLoremProvider.word_list]

    def test_paragraph(self, faker, num_samples):
        num_sentences = 10
        for _ in range(num_samples):
            paragraph = faker.paragraph(nb_sentences=num_sentences)
            assert isinstance(paragraph, str)
            words = paragraph.replace(".", "").split()
            assert all(word.lower() in self.word_list for word in words)

    def test_paragraphs(self, faker, num_samples):
        num_paragraphs = 5
        for _ in range(num_samples):
            paragraphs = faker.paragraphs(nb=num_paragraphs)
            for paragraph in paragraphs:
                assert isinstance(paragraph, str)
                words = paragraph.replace(".", "").split()
                assert all(word.lower() in self.word_list for word in words)

    def test_sentence(self, faker, num_samples):
        num_words = 10
        for _ in range(num_samples):
            sentence = faker.sentence(nb_words=num_words)
            assert isinstance(sentence, str)
            words = sentence.replace(".", "").split()
            assert all(word.lower() in self.word_list for word in words)

    def test_sentences(self, faker, num_samples):
        num_sentences = 5
        for _ in range(num_samples):
            sentences = faker.sentences(nb=num_sentences)
            for sentence in sentences:
                assert isinstance(sentence, str)
                words = sentence.replace(".", "").split()
                assert all(word.lower() in self.word_list for word in words)

    def test_text(self, faker, num_samples):
        num_chars = 25
        for _ in range(num_samples):
            text = faker.text(max_nb_chars=num_chars)
            assert isinstance(text, str)
            words = re.sub(r"[.\n]+", " ", text).split()
            assert all(word.lower() in self.word_list for word in words)

    def test_texts(self, faker, num_samples):
        num_texts = 5
        num_chars = 25
        for _ in range(num_samples):
            texts = faker.texts(max_nb_chars=num_chars, nb_texts=num_texts)
            for text in texts:
                assert isinstance(text, str)
                words = re.sub(r"[.\n]+", " ", text).split()
                assert all(word.lower() in self.word_list for word in words)

    def test_word(self, faker, num_samples):
        for _ in range(num_samples):
            word = faker.word()
            assert isinstance(word, str) and word in NlBeLoremProvider.word_list

    def test_words(self, faker, num_samples):
        num_words = 5
        for _ in range(num_samples):
            words = faker.words(num_words)
            assert all(isinstance(word, str) and word in NlBeLoremProvider.word_list for word in words)


class TestUkUa:
    """Test uk_UA lorem provider"""

    word_list = [word.lower() for word in UkUaLoremProvider.word_list]

    def test_paragraph(self, faker, num_samples):
        num_sentences = 10
        for _ in range(num_samples):
            paragraph = faker.paragraph(nb_sentences=num_sentences)
            assert isinstance(paragraph, str)
            words = paragraph.replace(".", "").split()
            assert all(word.lower() in self.word_list for word in words)

    def test_paragraphs(self, faker, num_samples):
        num_paragraphs = 5
        for _ in range(num_samples):
            paragraphs = faker.paragraphs(nb=num_paragraphs)
            for paragraph in paragraphs:
                assert isinstance(paragraph, str)
                words = paragraph.replace(".", "").split()
                assert all(word.lower() in self.word_list for word in words)

    def test_sentence(self, faker, num_samples):
        num_words = 10
        for _ in range(num_samples):
            sentence = faker.sentence(nb_words=num_words)
            assert isinstance(sentence, str)
            words = sentence.replace(".", "").split()
            assert all(word.lower() in self.word_list for word in words)

    def test_sentences(self, faker, num_samples):
        num_sentences = 5
        for _ in range(num_samples):
            sentences = faker.sentences(nb=num_sentences)
            for sentence in sentences:
                assert isinstance(sentence, str)
                words = sentence.replace(".", "").split()
                assert all(word.lower() in self.word_list for word in words)

    def test_text(self, faker, num_samples):
        num_chars = 25
        for _ in range(num_samples):
            text = faker.text(max_nb_chars=num_chars)
            assert isinstance(text, str)
            words = re.sub(r"[.\n]+", " ", text).split()
            assert all(word.lower() in self.word_list for word in words)

    def test_texts(self, faker, num_samples):
        num_texts = 5
        num_chars = 25
        for _ in range(num_samples):
            texts = faker.texts(max_nb_chars=num_chars, nb_texts=num_texts)
            for text in texts:
                assert isinstance(text, str)
                words = re.sub(r"[.\n]+", " ", text).split()
                assert all(word.lower() in self.word_list for word in words)

    def test_word(self, faker, num_samples):
        for _ in range(num_samples):
            word = faker.word()
            assert isinstance(word, str) and word in UkUaLoremProvider.word_list

    def test_words(self, faker, num_samples):
        num_words = 5
        for _ in range(num_samples):
            words = faker.words(num_words)
            assert all(isinstance(word, str) and word in UkUaLoremProvider.word_list for word in words)


class TestViVn:
    """Test vi_VN lorem provider"""

    word_list = [word.lower() for word in ViVNLoremProvider.word_list]

    def test_paragraph(self, faker, num_samples):
        num_sentences = 10
        for _ in range(num_samples):
            paragraph = faker.paragraph(nb_sentences=num_sentences)
            assert isinstance(paragraph, str)
            words = paragraph.replace(".", "").split()
            assert all(word.lower() in self.word_list for word in words)

    def test_paragraphs(self, faker, num_samples):
        num_paragraphs = 5
        for _ in range(num_samples):
            paragraphs = faker.paragraphs(nb=num_paragraphs)
            for paragraph in paragraphs:
                assert isinstance(paragraph, str)
                words = paragraph.replace(".", "").split()
                assert all(word.lower() in self.word_list for word in words)

    def test_sentence(self, faker, num_samples):
        num_words = 10
        for _ in range(num_samples):
            sentence = faker.sentence(nb_words=num_words)
            assert isinstance(sentence, str)
            words = sentence.replace(".", "").split()
            assert all(word.lower() in self.word_list for word in words)

    def test_sentences(self, faker, num_samples):
        num_sentences = 5
        for _ in range(num_samples):
            sentences = faker.sentences(nb=num_sentences)
            for sentence in sentences:
                assert isinstance(sentence, str)
                words = sentence.replace(".", "").split()
                assert all(word.lower() in self.word_list for word in words)

    def test_text(self, faker, num_samples):
        num_chars = 25
        for _ in range(num_samples):
            text = faker.text(max_nb_chars=num_chars)
            assert isinstance(text, str)
            words = re.sub(r"[.\n]+", " ", text).split()
            assert all(word.lower() in self.word_list for word in words)

    def test_texts(self, faker, num_samples):
        num_texts = 5
        num_chars = 25
        for _ in range(num_samples):
            texts = faker.texts(max_nb_chars=num_chars, nb_texts=num_texts)
            for text in texts:
                assert isinstance(text, str)
                words = re.sub(r"[.\n]+", " ", text).split()
                assert all(word.lower() in self.word_list for word in words)

    def test_word(self, faker, num_samples):
        for _ in range(num_samples):
            word = faker.word()
            assert isinstance(word, str) and word in ViVNLoremProvider.word_list

    def test_words(self, faker, num_samples):
        num_words = 5
        for _ in range(num_samples):
            words = faker.words(num_words)
            assert all(isinstance(word, str) and word in ViVNLoremProvider.word_list for word in words)


class TestItIt:
    """Test it_IT lorem provider"""

    word_list = [word.lower() for word in ItItLoremProvider.word_list]

    def test_paragraph(self, faker, num_samples):
        num_sentences = 10
        for _ in range(num_samples):
            paragraph = faker.paragraph(nb_sentences=num_sentences)
            assert isinstance(paragraph, str)
            words = paragraph.replace(".", "").split()
            assert all(word.lower() in self.word_list for word in words)

    def test_paragraphs(self, faker, num_samples):
        num_paragraphs = 5
        for _ in range(num_samples):
            paragraphs = faker.paragraphs(nb=num_paragraphs)
            for paragraph in paragraphs:
                assert isinstance(paragraph, str)
                words = paragraph.replace(".", "").split()
                assert all(word.lower() in self.word_list for word in words)

    def test_sentence(self, faker, num_samples):
        num_words = 10
        for _ in range(num_samples):
            sentence = faker.sentence(nb_words=num_words)
            assert isinstance(sentence, str)
            words = sentence.replace(".", "").split()
            assert all(word.lower() in self.word_list for word in words)

    def test_sentences(self, faker, num_samples):
        num_sentences = 5
        for _ in range(num_samples):
            sentences = faker.sentences(nb=num_sentences)
            for sentence in sentences:
                assert isinstance(sentence, str)
                words = sentence.replace(".", "").split()
                assert all(word.lower() in self.word_list for word in words)

    def test_text(self, faker, num_samples):
        num_chars = 25
        for _ in range(num_samples):
            text = faker.text(max_nb_chars=num_chars)
            assert isinstance(text, str)
            words = re.sub(r"[.\n]+", " ", text).split()
            assert all(word.lower() in self.word_list for word in words)

    def test_texts(self, faker, num_samples):
        num_texts = 5
        num_chars = 25
        for _ in range(num_samples):
            texts = faker.texts(max_nb_chars=num_chars, nb_texts=num_texts)
            for text in texts:
                assert isinstance(text, str)
                words = re.sub(r"[.\n]+", " ", text).split()
                assert all(word.lower() in self.word_list for word in words)

    def test_word(self, faker, num_samples):
        for _ in range(num_samples):
            word = faker.word()
            assert isinstance(word, str) and word in ItItLoremProvider.word_list

    def test_words(self, faker, num_samples):
        num_words = 5
        for _ in range(num_samples):
            words = faker.words(num_words)
            assert all(isinstance(word, str) and word in ItItLoremProvider.word_list for word in words)
