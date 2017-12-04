import json

from Algorithm.models import Algorithm, AlgoServer
from Study.models import Study, Trail
from User.models import User
from base.common import get_user_from_session
from base.decorator import require_post, require_json, require_params, require_login
from base.response import response, error_response
from base.error import Error
from gRPCapi.suggestion import suggestion_client
from gRPCapi.trail import trail_client


@require_json
@require_post
@require_params(['config', 'algo_id', 'client_ip', 'client_port'])
@require_login
def create_study(request):
    """
    client ask server to create a study for running
    """
    config = request.POST['config']
    algo_id = request.POST['algo_id']
    c_ip = request.POST['client_ip']
    c_port = request.POST['client_port']

    ret = get_user_from_session(request)
    if ret.error is not Error.OK:
        return error_response(ret.error)
    o_user = ret.body
    if not isinstance(o_user, User):
        return error_response(Error.STRANGE)

    ret = Algorithm.get_algo_by_id(algo_id)
    if ret.error is not Error.OK:
        return error_response(ret.error)
    o_algo = ret.body
    if not isinstance(o_algo, Algorithm):
        return error_response(Error.STRANGE)

    ret = Study.create(o_user, o_algo, config, c_ip, c_port)
    if ret.error is not Error.OK:
        return error_response(ret.error)
    o_study = ret.body
    if not isinstance(o_study, Study):
        return error_response(Error.STRANGE)

    return response(body=o_study.to_dict())


def select_and_run(o_study):
    # select a proper server for running
    ret = AlgoServer.choose_server()
    if ret.error is not Error.OK:
        return error_response(ret.error)
    o_server = ret.body
    if not isinstance(o_server, AlgoServer):
        return error_response(Error.STRANGE)

    # run a study
    return suggestion_client.run(o_server.ip, o_server.port, o_study.pk)


@require_json
@require_post
@require_params(['study_id'])
@require_login
def run_study(request):
    """
    client ask server to run a study
    """
    study_id = request.POST['study_id']

    # get user from session
    ret = get_user_from_session(request)
    if ret.error is not Error.OK:
        return error_response(ret.error)
    o_user = ret.body
    if not isinstance(o_user, User):
        return error_response(Error.STRANGE)

    # get study from study_id
    ret = Study.get_study_by_id(study_id)
    if ret.error is not Error.OK:
        return error_response(ret.error)
    o_study = ret.body
    if not isinstance(o_study, Study):
        return error_response(Error.STRANGE)

    # check study belongs to user
    if not o_study.belong(o_user):
        return error_response(Error.NO_RIGHT_RUN_STUDY)

    # check study status
    if o_study.status is not Study.STATUS_READY:
        return error_response(Error.STUDY_IS_RUNNING)
    o_study.status = Study.STATUS_RUNNING
    o_study.save()

    ret = select_and_run(o_study)
    if ret.error is not Error.OK:
        return error_response(ret.error)
    return response(body=ret.body)


@require_json
@require_post
@require_params(['trail', 'study_id'])
def ask_for_trail(request):
    trail = request.POST['trail']
    study_id = request.POST['study_id']

    # get study by id
    ret = Study.get_study_by_id(study_id)
    if ret.error is not Error.OK:
        return error_response(ret.error)
    o_study = ret.body
    if not isinstance(o_study, Study):
        return error_response(Error.STRANGE)

    trail_str = json.dumps(trail, ensure_ascii=False)
    ret = trail_client.run(o_study.client_ip, o_study.client_port, trail_str)
    if ret.error is not Error.OK:
        return error_response(ret.error)
    return response(body=ret.body)


@require_json
@require_post
@require_params(['trail', 'study_id', 'metric'])
def reply_to_trail(request):
    trail = request.POST['data']
    metric = request.POST['metric']
    study_id = request.POST['study_id']

    # get study by id
    ret = Study.get_study_by_id(study_id)
    if ret.error is not Error.OK:
        return error_response(ret.error)
    o_study = ret.body
    if not isinstance(o_study, Study):
        return error_response(Error.STRANGE)

    trail_str = json.dumps(trail, ensure_ascii=False)
    metric_str = json.dumps(metric, ensure_ascii=False)
    ret = Trail.create(o_study, trail_str, metric_str)
    if ret.error is not Error.OK:
        return error_response(ret.error)

    ret = select_and_run(o_study)
    if ret.error is not Error.OK:
        return error_response(ret.error)
    return response(body=ret.body)
