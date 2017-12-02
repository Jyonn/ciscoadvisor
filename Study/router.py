from base.error import Error
from base.response import error_response


def rt_study(request):
    if request.method == "POST":
        return create_study(request)
    return error_response(Error.ERROR_METHOD)
