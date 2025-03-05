import csv
import datetime
import io
import itertools
import json
import re
import tarfile
import unittest
import uuid
import xml
import zipfile

try:
    import PIL.Image
except ImportError:
    PIL = None

try:
    import xmltodict
except ImportError:
    xmltodict = None

from typing import Pattern
from unittest.mock import patch

import pytest

from faker import Faker, exceptions
from faker.contrib.pytest.plugin import DEFAULT_LOCALE, DEFAULT_SEED


@pytest.fixture(scope="class")
def _class_faker_with_foobar():
    _fake = Faker(locale=DEFAULT_LOCALE)
    _fake.add_provider(_FooBarProvider())
    _fake.set_arguments("argument_group", "param", "Baz")
    _fake.set_arguments("double", "multi", 2)
    return _fake


@pytest.fixture()
def faker_with_foobar(request):
    fake = request.getfixturevalue("_class_faker_with_foobar")
    seed = DEFAULT_SEED
    if "faker_seed" in request.fixturenames:
        seed = request.getfixturevalue("faker_seed")
    fake.seed_instance(seed=seed)
    return fake


class _FooBarProvider:
    def foo_bar(self, param: str = None) -> str:
        return "FooBar" + str(param) if param else "FooBar"

    def test_integer(self, multi=1) -> int:
        return 1 * multi

    def test_float(self, multi=1) -> float:
        return 1.1 * multi

    def test_date_time(self) -> datetime.datetime:
        return datetime.datetime(2022, 12, 22, 13, 42, 33, 123)


