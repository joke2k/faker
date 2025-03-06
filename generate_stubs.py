import inspect
import pathlib
import re

from collections import defaultdict
from typing import Any, Dict, List, Optional, Set, Tuple, Type, get_overloads, get_type_hints

import faker.proxy

from faker import Factory, Faker
from faker.config import AVAILABLE_LOCALES, PROVIDERS

BUILTIN_MODULES_TO_IGNORE = ["builtins"]
GENERIC_MANGLE_TYPES_TO_IGNORE = ["builtin_function_or_method", "mappingproxy"]
MODULES_TO_FULLY_QUALIFY = ["datetime"]


imports: Dict[str, Optional[Set[str]]] = defaultdict(lambda: None)
imports["collections"] = {"OrderedDict"}
imports["json"] = {"encoder"}
imports["typing"] = {"Callable", "Collection", "TypeVar", "overload"}
imports["uuid"] = {"UUID"}
imports["enum"] = {"Enum"}
imports["faker.typing"] = {"*"}
imports["faker.generator"] = {"Generator"}


def get_module_and_member_to_import(cls: Type, locale: Optional[str] = None) -> Tuple[str, str]:
    cls_name = getattr(cls, "__name__", getattr(cls, "_name", str(cls)))
    module, member = cls.__module__, cls_name
    if cls_name is None:
        qualified_type = re.findall(r"([a-zA-Z_0-9]+)\.([a-zA-Z_0-9]+)", str(cls))
        if len(qualified_type) > 0:
            if imports[qualified_type[0][0]] is None or qualified_type[0][1] not in imports[qualified_type[0][0]]:
                module, member = qualified_type[0]
        else:
            unqualified_type = re.findall(r"[^\.a-zA-Z0-9_]([A-Z][a-zA-Z0-9_]+)[^\.a-zA-Z0-9_]", f" {cls} ")
            if len(unqualified_type) > 0 and unqualified_type[0] != "NoneType":
                cls_str = str(cls).replace(".en_US", "").replace("faker.", ".")
                if "<class '" in cls_str:
                    cls_str = cls_str.split("'")[1]
                if locale is not None:
                    cls_str = cls_str.replace("." + locale, "")

                if imports[cls_str] is None or unqualified_type[0] not in imports[cls_str]:
                    module, member = cls_str, unqualified_type[0]
    if module in MODULES_TO_FULLY_QUALIFY:
        member = None
    return module, member


seen_funcs = set()
seen_vars = set()


class UniqueMemberFunctionsAndVariables:
    def __init__(self, cls: type, funcs: Dict[str, Any], vars: Dict[str, Any]):
        global seen_funcs, seen_vars
        self.cls = cls
        self.funcs = funcs
        for func_name in seen_funcs:
            self.funcs.pop(func_name, None)
        seen_funcs = seen_funcs.union(self.funcs.keys())

        self.vars = vars
        for var_name in seen_vars.union(seen_funcs):
            self.vars.pop(var_name, None)
        seen_vars = seen_vars.union(self.vars.keys())


def get_member_functions_and_variables(cls: object, include_mangled: bool = False) -> UniqueMemberFunctionsAndVariables:
    members = [
        (name, value)
        for (name, value) in inspect.getmembers(cls)
        if ((include_mangled and name.startswith("__")) or not name.startswith("_"))
    ]
    funcs: Dict[str, Any] = {}
    vars: Dict[str, Any] = {}
    for name, value in members:
        attr = getattr(cls, name, None)
        if attr is not None and (inspect.isfunction(attr) or inspect.ismethod(attr)):
            funcs[name] = value
        elif inspect.isgetsetdescriptor(attr) or inspect.ismethoddescriptor(attr):
            # I haven't implemented logic
            # for generating descriptor signatures yet
            continue
        elif not include_mangled or type(value).__name__ not in GENERIC_MANGLE_TYPES_TO_IGNORE:
            vars[name] = value

    return UniqueMemberFunctionsAndVariables(cls, funcs, vars)


