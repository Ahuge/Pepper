__author__ = 'Alex'
import os

_all_list = []
for mod in os.listdir(os.path.dirname(__file__)):
    mod, ext = os.path.splitext(mod)
    if mod != "__init__" and ext == ".py":
        check_mod = __import__(mod, globals(), locals(), ["main"])
        reload(check_mod)
        if hasattr(check_mod, "main"):
            _all_list.append(check_mod)

__all__ = _all_list
