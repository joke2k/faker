import io
import tarfile
import unittest
import uuid
import zipfile
import six

from faker import Faker


class TestMisc(unittest.TestCase):
    """Tests miscellaneous generators"""
    def setUp(self):
        self.factory = Faker()

    def test_uuid4(self):
        uuid4 = self.factory.uuid4()
        assert uuid4
        assert isinstance(uuid4, six.string_types)

    def test_uuid4_int(self):
        uuid4 = self.factory.uuid4(cast_to=int)
        assert uuid4
        assert isinstance(uuid4, six.integer_types)

    def test_uuid4_uuid_object(self):
        uuid4 = self.factory.uuid4(cast_to=lambda x: x)
        assert uuid4
        assert isinstance(uuid4, uuid.UUID)

    def test_uuid4_seedability(self):
        for _ in range(10):
            random_seed = self.factory.random_int()
            baseline_fake = Faker()
            Faker.seed(random_seed)
            expected_uuids = [baseline_fake.uuid4() for i in range(1000)]

            new_fake = Faker()
            Faker.seed(random_seed)
            new_uuids = [new_fake.uuid4() for i in range(1000)]
            assert new_uuids == expected_uuids

    def test_zip_invalid_file(self):
        with self.assertRaises(ValueError):
            self.factory.zip(num_files='1')

        with self.assertRaises(ValueError):
            self.factory.zip(num_files=0)

        with self.assertRaises(ValueError):
            self.factory.zip(min_file_size='1')

        with self.assertRaises(ValueError):
            self.factory.zip(min_file_size=0)

        with self.assertRaises(ValueError):
            self.factory.zip(uncompressed_size='1')

        with self.assertRaises(ValueError):
            self.factory.zip(uncompressed_size=0)

    def test_zip_one_byte_undersized(self):
        Faker.seed(0)
        for _ in range(10):
            num_files = self.factory.random.randint(1, 100)
            min_file_size = self.factory.random.randint(1, 1024)
            uncompressed_size = num_files * min_file_size - 1

            # Will always fail because of bad size requirements
            with self.assertRaises(AssertionError):
                self.factory.zip(
                    uncompressed_size=uncompressed_size, num_files=num_files,
                    min_file_size=min_file_size,
                )

    def test_zip_exact_minimum_size(self):
        Faker.seed(0)
        for _ in range(10):
            num_files = self.factory.random.randint(1, 100)
            min_file_size = self.factory.random.randint(1, 1024)
            uncompressed_size = num_files * min_file_size

            zip_bytes = self.factory.zip(
                uncompressed_size=uncompressed_size, num_files=num_files,
                min_file_size=min_file_size,
            )
            zip_buffer = io.BytesIO(zip_bytes)
            with zipfile.ZipFile(zip_buffer, 'r') as zip_handle:
                # Verify zip archive is good
                assert zip_handle.testzip() is None

                # Verify zip archive has the correct number of files
                infolist = zip_handle.infolist()
                assert len(infolist) == num_files

                # Every file's size will be the minimum specified
                total_size = 0
                for info in infolist:
                    assert info.file_size == min_file_size
                    total_size += info.file_size

                # The file sizes should sum up to the specified uncompressed size
                assert total_size == uncompressed_size

    def test_zip_over_minimum_size(self):
        Faker.seed(0)
        for _ in range(10):
            num_files = self.factory.random.randint(1, 100)
            min_file_size = self.factory.random.randint(1, 1024)
            expected_extra_bytes = self.factory.random.randint(1, 1024 * 1024)
            uncompressed_size = num_files * min_file_size + expected_extra_bytes

            zip_bytes = self.factory.zip(
                uncompressed_size=uncompressed_size, num_files=num_files,
                min_file_size=min_file_size,
            )
            zip_buffer = io.BytesIO(zip_bytes)
            with zipfile.ZipFile(zip_buffer, 'r') as zip_handle:
                # Verify zip archive is good
                assert zip_handle.testzip() is None

                # Verify zip archive has the correct number of files
                infolist = zip_handle.infolist()
                assert len(infolist) == num_files

                # Every file's size will be at least the minimum specified
                extra_bytes = 0
                total_size = 0
                for info in infolist:
                    assert info.file_size >= min_file_size
                    total_size += info.file_size
                    if info.file_size > min_file_size:
                        extra_bytes += (info.file_size - min_file_size)

                # The file sizes should sum up to the specified uncompressed size
                # and the extra bytes counted must be equal to the one expected
                assert total_size == uncompressed_size
                assert extra_bytes == expected_extra_bytes

    @unittest.skipIf(six.PY2, 'Python 3 only')
    def test_zip_compression_py3(self):
        Faker.seed(0)
        num_files = 10
        min_file_size = 512
        uncompressed_size = 50 * 1024
        compression_mapping = [
            ('deflate', zipfile.ZIP_DEFLATED),
            ('gzip', zipfile.ZIP_DEFLATED),
            ('gz', zipfile.ZIP_DEFLATED),
            ('bzip2', zipfile.ZIP_BZIP2),
            ('bz2', zipfile.ZIP_BZIP2),
            ('lzma', zipfile.ZIP_LZMA),
            ('xz', zipfile.ZIP_LZMA),
            (None, zipfile.ZIP_STORED),
        ]
        for compression, compress_type in compression_mapping:
            zip_bytes = self.factory.zip(
                uncompressed_size=uncompressed_size, num_files=num_files,
                min_file_size=min_file_size, compression=compression,
            )
            zip_buffer = io.BytesIO(zip_bytes)
            with zipfile.ZipFile(zip_buffer, 'r') as zip_handle:
                # Verify zip archive is good
                assert zip_handle.testzip() is None

                # Verify compression type used
                for info in zip_handle.infolist():
                    assert info.compress_type == compress_type

    @unittest.skipIf(six.PY3, 'Python 2 only')
    def test_zip_compression_py2(self):
        Faker.seed(0)
        num_files = 10
        min_file_size = 512
        uncompressed_size = 50 * 1024
        compression_mapping = [
            ('deflate', zipfile.ZIP_DEFLATED),
            ('gzip', zipfile.ZIP_DEFLATED),
            ('gz', zipfile.ZIP_DEFLATED),
            (None, zipfile.ZIP_STORED),
        ]
        for compression, compress_type in compression_mapping:
            zip_bytes = self.factory.zip(
                uncompressed_size=uncompressed_size, num_files=num_files,
                min_file_size=min_file_size, compression=compression,
            )
            zip_buffer = io.BytesIO(zip_bytes)
            with zipfile.ZipFile(zip_buffer, 'r') as zip_handle:
                # Verify zip archive is good
                assert zip_handle.testzip() is None

                # Verify compression type used
                for info in zip_handle.infolist():
                    assert info.compress_type == compress_type

        # BZIP2 and LZMA are not supported in Python 2
        for compression in ['bzip2', 'bz2', 'lzma', 'xz']:
            with self.assertRaises(RuntimeError):
                self.factory.zip(
                    uncompressed_size=uncompressed_size,  num_files=num_files,
                    min_file_size=min_file_size, compression=compression,
                )