def get_signatures_for_func(func_value, func_name, locale, is_overload: bool = False, comment: Optional[str] = None):
    """Return the signatures for the given function, recursing as necessary to handle overloads."""
    signatures = []

    if comment is None:
        comment = inspect.getdoc(func_value)

    if not is_overload:
        try:
            overloads = get_overloads(func_value)
        except Exception as e:
            raise TypeError(f"Can't parse overloads for {func_name}{sig}.") from e

        if overloads:
            for overload in overloads:
                signatures.extend(
                    get_signatures_for_func(overload, func_name, locale, is_overload=True, comment=comment)
                )
            return signatures

    sig = inspect.signature(func_value)
    try:
        hints = get_type_hints(func_value)
    except Exception as e:
        raise TypeError(f"Can't parse {func_name}{sig}.") from e
    ret_annot_module = getattr(sig.return_annotation, "__module__", None)
    if sig.return_annotation not in [
        None,
        inspect.Signature.empty,
        prov_cls.__name__,
    ] and ret_annot_module not in [
        None,
        *BUILTIN_MODULES_TO_IGNORE,
    ]:
        module, member = get_module_and_member_to_import(sig.return_annotation, locale)
        if module not in [None, "types"]:
            if imports[module] is None:
                imports[module] = set() if member is None else {member}
            elif member is not None:
                imports[module].add(member)

    new_parms = []
    for key, parm_val in sig.parameters.items():
        new_parm = parm_val
        annotation = hints.get(key, new_parm.annotation)
        if parm_val.default is not inspect.Parameter.empty:
            new_parm = parm_val.replace(default=...)
        if annotation is not inspect.Parameter.empty and annotation.__module__ not in BUILTIN_MODULES_TO_IGNORE:
            module, member = get_module_and_member_to_import(annotation, locale)
            if module not in [None, "types"]:
                if imports[module] is None:
                    imports[module] = set() if member is None else {member}
                elif member is not None:
                    imports[module].add(member)
        new_parms.append(new_parm)

    sig = sig.replace(parameters=new_parms)
    sig_str = str(sig).replace("Ellipsis", "...").replace("NoneType", "None").replace("~", "")
    for module in imports.keys():
        if module in MODULES_TO_FULLY_QUALIFY:
            continue
        sig_str = sig_str.replace(f"{module}.", "")

    decorator = ""
    if is_overload:
        decorator += "@overload\n"
    if list(sig.parameters)[0] == "cls":
        decorator += "@classmethod\n"
    elif list(sig.parameters)[0] != "self":
        decorator += "@staticmethod\n"
    signatures.append(
        (
            f"{decorator}def {func_name}{sig_str}: ...",
            None if comment == "" else comment,
            False,
        )
    )
    return signatures


classes_and_locales_to_use_for_stub: List[Tuple[object, str]] = []
for locale in AVAILABLE_LOCALES:
    for provider in PROVIDERS:
        if provider == "faker.providers":
            continue
        prov_cls, _, _ = Factory._find_provider_class(provider, locale)
        classes_and_locales_to_use_for_stub.append((prov_cls, locale))

all_members: List[Tuple[UniqueMemberFunctionsAndVariables, str]] = [
    (get_member_functions_and_variables(cls), locale) for cls, locale in classes_and_locales_to_use_for_stub
] + [(get_member_functions_and_variables(Faker, include_mangled=True), None)]

# Use the accumulated seen_funcs and seen_vars to remove all variables that have the same name as a function somewhere
overlapping_var_names = seen_vars.intersection(seen_funcs)
for mbr_funcs_and_vars, _ in all_members:
    for var_name_to_remove in overlapping_var_names:
        mbr_funcs_and_vars.vars.pop(var_name_to_remove, None)

# list of tuples. First elem of tuple is the signature string,
#  second is the comment string,
#  third is a boolean which is True if the comment precedes the signature
signatures_with_comments: List[Tuple[str, str, bool]] = []

for mbr_funcs_and_vars, locale in all_members:
    for func_name, func_value in mbr_funcs_and_vars.funcs.items():
        signatures_with_comments.extend(get_signatures_for_func(func_value, func_name, locale))

signatures_with_comments_as_str = []
for sig, comment, is_preceding_comment in signatures_with_comments:
    if comment is not None and is_preceding_comment:
        signatures_with_comments_as_str.append(f"# {comment}\n    {sig}")
    elif comment is not None:
        sig_without_final_ellipsis = sig.strip(" .")
        signatures_with_comments_as_str.append(
            sig_without_final_ellipsis + '\n    """\n    ' + comment.replace("\n", "\n    ") + '\n    """\n    ...'
        )
    else:
        signatures_with_comments_as_str.append(sig)


def get_import_str(module: str, members: Optional[Set[str]]) -> str:
    if members is None or len(members) == 0:
        return f"import {module}"
    else:
        return f"from {module} import {', '.join(members)}"


imports_block = "\n".join([get_import_str(module, names) for module, names in imports.items()])
member_signatures_block = "    " + "\n    ".join(
    [sig.replace("\n", "\n    ") for sig in signatures_with_comments_as_str]
)

body = f"""# This file is auto-generated by generate_stubs.py.
# Please do not edit this file directly.

{imports_block}

class Faker:
{member_signatures_block}
"""

faker_proxy_path = pathlib.Path(inspect.getfile(faker.proxy))
stub_file_path = faker_proxy_path.with_name("proxy.pyi").resolve()
with open(stub_file_path, "w", encoding="utf-8") as fh:
    fh.write(body)
