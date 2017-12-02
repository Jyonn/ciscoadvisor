from User.views import create_user

from base.error import Error
from base.response import error_response


def rt_user(request):
    if request.method == 'POST':
        return create_user(request)
    return error_response(Error.ERROR_METHOD)
