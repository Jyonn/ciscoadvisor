from functools import wraps

from django.views.decorators import http

from base.common import get_user_from_session
from base.response import *

require_post = http.require_POST
require_get = http.require_GET


def require_params(r_params):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            for require_param in r_params:
                if require_param not in request.POST:
                    return error_response(Error.REQUIRE_PARAM, append_msg=require_param)
            return func(request, *args, **kwargs)
        return wrapper
    return decorator


def require_get_params(r_params):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            for require_param in r_params:
                if require_param not in request.GET:
                    return error_response(Error.REQUIRE_PARAM, append_msg=require_param)
            return func(request, *args, **kwargs)
        return wrapper
    return decorator


def require_json(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.body:
            try:
                request.POST = json.loads(request.body.decode())
            except:
                pass
            return func(request, *args, **kwargs)
        else:
            return error_response(Error.REQUIRE_JSON)

    return wrapper


def decorator_generator(verify_func, error_id):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            if verify_func(request):
                return func(request, *args, **kwargs)
            return error_response(error_id)
        return wrapper
    return decorator


def require_login_func(request):
    o_user = get_user_from_session(request)
    return o_user is not None

require_login = decorator_generator(require_login_func, Error.REQUIRE_LOGIN)
