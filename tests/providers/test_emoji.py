from __future__ import unicode_literals

import unittest

from faker import Faker
from faker.providers.emoji import Provider as EmojiProvider


class TestEmoji(unittest.TestCase):
    """ Tests emoji """

    def setUp(self):
        self.factory = Faker()
        self.all_emojis = [EmojiProvider._convert_to_unicode(e[0]) for e in EmojiProvider._collect_emojis()]

    def get_main_category(self, position=0):
        return list(EmojiProvider.emojis.keys())[position]

    def get_sub_category(self, main_category, position=0):
        return list(EmojiProvider.emojis[main_category].keys())[position]

    def get_main_category_emojis(self, main_category, only_code=False):
        main_category_emojis = []
        for sub_category in EmojiProvider.emojis[main_category].keys():
            main_category_emojis.extend(EmojiProvider.emojis[main_category][sub_category])
        if only_code:
            return [EmojiProvider._convert_to_unicode(code) for code, _, _ in main_category_emojis]
        return main_category_emojis

    def get_sub_category_emojis(self, main_category, sub_category, only_code=False):
        sub_category_emojis = EmojiProvider.emojis[main_category][sub_category]
        if only_code:
            return [EmojiProvider._convert_to_unicode(code) for code, _, _ in sub_category_emojis]
        return sub_category_emojis

    def test_emoji_without_category(self):
        self.assertIn(self.factory.emoji(), self.all_emojis)

    def test_emoji_with_main_category(self):
        main_category = self.get_main_category()
        self.assertIn(
            self.factory.emoji(main_category),
            self.get_main_category_emojis(main_category, only_code=True)
        )

    def test_emoji_with_sub_category(self):
        main_category = self.get_main_category()
        sub_category = self.get_sub_category(main_category)

        self.assertIn(
            self.factory.emoji(sub_category),
            self.get_sub_category_emojis(main_category, sub_category, only_code=True)
        )

    def test_emoji_with_multiple_main_categories(self):
        # with main categories
        categories = [
            self.get_main_category(0),
            self.get_main_category(1)
        ]
        categories_emojis = self.get_main_category_emojis(categories[0], True)
        categories_emojis.extend(self.get_main_category_emojis(categories[1], True))

        self.assertIn(
            self.factory.emoji(categories),
            categories_emojis
        )

    def test_emoji_with_multiple_sub_categories(self):
        main_category = self.get_main_category()
        sub_categories = [
            self.get_sub_category(main_category, 0),
            self.get_sub_category(main_category, 1),
        ]
        sub_categories_emojis = self.get_sub_category_emojis(main_category, sub_categories[0], True)
        sub_categories_emojis.extend(self.get_sub_category_emojis(main_category, sub_categories[1], True))

        self.assertIn(
            self.factory.emoji(sub_categories),
            sub_categories_emojis
        )

    def test_emoji_with_multiple_mixed_categories(self):
        main_category = self.get_main_category()
        sub_main_category = self.get_main_category(1)
        sub_category = self.get_sub_category(sub_main_category)
        mixed_categories = [
            main_category,
            sub_category
        ]
        mixed_categories_emojis = self.get_main_category_emojis(main_category, True)
        mixed_categories_emojis.extend(self.get_sub_category_emojis(sub_main_category, sub_category, only_code=True))

        self.assertIn(
            self.factory.emoji(mixed_categories),
            mixed_categories_emojis
        )

    def test_get_main_category_emojis(self):
        main_category = self.get_main_category()
        main_category_emojis = self.get_main_category_emojis(main_category)

        self.assertEqual(
            main_category_emojis,
            EmojiProvider._get_category_emojis(main_category)
        )

    def test_get_sub_category_emojis(self):
        main_category = self.get_main_category()
        sub_category = self.get_sub_category(main_category)
        sub_category_emojis = EmojiProvider.emojis[main_category][sub_category]

        self.assertEqual(
            sub_category_emojis,
            EmojiProvider._get_category_emojis(sub_category)
        )

    def test_category_properties(self):
        self.assertEqual(
            list(EmojiProvider.emojis.keys()),
            EmojiProvider.main_categories
        )
        for main_cat in EmojiProvider.main_categories:
            for sub_cat in EmojiProvider.emojis[main_cat]:

                self.assertTrue(sub_cat in EmojiProvider.sub_categories)
                self.assertEqual(EmojiProvider.sub_categories[sub_cat], main_cat)

    def test_category_emoji_methods(self):
        main_category = self.get_main_category()
        emoji_method_name = 'emoji_{}'.format(main_category.replace('-', '_'))

        self.assertTrue(hasattr(EmojiProvider, emoji_method_name))
        self.assertIn(
            getattr(self.factory, emoji_method_name)(),
             self.get_main_category_emojis(main_category, only_code=True)
        )

    def test_keyword_emoji(self):
        keyword_with_one_emoji = 'shining'
        code = EmojiProvider._convert_to_unicode('U+1F31F')
        self.assertEqual(
            code,
            self.factory.emoji(keyword=keyword_with_one_emoji)
        )

    def test_category_not_found_fallback_to_keyword(self):
        keyword_with_one_emoji = 'shining'
        code = EmojiProvider._convert_to_unicode('U+1F31F')
        self.assertEqual(
            code,
            self.factory.emoji(keyword_with_one_emoji)
        )


