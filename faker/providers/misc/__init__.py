import csv
import hashlib
import io
import json
import re
import string
import tarfile
import uuid
import zipfile

from faker.exceptions import UnsupportedFeature

from .. import BaseProvider

localized = True

csv.register_dialect('faker-csv', csv.excel, quoting=csv.QUOTE_ALL)


class Provider(BaseProvider):

    def boolean(self, chance_of_getting_true=50):
        """Generate a random boolean value based on ``chance_of_getting_true``.

        :sample size=10: chance_of_getting_true=25
        :sample size=10: chance_of_getting_true=50
        :sample size=10: chance_of_getting_true=75
        """
        return self.generator.random.randint(1, 100) <= chance_of_getting_true

    def null_boolean(self):
        """Generate ``None``, ``True``, or ``False``, each with equal probability.

        :sample size=15:
        """
        return {
            0: None,
            1: True,
            -1: False,
        }[self.generator.random.randint(-1, 1)]

    def binary(self, length=(1 * 1024 * 1024)):
        """Generate a random binary blob of ``length`` bytes.

        :sample: length=64
        """
        blob = [self.generator.random.randrange(256) for _ in range(length)]
        return bytes(blob)

    def md5(self, raw_output=False):
        """Generate a random MD5 hash.

        If ``raw_output`` is ``False`` (default), a hexadecimal string representation of the MD5 hash
        will be returned. If ``True``, a ``bytes`` object representation will be returned instead.

        :sample: raw_output=False
        :sample: raw_output=True
        """
        res = hashlib.md5(str(self.generator.random.random()).encode())
        if raw_output:
            return res.digest()
        return res.hexdigest()

    def sha1(self, raw_output=False):
        """Generate a random SHA1 hash.

        If ``raw_output`` is ``False`` (default), a hexadecimal string representation of the SHA1 hash
        will be returned. If ``True``, a ``bytes`` object representation will be returned instead.

        :sample: raw_output=False
        :sample: raw_output=True
        """
        res = hashlib.sha1(str(self.generator.random.random()).encode())
        if raw_output:
            return res.digest()
        return res.hexdigest()

    def sha256(self, raw_output=False):
        """Generate a random SHA256 hash.

        If ``raw_output`` is ``False`` (default), a hexadecimal string representation of the SHA56 hash
        will be returned. If ``True``, a ``bytes`` object representation will be returned instead.

        :sample: raw_output=False
        :sample: raw_output=True
        """
        res = hashlib.sha256(
            str(self.generator.random.random()).encode())
        if raw_output:
            return res.digest()
        return res.hexdigest()

    def uuid4(self, cast_to=str):
        """Generate a random UUID4 object and cast it to another type if specified using a callable ``cast_to``.

        By default, ``cast_to`` is set to ``str``.

        May be called with ``cast_to=None`` to return a full-fledged ``UUID``.

        :sample:
        :sample: cast_to=None
        """
        # Based on http://stackoverflow.com/q/41186818
        generated_uuid = uuid.UUID(int=self.generator.random.getrandbits(128), version=4)
        if cast_to is not None:
            generated_uuid = cast_to(generated_uuid)
        return generated_uuid

    def password(
            self,
            length=10,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True):
        """Generate a random password of the specified ``length``.

        The arguments ``special_chars``, ``digits``, ``upper_case``, and ``lower_case`` control
        what category of characters will appear in the generated password. If set to ``True``
        (default), at least one character from the corresponding category is guaranteed to appear.
        Special characters are characters from ``!@#$%^&*()_+``, digits are characters from
        ``0123456789``, and uppercase and lowercase characters are characters from the ASCII set of
        letters.

        :sample: length=12
        :sample: length=40, special_chars=False, upper_case=False
        """
        choices = ""
        required_tokens = []
        if special_chars:
            required_tokens.append(
                self.generator.random.choice("!@#$%^&*()_+"))
            choices += "!@#$%^&*()_+"
        if digits:
            required_tokens.append(self.generator.random.choice(string.digits))
            choices += string.digits
        if upper_case:
            required_tokens.append(
                self.generator.random.choice(string.ascii_uppercase))
            choices += string.ascii_uppercase
        if lower_case:
            required_tokens.append(
                self.generator.random.choice(string.ascii_lowercase))
            choices += string.ascii_lowercase

        assert len(
            required_tokens) <= length, "Required length is shorter than required characters"

        # Generate a first version of the password
        chars = self.random_choices(choices, length=length)

        # Pick some unique locations
        random_indexes = set()
        while len(random_indexes) < len(required_tokens):
            random_indexes.add(
                self.generator.random.randint(0, len(chars) - 1))

        # Replace them with the required characters
        for i, index in enumerate(random_indexes):
            chars[index] = required_tokens[i]

        return ''.join(chars)

    def zip(self, uncompressed_size=65536, num_files=1, min_file_size=4096, compression=None):
        """Generate a bytes object containing a random valid zip archive file.

        The number and sizes of files contained inside the resulting archive can be controlled
        using the following arguments:

        - ``uncompressed_size`` - the total size of files before compression, 16 KiB by default
        - ``num_files`` - the number of files archived in resulting zip file, 1 by default
        - ``min_file_size`` - the minimum size of each file before compression, 4 KiB by default

        No compression is used by default, but setting ``compression`` to one of the values listed
        below will use the corresponding compression type.

        - ``'bzip2'`` or ``'bz2'`` for BZIP2
        - ``'lzma'`` or ``'xz'`` for LZMA
        - ``'deflate'``, ``'gzip'``, or ``'gz'`` for GZIP

        :sample: uncompressed_size=256, num_files=4, min_file_size=32
        :sample: uncompressed_size=256, num_files=32, min_file_size=4, compression='bz2'
        """
        if any([
            not isinstance(num_files, int) or num_files <= 0,
            not isinstance(min_file_size, int) or min_file_size <= 0,
            not isinstance(uncompressed_size, int) or uncompressed_size <= 0,
        ]):
            raise ValueError(
                '`num_files`, `min_file_size`, and `uncompressed_size` must be positive integers',
            )
        if min_file_size * num_files > uncompressed_size:
            raise AssertionError(
                '`uncompressed_size` is smaller than the calculated minimum required size',
            )
        if compression in ['bzip2', 'bz2']:
            compression = zipfile.ZIP_BZIP2
        elif compression in ['lzma', 'xz']:
            compression = zipfile.ZIP_LZMA
        elif compression in ['deflate', 'gzip', 'gz']:
            compression = zipfile.ZIP_DEFLATED
        else:
            compression = zipfile.ZIP_STORED

        zip_buffer = io.BytesIO()
        remaining_size = uncompressed_size
        with zipfile.ZipFile(zip_buffer, mode='w', compression=compression) as zip_handle:
            for file_number in range(1, num_files + 1):
                filename = self.generator.pystr() + str(file_number)

                max_allowed_size = remaining_size - (num_files - file_number) * min_file_size
                if file_number < num_files:
                    file_size = self.generator.random.randint(min_file_size, max_allowed_size)
                    remaining_size = remaining_size - file_size
                else:
                    file_size = remaining_size

                data = self.generator.binary(file_size)
                zip_handle.writestr(filename, data)
        return zip_buffer.getvalue()

    def tar(self, uncompressed_size=65536, num_files=1, min_file_size=4096, compression=None):
        """Generate a bytes object containing a random valid tar file.

        The number and sizes of files contained inside the resulting archive can be controlled
        using the following arguments:

        - ``uncompressed_size`` - the total size of files before compression, 16 KiB by default
        - ``num_files`` - the number of files archived in resulting zip file, 1 by default
        - ``min_file_size`` - the minimum size of each file before compression, 4 KiB by default

        No compression is used by default, but setting ``compression`` to one of the values listed
        below will use the corresponding compression type.

        - ``'bzip2'`` or ``'bz2'`` for BZIP2
        - ``'lzma'`` or ``'xz'`` for LZMA
        - ``'gzip'`` or ``'gz'`` for GZIP

        :sample: uncompressed_size=256, num_files=4, min_file_size=32
        :sample: uncompressed_size=256, num_files=32, min_file_size=4, compression='bz2'
        """
        if any([
            not isinstance(num_files, int) or num_files <= 0,
            not isinstance(min_file_size, int) or min_file_size <= 0,
            not isinstance(uncompressed_size, int) or uncompressed_size <= 0,
        ]):
            raise ValueError(
                '`num_files`, `min_file_size`, and `uncompressed_size` must be positive integers',
            )
        if min_file_size * num_files > uncompressed_size:
            raise AssertionError(
                '`uncompressed_size` is smaller than the calculated minimum required size',
            )
        if compression in ['gzip', 'gz']:
            mode = 'w:gz'
        elif compression in ['bzip2', 'bz2']:
            mode = 'w:bz2'
        elif compression in ['lzma', 'xz']:
            mode = 'w:xz'
        else:
            mode = 'w'

        tar_buffer = io.BytesIO()
        remaining_size = uncompressed_size
        with tarfile.open(mode=mode, fileobj=tar_buffer) as tar_handle:
            for file_number in range(1, num_files + 1):
                file_buffer = io.BytesIO()
                filename = self.generator.pystr() + str(file_number)

                max_allowed_size = remaining_size - (num_files - file_number) * min_file_size
                if file_number < num_files:
                    file_size = self.generator.random.randint(min_file_size, max_allowed_size)
                    remaining_size = remaining_size - file_size
                else:
                    file_size = remaining_size

                tarinfo = tarfile.TarInfo(name=filename)
                data = self.generator.binary(file_size)
                file_buffer.write(data)
                tarinfo.size = len(file_buffer.getvalue())
                file_buffer.seek(0)
                tar_handle.addfile(tarinfo, file_buffer)
                file_buffer.close()
        return tar_buffer.getvalue()

    def image(self, size=(256, 256), image_format='png', hue=None, luminosity=None):
        """Generate an image and draw a random polygon on it using the Python Image Library.
        Without it installed, this provider won't be functional. Returns the bytes representing
        the image in a given format.

        The argument ``size`` must be a 2-tuple containing (width, height) in pixels. Defaults to 256x256.

        The argument ``image_format`` can be any valid format to the underlying library like ``'tiff'``,
        ``'jpeg'``, ``'pdf'`` or ``'png'`` (default). Note that some formats need present system libraries
        prior to building the Python Image Library.
        Refer to https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html for details.

        The arguments ``hue`` and ``luminosity`` are the same as in the color provider and are simply forwarded to
        it to generate both the background and the shape colors. Therefore, you can ask for a "dark blue" image, etc.

        :sample size=2: size=(2, 2), hue='purple', luminosity='bright', image_format='pdf'
        :sample size=2: size=(16, 16), hue=[90,270], image_format='ico'
        """
        try:
            import PIL.Image
            import PIL.ImageDraw
        except ImportError:
            raise UnsupportedFeature("`image` requires the `Pillow` python library.", "image")

        (width, height) = size
        image = PIL.Image.new('RGB', size, self.generator.color(hue=hue, luminosity=luminosity))
        draw = PIL.ImageDraw.Draw(image)
        draw.polygon(
            [
                (self.random_int(0, width), self.random_int(0, height))
                for _ in range(self.random_int(3, 12))
            ],
            fill=self.generator.color(hue=hue, luminosity=luminosity),
            outline=self.generator.color(hue=hue, luminosity=luminosity),
        )
        with io.BytesIO() as fobj:
            image.save(fobj, format=image_format)
            fobj.seek(0)
            return fobj.read()

    def dsv(self, dialect='faker-csv', header=None,
            data_columns=('{{name}}', '{{address}}'),
            num_rows=10, include_row_ids=False, **fmtparams):
        """Generate random delimiter-separated values.

        This method's behavior share some similarities with ``csv.writer``. The ``dialect`` and
        ``**fmtparams`` arguments are the same arguments expected by ``csv.writer`` to control its
        behavior, and instead of expecting a file-like object to where output will be written, the
        output is controlled by additional keyword arguments and is returned as a string.

        The ``dialect`` argument defaults to ``'faker-csv'`` which is the name of a ``csv.excel``
        subclass with full quoting enabled.

        The ``header`` argument expects a list or a tuple of strings that will serve as the header row
        if supplied. The ``data_columns`` argument expects a list or a tuple of string tokens, and these
        string tokens will be passed to  :meth:`pystr_format() <faker.providers.python.Provider.pystr_format>`
        for data generation. Argument Groups are used to pass arguments to the provider methods.
        Both ``header`` and ``data_columns`` must be of the same length.

        Example:
            fake.set_arguments('top_half', {'min_value': 50, 'max_value': 100})
            fake.dsv(data_columns=('{{ name }}', '{{ pyint:top_half }}'))

        The ``num_rows`` argument controls how many rows of data to generate, and the ``include_row_ids``
        argument may be set to ``True`` to include a sequential row ID column.

        :sample: dialect='excel', data_columns=('{{name}}', '{{address}}')
        :sample: dialect='excel-tab', data_columns=('{{name}}', '{{address}}'), include_row_ids=True
        :sample: data_columns=('{{name}}', '{{address}}'), num_rows=5, delimiter='$'
        """

        if not isinstance(num_rows, int) or num_rows <= 0:
            raise ValueError('`num_rows` must be a positive integer')
        if not isinstance(data_columns, (list, tuple)):
            raise TypeError('`data_columns` must be a tuple or a list')
        if header is not None:
            if not isinstance(header, (list, tuple)):
                raise TypeError('`header` must be a tuple or a list')
            if len(header) != len(data_columns):
                raise ValueError('`header` and `data_columns` must have matching lengths')

        dsv_buffer = io.StringIO()
        writer = csv.writer(dsv_buffer, dialect=dialect, **fmtparams)

        if header:
            if include_row_ids:
                header = list(header)
                header.insert(0, 'ID')
            writer.writerow(header)

        for row_num in range(1, num_rows + 1):
            row = [self.generator.pystr_format(column) for column in data_columns]
            if include_row_ids:
                row.insert(0, str(row_num))

            writer.writerow(row)

        return dsv_buffer.getvalue()

    def csv(self, header=None, data_columns=('{{name}}', '{{address}}'), num_rows=10, include_row_ids=False):
        """Generate random comma-separated values.

        For more information on the different arguments of this method, please refer to
        :meth:`dsv() <faker.providers.misc.Provider.dsv>` which is used under the hood.

        :sample: data_columns=('{{name}}', '{{address}}'), num_rows=10, include_row_ids=False
        :sample: header=('Name', 'Address', 'Favorite Color'),
                data_columns=('{{name}}', '{{address}}', '{{safe_color_name}}'),
                num_rows=10, include_row_ids=True
        """
        return self.dsv(
            header=header, data_columns=data_columns, num_rows=num_rows,
            include_row_ids=include_row_ids, delimiter=',',
        )

    def tsv(self, header=None, data_columns=('{{name}}', '{{address}}'), num_rows=10, include_row_ids=False):
        """Generate random tab-separated values.

        For more information on the different arguments of this method, please refer to
        :meth:`dsv() <faker.providers.misc.Provider.dsv>` which is used under the hood.

        :sample: data_columns=('{{name}}', '{{address}}'), num_rows=10, include_row_ids=False
        :sample: header=('Name', 'Address', 'Favorite Color'),
                data_columns=('{{name}}', '{{address}}', '{{safe_color_name}}'),
                num_rows=10, include_row_ids=True
        """
        return self.dsv(
            header=header, data_columns=data_columns, num_rows=num_rows,
            include_row_ids=include_row_ids, delimiter='\t',
        )

    def psv(self, header=None, data_columns=('{{name}}', '{{address}}'), num_rows=10, include_row_ids=False):
        """Generate random pipe-separated values.

        For more information on the different arguments of this method, please refer to
        :meth:`dsv() <faker.providers.misc.Provider.dsv>` which is used under the hood.

        :sample: data_columns=('{{name}}', '{{address}}'), num_rows=10, include_row_ids=False
        :sample: header=('Name', 'Address', 'Favorite Color'),
                data_columns=('{{name}}', '{{address}}', '{{safe_color_name}}'),
                num_rows=10, include_row_ids=True
        """
        return self.dsv(
            header=header, data_columns=data_columns, num_rows=num_rows,
            include_row_ids=include_row_ids, delimiter='|',
        )

    def json(self,
             data_columns: list = None,
             num_rows: int = 10,
             indent: int = None) -> str:
        """
        Generate random JSON structure values.

        Using a dictionary or list of records that is passed as ``data_columns``,
        define the structure that is used to build JSON structures.  For complex
        data structures it is recommended to use the dictionary format.

        Data Column Dictionary format:
            {'key name': 'definition'}

        The definition can be 'provider', 'provider:argument_group', tokenized
        'string {{ provider:argument_group }}' that is passed to the python
        provider method pystr_format() for generation, or a fixed '@word'.
        Using Lists, Tuples, and Dicts as a definition for structure.

        Example:
            fake.set_arguments('top_half', {'min_value': 50, 'max_value': 100})
            fake.json(data_columns={'Name': 'name', 'Score': 'pyint:top_half'})

        Data Column List format:
            [('key name', 'definition', {'arguments'})]

        With the list format the definition can be a list of records, to create
        a list within the structure data.  For literal entries within the list,
        set the 'field_name' to None.

        :param data_columns: specification for the data structure
        :type data_columns: dict
        :param num_rows: number of rows the returned
        :type num_rows: int
        :param indent: number of spaces to indent the fields
        :type indent: int
        :return: Serialized JSON data
        :rtype: str

        :sample: data_columns={'Spec': '@1.0.1', 'ID': 'pyint',
                'Details': {'Name': 'name', 'Address': 'address'}}, num_rows=2
        :sample: data_columns={'Candidates': ['name', 'name', 'name']},
                num_rows=1
        :sample: data_columns=[('Name', 'name'), ('Points', 'pyint',
                {'min_value': 50, 'max_value': 100})], num_rows=1
        """
        default_data_columns = {
            'name': '{{name}}',
            'residency': '{{address}}',
        }
        data_columns = data_columns if data_columns else default_data_columns

        def process_list_structure(data: list) -> dict:
            entry = {}

            for name, definition, *arguments in data:
                kwargs = arguments[0] if arguments else {}

                if not isinstance(kwargs, dict):
                    raise TypeError('Invalid arguments type. Must be a dictionary')

                if name is None:
                    return self._value_format_selection(definition, **kwargs)

                if isinstance(definition, tuple):
                    entry[name] = process_list_structure(definition)
                elif isinstance(definition, (list, set)):
                    entry[name] = [process_list_structure([item])
                                   for item in definition]
                else:
                    entry[name] = self._value_format_selection(definition, **kwargs)
            return entry

        def process_dict_structure(data: dict) -> dict:
            entry = {}

            if isinstance(data, str):
                return self._value_format_selection(data)

            if isinstance(data, dict):
                for name, definition in data.items():
                    if isinstance(definition, (tuple, list, set)):
                        entry[name] = [process_dict_structure(item)
                                       for item in definition]
                    elif isinstance(definition, (dict, int, float, bool)):
                        entry[name] = process_dict_structure(definition)
                    else:
                        entry[name] = self._value_format_selection(definition)
                return entry

            return data

        def create_json_structure(data_columns) -> dict:
            if isinstance(data_columns, dict):
                return process_dict_structure(data_columns)

            if isinstance(data_columns, list):
                return process_list_structure(data_columns)

            raise TypeError('Invalid data_columns type. Must be a dictionary or list')

        if num_rows == 1:
            return json.dumps(create_json_structure(data_columns), indent=indent)

        data = [create_json_structure(data_columns) for _ in range(num_rows)]
        return json.dumps(data, indent=indent)

    def fixed_width(self,
                    data_columns: list = None,
                    num_rows: int = 10,
                    align: str = 'left') -> str:
        """
        Generate random fixed width values.

        Using a list of tuple records that is passed as ``data_columns``, that
        defines the structure that will be generated. Arguments within the
        record are provider specific, and should be a dictionary that will be
        passed to the provider method.

        Data Column List format
            [('field width', 'definition', {'arguments'})]

        The definition can be 'provider', 'provider:argument_group', tokenized
        'string {{ provider:argument_group }}' that is passed to the python
        provider method pystr_format() for generation, or a fixed '@word'.
        Using Lists, Tuples, and Dicts as a definition for structure.

        Argument Groups can be used to pass arguments to the provider methods,
        but will override the arguments supplied in the tuple record.

        Example:
            fake.set_arguments('top_half', {'min_value': 50, 'max_value': 100})
            fake.fixed_width(data_columns=[(20, 'name'), (3, 'pyint:top_half')])

        :param data_columns: specification for the data structure
        :type data_columns: list
        :param num_rows: number of rows the generator will yield
        :type num_rows: int
        :param align: positioning of the value. (left, middle, right)
        :type align: str
        :return: Serialized Fixed Width data
        :rtype: str

        :sample: data_columns=[(20, 'name'), (3, 'pyint', {'min_value': 50,
                'max_value': 100})], align='right', num_rows=2
        """
        default_data_columns = [
            (20, 'name'),
            (3, 'pyint', {'max_value': 20}),
        ]
        data_columns = data_columns if data_columns else default_data_columns
        align_map = {
            'left': '<',
            'middle': '^',
            'right': '>',
        }
        data = []

        for _ in range(num_rows):
            row = []

            for width, definition, *arguments in data_columns:
                kwargs = arguments[0] if arguments else {}

                if not isinstance(kwargs, dict):
                    raise TypeError('Invalid arguments type. Must be a dictionary')

                result = self._value_format_selection(definition, **kwargs)
                row.append(f'{result:{align_map.get(align, "<")}{width}}'[:width])

            data.append(''.join(row))
        return '\n'.join(data)

    def _value_format_selection(self, definition, **kwargs):
        """
        Formats the string in different ways depending on it's contents.

        The return can be the '@word' itself, a '{{ token }}' passed to PyStr,
        or a 'provider:argument_group' format field that returns potentially
        a non-string type.

        This ensures that Numbers, Boolean types that are generated in the
        JSON structures in there proper type, and not just strings.
        """

        # Check for PyStr first as complex strings may start with @
        if re.match(r'.*\{\{.*\}\}.*', definition):
            return self.generator.pystr_format(definition)

        # Check for fixed @words that won't be generated
        if re.match(r'^@.*', definition):
            return definition.lstrip('@')

        # Check if a argument group has been supplied
        if re.match(r'^[a-zA-Z0-9_-]*:\w', definition):
            definition, argument_group = definition.split(':')
            arguments = self.generator.get_arguments(argument_group.strip())

            return self.generator.format(definition.strip(), **arguments)

        # Assume the string is refering to a provider
        return self.generator.format(definition, **kwargs)
