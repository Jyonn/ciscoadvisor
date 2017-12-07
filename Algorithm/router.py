from Algorithm.views import get_algo_list, create_algo
from base.error import Error
from base.response import error_response


def rt_algo(request):
    if request.method == "GET":
        return get_algo_list(request)
    if request.method == "POST":
        return create_algo(request)
    return error_response(Error.ERROR_METHOD)
