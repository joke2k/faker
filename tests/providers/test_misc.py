# coding=utf-8

from __future__ import unicode_literals
import csv
import io
import itertools
import tarfile
import unittest
import uuid
import zipfile
import six

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

from faker import Faker


class TestMisc(unittest.TestCase):
    """Tests miscellaneous generators"""
    def setUp(self):
        self.fake = Faker()
        Faker.seed(0)

    def test_uuid4(self):
        uuid4 = self.fake.uuid4()
        assert uuid4
        assert isinstance(uuid4, six.string_types)

    def test_uuid4_int(self):
        uuid4 = self.fake.uuid4(cast_to=int)
        assert uuid4
        assert isinstance(uuid4, six.integer_types)

    def test_uuid4_uuid_object(self):
        uuid4 = self.fake.uuid4(cast_to=lambda x: x)
        assert uuid4
        assert isinstance(uuid4, uuid.UUID)

    def test_uuid4_seedability(self):
        for _ in range(10):
            random_seed = self.fake.random_int()
            baseline_fake = Faker()
            Faker.seed(random_seed)
            expected_uuids = [baseline_fake.uuid4() for i in range(1000)]

            new_fake = Faker()
            Faker.seed(random_seed)
            new_uuids = [new_fake.uuid4() for i in range(1000)]
            assert new_uuids == expected_uuids

    def test_zip_invalid_file(self):
        with self.assertRaises(ValueError):
            self.fake.zip(num_files='1')

        with self.assertRaises(ValueError):
            self.fake.zip(num_files=0)

        with self.assertRaises(ValueError):
            self.fake.zip(min_file_size='1')

        with self.assertRaises(ValueError):
            self.fake.zip(min_file_size=0)

        with self.assertRaises(ValueError):
            self.fake.zip(uncompressed_size='1')

        with self.assertRaises(ValueError):
            self.fake.zip(uncompressed_size=0)

    def test_zip_one_byte_undersized(self):
        for _ in range(10):
            num_files = self.fake.random.randint(1, 100)
            min_file_size = self.fake.random.randint(1, 1024)
            uncompressed_size = num_files * min_file_size - 1

            # Will always fail because of bad size requirements
            with self.assertRaises(AssertionError):
                self.fake.zip(
                    uncompressed_size=uncompressed_size, num_files=num_files,
                    min_file_size=min_file_size,
                )

    def test_zip_exact_minimum_size(self):
        for _ in range(10):
            num_files = self.fake.random.randint(1, 100)
            min_file_size = self.fake.random.randint(1, 1024)
            uncompressed_size = num_files * min_file_size

            zip_bytes = self.fake.zip(
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
        for _ in range(10):
            num_files = self.fake.random.randint(1, 100)
            min_file_size = self.fake.random.randint(1, 1024)
            expected_extra_bytes = self.fake.random.randint(1, 1024 * 1024)
            uncompressed_size = num_files * min_file_size + expected_extra_bytes

            zip_bytes = self.fake.zip(
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
            zip_bytes = self.fake.zip(
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
            zip_bytes = self.fake.zip(
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
                self.fake.zip(
                    uncompressed_size=uncompressed_size, num_files=num_files,
                    min_file_size=min_file_size, compression=compression,
                )

    def test_tar_invalid_file(self):
        with self.assertRaises(ValueError):
            self.fake.tar(num_files='1')

        with self.assertRaises(ValueError):
            self.fake.tar(num_files=0)

        with self.assertRaises(ValueError):
            self.fake.tar(min_file_size='1')

        with self.assertRaises(ValueError):
            self.fake.tar(min_file_size=0)

        with self.assertRaises(ValueError):
            self.fake.tar(uncompressed_size='1')

        with self.assertRaises(ValueError):
            self.fake.tar(uncompressed_size=0)

    def test_tar_one_byte_undersized(self):
        for _ in range(10):
            num_files = self.fake.random.randint(1, 100)
            min_file_size = self.fake.random.randint(1, 1024)
            uncompressed_size = num_files * min_file_size - 1

            # Will always fail because of conflicting size requirements
            with self.assertRaises(AssertionError):
                self.fake.tar(
                    uncompressed_size=uncompressed_size, num_files=num_files,
                    min_file_size=min_file_size,
                )

    def test_tar_exact_minimum_size(self):
        for _ in range(10):
            num_files = self.fake.random.randint(1, 100)
            min_file_size = self.fake.random.randint(1, 1024)
            uncompressed_size = num_files * min_file_size

            tar_bytes = self.fake.tar(
                uncompressed_size=uncompressed_size, num_files=num_files,
                min_file_size=min_file_size,
            )
            tar_buffer = io.BytesIO(tar_bytes)
            with tarfile.open(fileobj=tar_buffer) as tar_handle:
                # Verify tar has the correct number of files
                members = tar_handle.getmembers()
                assert len(members) == num_files

                # Every file's size will be the minimum specified
                total_size = 0
                for member in members:
                    assert member.size == min_file_size
                    total_size += member.size

                # The file sizes should sum up to the specified uncompressed size
                assert total_size == uncompressed_size

    def test_tar_over_minimum_size(self):
        for _ in range(10):
            num_files = self.fake.random.randint(1, 100)
            min_file_size = self.fake.random.randint(1, 1024)
            expected_extra_bytes = self.fake.random.randint(1, 1024 * 1024)
            uncompressed_size = num_files * min_file_size + expected_extra_bytes

            tar_bytes = self.fake.tar(
                uncompressed_size=uncompressed_size, num_files=num_files,
                min_file_size=min_file_size,
            )
            tar_buffer = io.BytesIO(tar_bytes)
            with tarfile.open(fileobj=tar_buffer) as tar_handle:
                # Verify tar has the correct number of files
                members = tar_handle.getmembers()
                assert len(members) == num_files

                # Every file's size will be at least the minimum specified
                extra_bytes = 0
                total_size = 0
                for member in members:
                    assert member.size >= min_file_size
                    total_size += member.size
                    if member.size > min_file_size:
                        extra_bytes += (member.size - min_file_size)

                # The file sizes should sum up to the specified uncompressed size
                # and the extra bytes counted should be the one we expect
                assert total_size == uncompressed_size
                assert extra_bytes == expected_extra_bytes

    @unittest.skipIf(six.PY2, 'Python 3 only')
    def test_tar_compression_py3(self):
        num_files = 25
        min_file_size = 512
        uncompressed_size = 50 * 1024
        compression_mapping = [
            ('gzip', 'r:gz'),
            ('gz', 'r:gz'),
            ('bzip2', 'r:bz2'),
            ('bz2', 'r:bz2'),
            ('lzma', 'r:xz'),
            ('xz', 'r:xz'),
            (None, 'r'),
        ]

        for compression, read_mode in compression_mapping:
            tar_bytes = self.fake.tar(
                uncompressed_size=uncompressed_size, num_files=num_files,
                min_file_size=min_file_size, compression=compression,
            )
            tar_buffer = io.BytesIO(tar_bytes)
            with tarfile.open(fileobj=tar_buffer, mode=read_mode) as tar_handle:
                # Verify tar has the correct number of files
                members = tar_handle.getmembers()
                assert len(members) == num_files

    @unittest.skipIf(six.PY3, 'Python 2 only')
    def test_tar_compression_py2(self):
        num_files = 25
        min_file_size = 512
        uncompressed_size = 50 * 1024
        compression_mapping = [
            ('gzip', 'r:gz'),
            ('gz', 'r:gz'),
            ('bzip2', 'r:bz2'),
            ('bz2', 'r:bz2'),
            (None, 'r'),
        ]

        for compression, read_mode in compression_mapping:
            tar_bytes = self.fake.tar(
                uncompressed_size=uncompressed_size, num_files=num_files,
                min_file_size=min_file_size, compression=compression,
            )
            tar_buffer = io.BytesIO(tar_bytes)
            with tarfile.open(fileobj=tar_buffer, mode=read_mode) as tar_handle:
                # Verify tar has the correct number of files
                members = tar_handle.getmembers()
                assert len(members) == num_files

        # LZMA is not supported in Python 2
        for compression in ['lzma', 'xz']:
            with self.assertRaises(RuntimeError):
                self.fake.tar(
                    uncompressed_size=uncompressed_size, num_files=num_files,
                    min_file_size=min_file_size, compression=compression,
                )

    def test_dsv_with_invalid_values(self):
        with self.assertRaises(ValueError):
            self.fake.dsv(num_rows='1')

        with self.assertRaises(ValueError):
            self.fake.dsv(num_rows=0)

        with self.assertRaises(TypeError):
            self.fake.dsv(header=None, data_columns=1)

        with self.assertRaises(TypeError):
            self.fake.dsv(header=1, data_columns=['???'])

        with self.assertRaises(ValueError):
            self.fake.dsv(header=['Column 1', 'Column 2'], data_columns=['???'])

    def test_dsv_no_header(self):
        data_columns = ['????', '?????']
        for _ in range(10):
            num_rows = self.fake.random.randint(1, 1000)
            dsv = self.fake.dsv(header=None, data_columns=data_columns, num_rows=num_rows)
            reader = csv.reader(six.StringIO(dsv), dialect='faker-csv')

            # Verify each row has correct number of columns
            for row in reader:
                assert len(row) == len(data_columns)

            # Verify correct number of lines read
            assert reader.line_num == num_rows

    def test_dsv_with_valid_header(self):
        header = ['Column 1', 'Column 2']
        data_columns = ['????', '?????']
        for _ in range(10):
            num_rows = self.fake.random.randint(1, 1000)
            dsv = self.fake.dsv(header=header, data_columns=data_columns, num_rows=num_rows)
            reader = csv.reader(six.StringIO(dsv), dialect='faker-csv')

            # Verify each row has correct number of columns
            for row in reader:
                assert len(row) == len(data_columns)

            # Verify correct number of lines read (additional header row)
            assert reader.line_num == num_rows + 1

    def test_dsv_with_row_ids(self):
        data_columns = ['????', '?????']
        for _ in range(10):
            counter = 0
            num_rows = self.fake.random.randint(1, 1000)
            dsv = self.fake.dsv(
                header=None, data_columns=data_columns,
                num_rows=num_rows, include_row_ids=True,
            )
            reader = csv.reader(six.StringIO(dsv), dialect='faker-csv')

            # Verify each row has correct number of columns
            # and row ids increment correctly
            for row in reader:
                assert len(row) == len(data_columns) + 1
                counter += 1
                assert row[0] == str(counter)

            # Verify correct number of lines read
            assert reader.line_num == num_rows

    def test_dsv_data_columns(self):
        num_rows = 10
        data_columns = ['{{name}}', '#??-####', '{{address}}', '{{phone_number}}']
        with patch.object(self.fake['en_US'], 'pystr_format') as mock_pystr_format:
            mock_pystr_format.assert_not_called()
            self.fake.dsv(data_columns=data_columns, num_rows=num_rows)

            # pystr_format will be called for each data column and each row
            calls = mock_pystr_format.call_args_list
            assert len(calls) == num_rows * len(data_columns)

            # Elements in data_columns will be used in sequence per row generation cycle
            column_cycle = itertools.cycle(data_columns)
            for args, kwargs in calls:
                assert args[0] == next(column_cycle)
                assert kwargs == {}

    def test_dsv_csvwriter_kwargs(self):
        data_keys = ['header', 'data_columns', 'num_rows', 'include_row_ids']
        test_kwargs = {
            'dialect': 'excel',
            'header': ['Column 1', 'Column 2'],
            'data_columns': ['????', '?????'],
            'num_rows': 5,
            'include_row_ids': True,
            'delimiter': ';',
            'invalid_kwarg': 'invalid_value',
        }
        with patch('faker.providers.misc.csv.writer') as mock_writer:
            mock_writer.assert_not_called()
            self.fake.dsv(**test_kwargs)
            assert mock_writer.call_count == 1

            # Remove all data generation kwargs
            for key in data_keys:
                del test_kwargs[key]

            # Verify csv.writer was called with the remaining kwargs
            for args, kwargs in mock_writer.call_args_list:
                assert kwargs == test_kwargs

    def test_csv_helper_method(self):
        kwargs = {
            'header': ['Column 1', 'Column 2'],
            'data_columns': ['????', '?????'],
            'num_rows': 5,
            'include_row_ids': True,
        }
        with patch('faker.providers.misc.Provider.dsv') as mock_dsv:
            mock_dsv.assert_not_called()
            self.fake.csv(**kwargs)
            kwargs['delimiter'] = ','
            mock_dsv.assert_called_once_with(**kwargs)

    def test_tsv_helper_method(self):
        kwargs = {
            'header': ['Column 1', 'Column 2'],
            'data_columns': ['????', '?????'],
            'num_rows': 5,
            'include_row_ids': True,
        }
        with patch('faker.providers.misc.Provider.dsv') as mock_dsv:
            mock_dsv.assert_not_called()
            self.fake.tsv(**kwargs)
            kwargs['delimiter'] = '\t'
            mock_dsv.assert_called_once_with(**kwargs)

    def test_psv_helper_method(self):
        kwargs = {
            'header': ['Column 1', 'Column 2'],
            'data_columns': ['????', '?????'],
            'num_rows': 5,
            'include_row_ids': True,
        }
        with patch('faker.providers.misc.Provider.dsv') as mock_dsv:
            mock_dsv.assert_not_called()
            self.fake.psv(**kwargs)
            kwargs['delimiter'] = '|'
            mock_dsv.assert_called_once_with(**kwargs)
