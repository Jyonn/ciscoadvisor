from Study.views import create_study, run_study, ask_for_trail, reply_to_trail, pause_study
from base.error import Error
from base.response import error_response


def rt_study(request):
    if request.method == "POST":
        return create_study(request)
    return error_response(Error.ERROR_METHOD)


def rt_study_run(request):
    if request.method == "POST":
        return run_study(request)
    return error_response(Error.ERROR_METHOD)


def rt_study_pause(request):
    if request.method == "POST":
        return pause_study(request)
    return error_response(Error.ERROR_METHOD)


def rt_study_trail_req(request):
    if request.method == "POST":
        # algoserver want to get trail from client
        return ask_for_trail(request)
    return error_response(Error.ERROR_METHOD)


def rt_study_trail_resp(request):
    if request.method == "POST":
        return reply_to_trail(request)
    return error_response(Error.ERROR_METHOD)