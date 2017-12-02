from Study.views import create_study, run_study
from base.error import Error
from base.response import error_response


def rt_study(request):
    if request.method == "POST":
        return create_study(request)
    if request.method == "PUT":
        return run_study(request)
    return error_response(Error.ERROR_METHOD)


def rt_study_trail(request):
    # TODO: 接口有问题
    if request.method == "GET":
        pass
    pass