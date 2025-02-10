#!/usr/bin/env python

from pathlib import Path

from setuptools import find_packages, setup

here = Path(__file__).resolve().parent
README = (here / "README.rst").read_text(encoding="utf-8")
VERSION = (here / "VERSION").read_text(encoding="utf-8").strip()

excluded_packages = ["docs", "tests", "tests.*"]


# this module can be zip-safe if the zipimporter implements iter_modules or if
# pkgutil.iter_importer_modules has registered a dispatch for the zipimporter.
try:
    import pkgutil
    import zipimport

    zip_safe = (
        hasattr(zipimport.zipimporter, "iter_modules")
        or zipimport.zipimporter in pkgutil.iter_importer_modules.registry.keys()
    )
except AttributeError:
    zip_safe = False

extra_test = [
    "coverage>=5.2",
    "freezegun",
    "pytest>=6.0.1",
    "ukpostcodeparser>=1.1.1",
    "validators>=0.13.0",
    "sphinx>=2.4,<3.0",
    "Pillow",
    "xmltodict",
]
extra_flake8 = ["flake8>=4.0.0", "flake8-comprehensions"]
extra_check_manifest = ["check-manifest"]
extra_isort = ["isort"]
extra_mypy = ["mypy==1.14.1"]
extra_black = ["black==24.4.0"]
extra_doc8 = ["doc8"]
extra_dev = list(
    set(extra_test + extra_flake8 + extra_check_manifest + extra_isort + extra_mypy + extra_black + extra_doc8)
)

setup(
    name="Faker",
    version=VERSION,
    description="Faker is a Python package that generates fake data for you.",
    long_description=README,
    entry_points={
        "console_scripts": ["faker=faker.cli:execute_from_command_line"],
        "pytest11": ["faker = faker.contrib.pytest.plugin"],
    },
    classifiers=[
        # See https://pypi.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="faker fixtures data test mock generator",
    author="joke2k",
    author_email="joke2k@gmail.com",
    url="https://github.com/joke2k/faker",
    project_urls={
        "Bug Tracker": "https://github.com/joke2k/faker/issues",
        "Changes": "https://github.com/joke2k/faker/blob/master/CHANGELOG.md",
        "Documentation": "http://faker.rtfd.org/",
        "Source Code": "https://github.com/joke2k/faker",
    },
    license="MIT License",
    packages=find_packages(exclude=excluded_packages),
    package_data={
        "faker": ["py.typed", "proxy.pyi"],
    },
    platforms=["any"],
    zip_safe=zip_safe,
    python_requires=">=3.9",
    install_requires=[
        "python-dateutil>=2.4",
    ],
    extras_require={
        "test": extra_test,
        "flake8": extra_flake8,
        "check-manifest": extra_check_manifest,
        "isort": extra_isort,
        "mypy": extra_mypy,
        "black": extra_black,
        "doc8": extra_doc8,
        "dev": extra_dev,
    },
)
