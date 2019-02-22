import os
import sys
import pkgutil


def get_path(module):
    if getattr(sys, 'frozen', False):
        # frozen
        base_dir = os.path.dirname(sys.executable)
        lib_dir = os.path.join(base_dir, "lib")
        module_to_rel_path = os.path.join(*module.__package__.split("."))
        path = os.path.join(lib_dir, module_to_rel_path)
    else:
        # unfrozen
        path = os.path.dirname(os.path.realpath(module.__file__))
    return path


def list_module(module):
    path = get_path(module)
    modules = [name for _, name,
               is_pkg in pkgutil.iter_modules([path]) if is_pkg]
    return modules

