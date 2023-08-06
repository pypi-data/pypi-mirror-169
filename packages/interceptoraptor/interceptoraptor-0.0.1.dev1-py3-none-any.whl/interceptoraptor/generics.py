"""
Not categorized API: utility, helpers ...
"""
import copy
import pickle
from inspect import signature
from typing import Any, Callable, Dict, Tuple

import requests


def custom_http_requests_pickle(response: requests.Response) -> bytes:
    """
    Request response may contain non pickle-able items inside
    to be safe we re-wrapp response into new response object:
    encoding, _content and status_code for requests.Response
    """
    # workaround for the bug for pickle requests.Response
    my_resp = requests.Response()
    my_resp.encoding = response.encoding
    my_resp._content = response._content  # pylint: disable=protected-access
    my_resp.status_code = response.status_code

    return pickle.dumps(my_resp)


def unify_args_to_kwargs(func: Callable[..., Any],
                         args: Tuple[Any],
                         kwargs: Dict[str, Any]) -> Dict[str, Any]:
    """
    Move input data from positional args into kwargs
    """
    sign = signature(func)
    parameters = dict(sign.parameters)
    for index, key in enumerate(parameters.keys()):
        value = args[index] if index < len(args) else kwargs.get(key, sign.parameters[key].default)
        parameters[key] = copy.deepcopy(value)

    return parameters
