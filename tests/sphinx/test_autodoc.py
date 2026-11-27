from types import SimpleNamespace

from faker.sphinx import documentor
from faker.sphinx.autodoc import _create_source_files


def test_provider_docs_use_sphinx_source_directory(tmp_path, monkeypatch):
    monkeypatch.setattr(documentor, "STANDARD_PROVIDER_NAMES", ["faker.providers.address"])
    monkeypatch.setattr(documentor, "AVAILABLE_LOCALES", ["en_US"])
    _create_source_files(SimpleNamespace(srcdir=str(tmp_path)))

    assert (tmp_path / "providers.rst").is_file()
    assert (tmp_path / "providers" / "baseprovider.rst").is_file()
    assert (tmp_path / "providers" / "faker.providers.address.rst").is_file()
    assert (tmp_path / "locales.rst").is_file()
    assert (tmp_path / "locales" / "en_US.rst").is_file()
