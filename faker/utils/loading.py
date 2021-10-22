import pkgutil
import sys

from importlib import import_module
from pathlib import Path
from types import ModuleType
from typing import List


def get_path(module: ModuleType) -> str:
    if getattr(sys, "frozen", False):
        # frozen

        if getattr(sys, "_MEIPASS", False):
            # PyInstaller
            lib_dir = Path(getattr(sys, "_MEIPASS"))
        else:
            # others
            lib_dir = Path(sys.executable).parent / "lib"

        path = lib_dir.joinpath(*module.__package__.split("."))  # type: ignore
    else:
        # unfrozen
        path = Path(module.__file__).parent
    return str(path)


def list_module(module: ModuleType) -> List[str]:
    path = get_path(module)

    if getattr(sys, "_MEIPASS", False):
        # PyInstaller
        return [file.parent.name for file in Path(path).glob("*/__init__.py")]
    else:
        return [name for _, name, is_pkg in pkgutil.iter_modules([str(path)]) if is_pkg]


def find_available_locales(providers: List[str]) -> List[str]:
    available_locales = set()

    for provider_path in providers:

        provider_module = import_module(provider_path)
        if getattr(provider_module, "localized", False):
            langs = list_module(provider_module)
            available_locales.update(langs)
    return sorted(available_locales)


def find_available_providers(modules: List[ModuleType]) -> List[str]:
    available_providers = set()
    for providers_mod in modules:
        if providers_mod.__package__:
            providers = [
                ".".join([providers_mod.__package__, mod]) for mod in list_module(providers_mod) if mod != "__pycache__"
            ]
            available_providers.update(providers)
    return sorted(available_providers)
