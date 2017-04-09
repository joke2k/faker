from __future__ import unicode_literals

import unittest
import re

from faker import Factory
from faker.providers.file import Provider as FileProvider


class TestFile(unittest.TestCase):
    """ Tests file """

    def setUp(self):
        self.factory = Factory.create()

    def test_file_path(self):
        for _ in range(100):
            file_path = FileProvider.file_path()
            self.assertTrue(re.search(r'\/\w+\/\w+\.\w+', file_path))
            file_path = FileProvider.file_path(depth=3)
            self.assertTrue(re.search(r'\/\w+\/\w+\/\w+\.\w+', file_path))
            file_path = FileProvider.file_path(extension='pdf')
            self.assertTrue(re.search(r'\/\w+\/\w+\.pdf', file_path))
            file_path = FileProvider.file_path(category='image')
            self.assertTrue(re.search(r'\/\w+\/\w+\.(bmp|gif|jpeg|jpg|png|tiff)', file_path))
