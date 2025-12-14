import json
import os
from pprint import pformat

_debug_as_dict = os.getenv("DEBUG")


def as_dict(result):
    x = result.as_dict()
    if _debug_as_dict:
        print("DEBUG DICT -> ", pformat(x))
        print("DEBUG JSON -> ", json.dumps(x, indent=2))
    return x