class TestMiscProvider:
    """Test miscellaneous provider methods"""

    num_samples = 10

    def test_uuid4_str(self, faker, num_samples):
        pattern: Pattern = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}")
        for _ in range(num_samples):
            assert pattern.fullmatch(faker.uuid4())

    def test_uuid4_int(self, faker, num_samples):
        for _ in range(num_samples):
            assert isinstance(faker.uuid4(cast_to=int), int)

    def test_uuid4_uuid_object(self, faker, num_samples):
        for _ in range(num_samples):
            uuid4 = faker.uuid4(cast_to=None)
            assert isinstance(uuid4, uuid.UUID)
            assert uuid4.version == 4

    def test_uuid4_seedability(self, faker, num_samples):
        for _ in range(num_samples):
            random_seed = faker.random_int()
            faker.seed_instance(random_seed)
            expected_uuids = [faker.uuid4() for _ in range(100)]
            faker.seed_instance(random_seed)
            new_uuids = [faker.uuid4() for _ in range(100)]
            assert new_uuids == expected_uuids

    def test_zip_invalid_file(self, faker):
        with pytest.raises(ValueError):
            faker.zip(num_files="1")

        with pytest.raises(ValueError):
            faker.zip(num_files=0)

        with pytest.raises(ValueError):
            faker.zip(min_file_size="1")

        with pytest.raises(ValueError):
            faker.zip(min_file_size=0)

        with pytest.raises(ValueError):
            faker.zip(uncompressed_size="1")

        with pytest.raises(ValueError):
            faker.zip(uncompressed_size=0)

    def test_zip_one_byte_undersized(self, faker, num_samples):
        for _ in range(num_samples):
            num_files = faker.random.randint(1, 100)
            min_file_size = faker.random.randint(1, 1024)
            uncompressed_size = num_files * min_file_size - 1

            # Will always fail because of bad size requirements
            with pytest.raises(AssertionError):
                faker.zip(
                    uncompressed_size=uncompressed_size,
                    num_files=num_files,
                    min_file_size=min_file_size,
                )

    def test_zip_exact_minimum_size(self, faker, num_samples):
        for _ in range(num_samples):
            num_files = faker.random.randint(1, 100)
            min_file_size = faker.random.randint(1, 1024)
            uncompressed_size = num_files * min_file_size

            zip_bytes = faker.zip(
                uncompressed_size=uncompressed_size,
                num_files=num_files,
                min_file_size=min_file_size,
            )
            zip_buffer = io.BytesIO(zip_bytes)
            with zipfile.ZipFile(zip_buffer, "r") as zip_handle:
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

    def test_zip_over_minimum_size(self, faker, num_samples):
        for _ in range(num_samples):
            num_files = faker.random.randint(1, 100)
            min_file_size = faker.random.randint(1, 1024)
            expected_extra_bytes = faker.random.randint(1, 1024 * 1024)
            uncompressed_size = num_files * min_file_size + expected_extra_bytes

            zip_bytes = faker.zip(
                uncompressed_size=uncompressed_size,
                num_files=num_files,
                min_file_size=min_file_size,
            )
            zip_buffer = io.BytesIO(zip_bytes)
            with zipfile.ZipFile(zip_buffer, "r") as zip_handle:
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
                        extra_bytes += info.file_size - min_file_size

                # The file sizes should sum up to the specified uncompressed size
                # and the extra bytes counted must be equal to the one expected
                assert total_size == uncompressed_size
                assert extra_bytes == expected_extra_bytes

    def test_zip_compression_py3(self, faker):
        num_files = 10
        min_file_size = 512
        uncompressed_size = 50 * 1024
        compression_mapping = [
            ("deflate", zipfile.ZIP_DEFLATED),
            ("gzip", zipfile.ZIP_DEFLATED),
            ("gz", zipfile.ZIP_DEFLATED),
            ("bzip2", zipfile.ZIP_BZIP2),
            ("bz2", zipfile.ZIP_BZIP2),
            ("lzma", zipfile.ZIP_LZMA),
            ("xz", zipfile.ZIP_LZMA),
            (None, zipfile.ZIP_STORED),
        ]
        for compression, compress_type in compression_mapping:
            zip_bytes = faker.zip(
                uncompressed_size=uncompressed_size,
                num_files=num_files,
                min_file_size=min_file_size,
                compression=compression,
            )
            zip_buffer = io.BytesIO(zip_bytes)
            with zipfile.ZipFile(zip_buffer, "r") as zip_handle:
                # Verify zip archive is good
                assert zip_handle.testzip() is None

                # Verify compression type used
                for info in zip_handle.infolist():
                    assert info.compress_type == compress_type

    def test_tar_invalid_file(self, faker):
        with pytest.raises(ValueError):
            faker.tar(num_files="1")

        with pytest.raises(ValueError):
            faker.tar(num_files=0)

        with pytest.raises(ValueError):
            faker.tar(min_file_size="1")

        with pytest.raises(ValueError):
            faker.tar(min_file_size=0)

        with pytest.raises(ValueError):
            faker.tar(uncompressed_size="1")

        with pytest.raises(ValueError):
            faker.tar(uncompressed_size=0)

    def test_tar_one_byte_undersized(self, faker, num_samples):
        for _ in range(num_samples):
            num_files = faker.random.randint(1, 100)
            min_file_size = faker.random.randint(1, 1024)
            uncompressed_size = num_files * min_file_size - 1

            # Will always fail because of conflicting size requirements
            with pytest.raises(AssertionError):
                faker.tar(
                    uncompressed_size=uncompressed_size,
                    num_files=num_files,
                    min_file_size=min_file_size,
                )

    def test_tar_exact_minimum_size(self, faker, num_samples):
        for _ in range(num_samples):
            num_files = faker.random.randint(1, 100)
            min_file_size = faker.random.randint(1, 1024)
            uncompressed_size = num_files * min_file_size

            tar_bytes = faker.tar(
                uncompressed_size=uncompressed_size,
                num_files=num_files,
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

    def test_tar_over_minimum_size(self, faker, num_samples):
        for _ in range(num_samples):
            num_files = faker.random.randint(1, 100)
            min_file_size = faker.random.randint(1, 1024)
            expected_extra_bytes = faker.random.randint(1, 1024 * 1024)
            uncompressed_size = num_files * min_file_size + expected_extra_bytes

            tar_bytes = faker.tar(
                uncompressed_size=uncompressed_size,
                num_files=num_files,
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
                        extra_bytes += member.size - min_file_size

                # The file sizes should sum up to the specified uncompressed size
                # and the extra bytes counted should be the one we expect
                assert total_size == uncompressed_size
                assert extra_bytes == expected_extra_bytes

    def test_tar_compression_py3(self, faker):
        num_files = 25
        min_file_size = 512
        uncompressed_size = 50 * 1024
        compression_mapping = [
            ("gzip", "r:gz"),
            ("gz", "r:gz"),
            ("bzip2", "r:bz2"),
            ("bz2", "r:bz2"),
            ("lzma", "r:xz"),
            ("xz", "r:xz"),
            (None, "r"),
        ]

        for compression, read_mode in compression_mapping:
            tar_bytes = faker.tar(
                uncompressed_size=uncompressed_size,
                num_files=num_files,
                min_file_size=min_file_size,
                compression=compression,
            )
            tar_buffer = io.BytesIO(tar_bytes)
            with tarfile.open(fileobj=tar_buffer, mode=read_mode) as tar_handle:
                # Verify tar has the correct number of files
                members = tar_handle.getmembers()
                assert len(members) == num_files

    @unittest.skipUnless(PIL, "requires the Python Image Library")
    def test_image(self, faker):
        img = PIL.Image.open(io.BytesIO(faker.image()))
        assert img.size == (256, 256)
        assert img.format == "PNG"
        img = PIL.Image.open(io.BytesIO(faker.image(size=(2, 2), image_format="tiff")))
        assert img.size == (2, 2)
        assert img.format == "TIFF"

    def test_image_no_pillow(self, faker):
        with patch.dict("sys.modules", {"PIL": None}):
            with pytest.raises(exceptions.UnsupportedFeature) as excinfo:
                faker.image()

            assert excinfo.value.name == "image"

    def test_dsv_with_invalid_values(self, faker):
        with pytest.raises(ValueError):
            faker.dsv(num_rows="1")

        with pytest.raises(ValueError):
            faker.dsv(num_rows=0)

        with pytest.raises(TypeError):
            faker.dsv(header=None, data_columns=1)

        with pytest.raises(TypeError):
            faker.dsv(header=1, data_columns=["???"])

        with pytest.raises(ValueError):
            faker.dsv(header=["Column 1", "Column 2"], data_columns=["???"])

    def test_dsv_no_header(self, faker, num_samples):
        data_columns = ["????", "?????"]
        for _ in range(num_samples):
            num_rows = faker.random.randint(1, 1000)
            dsv = faker.dsv(header=None, data_columns=data_columns, num_rows=num_rows)
            reader = csv.reader(io.StringIO(dsv), dialect="faker-csv")

            # Verify each row has correct number of columns
            for row in reader:
                assert len(row) == len(data_columns)

            # Verify correct number of lines read
            assert reader.line_num == num_rows

    def test_dsv_with_valid_header(self, faker, num_samples):
        header = ["Column 1", "Column 2"]
        data_columns = ["????", "?????"]
        for _ in range(num_samples):
            num_rows = faker.random.randint(1, 1000)
            dsv = faker.dsv(header=header, data_columns=data_columns, num_rows=num_rows)
            reader = csv.reader(io.StringIO(dsv), dialect="faker-csv")

            # Verify each row has correct number of columns
            for row in reader:
                assert len(row) == len(data_columns)

            # Verify correct number of lines read (additional header row)
            assert reader.line_num == num_rows + 1

    def test_dsv_with_row_ids(self, faker, num_samples):
        data_columns = ["????", "?????"]
        for _ in range(num_samples):
            counter = 0
            num_rows = faker.random.randint(1, 1000)
            dsv = faker.dsv(
                header=None,
                data_columns=data_columns,
                num_rows=num_rows,
                include_row_ids=True,
            )
            reader = csv.reader(io.StringIO(dsv), dialect="faker-csv")

            # Verify each row has correct number of columns
            # and row ids increment correctly
            for row in reader:
                assert len(row) == len(data_columns) + 1
                counter += 1
                assert row[0] == str(counter)

            # Verify correct number of lines read
            assert reader.line_num == num_rows

    def test_dsv_data_columns(self, faker):
        num_rows = 10
        data_columns = ["{{name}}", "#??-####", "{{address}}", "{{phone_number}}"]
        with patch.object(faker["en_US"].factories[0], "pystr_format") as mock_pystr_format:
            mock_pystr_format.assert_not_called()
            faker.dsv(data_columns=data_columns, num_rows=num_rows)

            # pystr_format will be called for each data column and each row
            calls = mock_pystr_format.call_args_list
            assert len(calls) == num_rows * len(data_columns)

            # Elements in data_columns will be used in sequence per row generation cycle
            column_cycle = itertools.cycle(data_columns)
            for args, kwargs in calls:
                assert args[0] == next(column_cycle)
                assert kwargs == {}

    def test_dsv_csvwriter_kwargs(self, faker):
        data_keys = ["header", "data_columns", "num_rows", "include_row_ids"]
        test_kwargs = {
            "dialect": "excel",
            "header": ["Column 1", "Column 2"],
            "data_columns": ["????", "?????"],
            "num_rows": 5,
            "include_row_ids": True,
            "delimiter": ";",
            "invalid_kwarg": "invalid_value",
        }
        with patch("faker.providers.misc.csv.writer") as mock_writer:
            mock_writer.assert_not_called()
            faker.dsv(**test_kwargs)
            assert mock_writer.call_count == 1

            # Remove all data generation kwargs
            for key in data_keys:
                del test_kwargs[key]

            # Verify csv.writer was called with the remaining kwargs
            for args, kwargs in mock_writer.call_args_list:
                assert kwargs == test_kwargs

    @unittest.skipUnless(xmltodict, "requires the Python xmltodict Library")
    def test_xml(self, faker):
        try:
            xml.etree.ElementTree.fromstring(faker.xml())
        except xml.etree.ElementTree.ParseError:
            raise AssertionError("The XML format is invalid.")

    def test_xml_no_xmltodict(self, faker):
        with patch.dict("sys.modules", {"xmltodict": None}):
            with pytest.raises(exceptions.UnsupportedFeature) as excinfo:
                faker.xml()

            assert excinfo.value.name == "xml"

    def test_csv_helper_method(self, faker):
        kwargs = {
            "header": ["Column 1", "Column 2"],
            "data_columns": ["????", "?????"],
            "num_rows": 5,
            "include_row_ids": True,
        }
        with patch("faker.providers.misc.Provider.dsv") as mock_dsv:
            mock_dsv.assert_not_called()
            faker.csv(**kwargs)
            kwargs["delimiter"] = ","
            mock_dsv.assert_called_once_with(**kwargs)

    def test_tsv_helper_method(self, faker):
        kwargs = {
            "header": ["Column 1", "Column 2"],
            "data_columns": ["????", "?????"],
            "num_rows": 5,
            "include_row_ids": True,
        }
        with patch("faker.providers.misc.Provider.dsv") as mock_dsv:
            mock_dsv.assert_not_called()
            faker.tsv(**kwargs)
            kwargs["delimiter"] = "\t"
            mock_dsv.assert_called_once_with(**kwargs)

    def test_psv_helper_method(self, faker):
        kwargs = {
            "header": ["Column 1", "Column 2"],
            "data_columns": ["????", "?????"],
            "num_rows": 5,
            "include_row_ids": True,
        }
        with patch("faker.providers.misc.Provider.dsv") as mock_dsv:
            mock_dsv.assert_not_called()
            faker.psv(**kwargs)
            kwargs["delimiter"] = "|"
            mock_dsv.assert_called_once_with(**kwargs)

    def test_json_with_arguments(self, faker_with_foobar):
        kwargs = {
            "data_columns": [
                ("item1", "{{ foo_bar:argument_group }}"),
                ("item2", "foo_bar", {"param": "BAZ"}),
            ],
            "num_rows": 1,
        }
        json_data = json.loads(faker_with_foobar.json(**kwargs))

        assert json_data.get("item1") == "FooBarBaz"
        assert json_data.get("item2") == "FooBarBAZ"

    def test_json_multiple_rows(self, faker_with_foobar):
        kwargs = {
            "data_columns": {"item": "foo_bar"},
            "num_rows": 2,
        }
        json_data = json.loads(faker_with_foobar.json(**kwargs))

        assert isinstance(json_data, list) and len(json_data) == 2

    def test_json_passthrough_values(self, faker_with_foobar):
        kwargs = {
            "data_columns": {
                "item1": 1,
                "item2": 1.0,
                "item3": True,
                "item4": "@fixed",
            },
            "num_rows": 1,
        }
        json_data = json.loads(faker_with_foobar.json(**kwargs))

        assert json_data["item1"] == 1
        assert json_data["item2"] == 1.0
        assert json_data["item3"] is True
        assert json_data["item4"] == "fixed"

    def test_json_type_integrity_int(self, faker_with_foobar):
        kwargs = {
            "data_columns": {
                "item1": "test_integer",
                "item2": "test_integer:double",
            },
            "num_rows": 1,
        }
        json_data = json.loads(faker_with_foobar.json(**kwargs))
        assert isinstance(json_data["item1"], int)
        assert json_data["item2"] == 2

    def test_json_type_integrity_float(self, faker_with_foobar):
        kwargs = {
            "data_columns": {
                "item1": "test_float",
                "item2": "test_float:double",
            },
            "num_rows": 1,
        }
        json_data = json.loads(faker_with_foobar.json(**kwargs))
        assert isinstance(json_data["item1"], float)
        assert json_data["item2"] == 2.2

    def test_json_invalid_data_columns(self, faker_with_foobar):
        kwargs = {
            "data_columns": (("item", "foo_bar"),),
            "num_rows": 1,
        }
        with pytest.raises(TypeError) as excinfo:
            json.loads(faker_with_foobar.json(**kwargs))
        assert str(excinfo.value) == "Invalid data_columns type. Must be a dictionary or list"

    def test_json_list_format_invalid_arguments_type(self, faker_with_foobar):
        kwargs = {
            "data_columns": [("item", "foo_bar", ["wrong"])],
            "num_rows": 1,
        }
        with pytest.raises(TypeError) as excinfo:
            faker_with_foobar.json(**kwargs)
        assert str(excinfo.value) == "Invalid arguments type. Must be a dictionary"

    def test_json_list_format_nested_list_of_values(self, faker_with_foobar):
        kwargs = {
            "data_columns": [
                (
                    "list",
                    [
                        (None, "{{ foo_bar }}s"),
                        (None, "foo_bar"),
                    ],
                ),
            ],
            "num_rows": 1,
        }
        json_data = json.loads(faker_with_foobar.json(**kwargs))

        assert json_data["list"][0] == "FooBars"
        assert json_data["list"][1] == "FooBar"

    def test_json_list_format_nested_list_of_objects(self, faker_with_foobar):
        kwargs = {
            "data_columns": [
                (
                    "list",
                    [
                        ("item", "{{ foo_bar }}s"),
                        ("item", "foo_bar"),
                    ],
                ),
            ],
            "num_rows": 1,
        }
        json_data = json.loads(faker_with_foobar.json(**kwargs))

        assert json_data["list"][0]["item"] == "FooBars"
        assert json_data["list"][1]["item"] == "FooBar"

    def test_json_list_format_nested_objects(self, faker_with_foobar):
        kwargs = {
            "data_columns": [
                (
                    "dict",
                    (
                        ("item1", "{{ foo_bar }}s"),
                        ("item2", "foo_bar"),
                    ),
                ),
            ],
            "num_rows": 1,
        }
        json_data = json.loads(faker_with_foobar.json(**kwargs))

        assert json_data["dict"]["item1"] == "FooBars"
        assert json_data["dict"]["item2"] == "FooBar"

    def test_json_dict_format_nested_list_of_values(self, faker_with_foobar):
        kwargs = {
            "data_columns": {
                "list": [
                    "{{ foo_bar }}s",
                    "foo_bar",
                ],
            },
            "num_rows": 1,
        }
        json_data = json.loads(faker_with_foobar.json(**kwargs))

        assert json_data["list"][0] == "FooBars"
        assert json_data["list"][1] == "FooBar"

    def test_json_dict_format_nested_list_of_objects(self, faker_with_foobar):
        kwargs = {
            "data_columns": {
                "list": [
                    {"item": "{{ foo_bar }}s"},
                    {"item": "foo_bar"},
                ],
            },
            "num_rows": 1,
        }
        json_data = json.loads(faker_with_foobar.json(**kwargs))

        assert json_data["list"][0]["item"] == "FooBars"
        assert json_data["list"][1]["item"] == "FooBar"

    def test_json_dict_format_nested_objects(self, faker_with_foobar):
        kwargs = {
            "data_columns": {
                "dict": {
                    "item1": "{{ foo_bar }}s",
                    "item2": "foo_bar",
                },
            },
            "num_rows": 1,
        }
        json_data = json.loads(faker_with_foobar.json(**kwargs))

        assert json_data["dict"]["item1"] == "FooBars"
        assert json_data["dict"]["item2"] == "FooBar"

    def test_json_type_integrity_datetime_using_encoder(self, faker_with_foobar):
        class DateTimeEncoder(json.JSONEncoder):
            def default(self, obj):
                if isinstance(obj, datetime.datetime):
                    return str(obj)

                # Let the base class default method raise the TypeError
                return json.JSONEncoder.default(self, obj)

        kwargs = {
            "data_columns": {"item1": "test_date_time"},
            "num_rows": 1,
            "cls": DateTimeEncoder,
        }
        json_data = json.loads(faker_with_foobar.json(**kwargs))
        assert isinstance(json_data["item1"], str)
        assert json_data["item1"] == "2022-12-22 13:42:33.000123"

    def test_json_type_integrity_datetime_no_encoder(self, faker_with_foobar):
        kwargs = {"data_columns": {"item1": "test_date_time"}, "num_rows": 1}
        with pytest.raises(TypeError):
            faker_with_foobar.json(**kwargs)

    def test_json_bytes(self, faker_with_foobar):
        kwargs = {"data_columns": {"item1": "foo_bar"}, "num_rows": 1}
        json_data_bytes = faker_with_foobar.json_bytes(**kwargs)
        assert isinstance(json_data_bytes, bytes)
        json_data = json.loads(json_data_bytes.decode())
        assert json_data["item1"] == "FooBar"

    def test_fixed_width_with_arguments(self, faker_with_foobar):
        kwargs = {
            "data_columns": [
                (9, "{{ foo_bar:argument_group }}"),
                (9, "foo_bar", {"param": "BAR"}),
            ],
            "num_rows": 2,
        }
        fixed_width_string = faker_with_foobar.fixed_width(**kwargs)

        for row in fixed_width_string.split("\n"):
            assert len(row) == 18
            assert row[0:9].strip() == "FooBarBaz"
            assert row[9:18].strip() == "FooBarBAR"

    def test_fixed_width_invalid_arguments_type(self, faker_with_foobar):
        kwargs = {
            "data_columns": [(9, "foo_bar", ["wrong"])],
            "num_rows": 1,
        }
        with pytest.raises(TypeError) as excinfo:
            faker_with_foobar.fixed_width(**kwargs)
        assert str(excinfo.value) == "Invalid arguments type. Must be a dictionary"

    def test_md5(self, faker):
        assert isinstance(faker.md5(), str)
        assert isinstance(faker.md5(raw_output=True), bytes)

    def test_sha1(self, faker):
        assert isinstance(faker.sha1(), str)
        assert isinstance(faker.sha1(raw_output=True), bytes)

    def test_sha256(self, faker):
        assert isinstance(faker.sha256(), str)
        assert isinstance(faker.sha256(raw_output=True), bytes)
    
    def test_password_length():
        pw = password(length=12)
        assert len(pw) == 12, "Password length should be 12"
    
    def test_password_special_chars():
        pw = password(special_chars=True, length=10)
        assert any(c in "!@#$%^&*()_+" for c in pw), "Password should contain at least one special character"
    
    def test_password_digits():
        pw = password(digits=True, length=10)
        assert any(c in string.digits for c in pw), "Password should contain at least one digit"
    
    def test_password_upper_case():
        pw = password(upper_case=True, length=10)
        assert any(c in string.ascii_uppercase for c in pw), "Password should contain at least one uppercase letter"
    
    def test_password_lower_case():
        pw = password(lower_case=True, length=10)
        assert any(c in string.ascii_lowercase for c in pw), "Password should contain at least one lowercase letter"
    
    def test_password_no_special_chars():
        pw = password(special_chars=False, length=10)
        assert all(c not in "!@#$%^&*()_+" for c in pw), "Password should not contain special characters"
    
    def test_password_all_requirements():
        pw = password(special_chars=True, digits=True, upper_case=True, lower_case=True, length=12)
        assert any(c in "!@#$%^&*()_+" for c in pw), "Password should contain at least one special character"
        assert any(c in string.digits for c in pw), "Password should contain at least one digit"
        assert any(c in string.ascii_uppercase for c in pw), "Password should contain at least one uppercase letter"
        assert any(c in string.ascii_lowercase for c in pw), "Password should contain at least one lowercase letter"
    
    def test_password_length_adjustment_for_required_characters():
        pw = password(special_chars=True, digits=True, length=4)
        assert len(pw) >= 6, "Password length should be at least 6 if multiple character types are required"
