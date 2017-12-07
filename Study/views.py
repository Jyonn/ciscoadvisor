import json

from Algorithm.models import Algorithm, AlgoServer
from Study.models import Study, Trail
from User.models import User
from base.common import get_user_from_session
from base.decorator import require_post, require_json, require_params, require_login
from base.response import response, error_response, Ret
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
    if not isinstance(o_study, Study):
        return Ret(Error.STRANGE)

    if o_study.status == Study.STATUS_PAUSED:
        return Ret(Error.STUDY_PAUSED)
    # select a proper server for running
    ret = AlgoServer.choose_server()
    if ret.error is not Error.OK:
        return Ret(ret.error)
    o_server = ret.body
    if not isinstance(o_server, AlgoServer):
        return Ret(Error.STRANGE)
    # run a study
    ret = suggestion_client.run(o_server.ip, o_server.port, o_study.pk)
    if ret.error is not Error.OK:
        return error_response(ret.error)
    return Ret(Error.OK, ret.body)


@require_json
@require_post
@require_params(['study_id'])
@require_login
def pause_study(request):
    study_id = request.POST['study_id']

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
        return error_response(Error.NO_RIGHT_MODIFY_STUDY)

    if o_study.status not in [Study.STATUS_RUNNING]:
        return error_response(Error.STUDY_IS_NOT_RUNNING)
    o_study.status = Study.STATUS_PAUSED
    o_study.save()

    return response(body=o_study.to_dict())


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
        return error_response(Error.NO_RIGHT_MODIFY_STUDY)

    # check study status
    if o_study.status not in [Study.STATUS_READY, Study.STATUS_PAUSED]:
        return error_response(Error.STUDY_IS_RUNNING_OR_FINISHED)
    o_study.status = Study.STATUS_RUNNING
    o_study.save()

    ret = select_and_run(o_study)
    if ret.error is not Error.OK:
        o_study.status = Study.STATUS_PAUSED
        o_study.save()
        return error_response(ret.error)
    return response(body=ret.body)


@require_json
@require_post
@require_params(['trail', 'study_id'])
def ask_for_trail(request):
    trail = request.POST['trail']
    study_id = request.POST['study_id']
    print(trail, study_id)

    # get study by id
    ret = Study.get_study_by_id(study_id)
    if ret.error is not Error.OK:
        return error_response(ret.error)
    o_study = ret.body
    if not isinstance(o_study, Study):
        return error_response(Error.STRANGE)

    o_study.finish_epoch()
    if o_study.status == Study.STATUS_FINISH:
        return error_response(Error.FINISHED)
    trail_str = json.dumps(trail, ensure_ascii=False)

    ret = Trail.create(o_study, trail_str)
    if ret.error is not Error.OK:
        return error_response(ret.error)
    o_trail = ret.body
    if not isinstance(o_trail, Trail):
        return error_response(Error.STRANGE)

    ret = trail_client.run(o_study.client_ip, o_study.client_port, trail_str, o_trail.pk)
    if ret.error is not Error.OK:
        return error_response(ret.error)
    return response(body=ret.body)


@require_json
@require_post
@require_params(['trail_id', 'metric'])
def reply_to_trail(request):
    trail_id = request.POST['trail_id']
    metric = request.POST['metric']
    # study_id = request.POST['study_id']

    # # get study by id
    # ret = Study.get_study_by_id(study_id)
    # if ret.error is not Error.OK:
    #     return error_response(ret.error)
    # o_study = ret.body
    # if not isinstance(o_study, Study):
    #     return error_response(Error.STRANGE)

    # get trail by id
    ret = Trail.get_trail_by_id(trail_id)
    if ret.error is not Error.OK:
        return error_response(ret.error)
    o_trail = ret.body
    if not isinstance(o_trail, Trail):
        return error_response(Error.STRANGE)

    o_study = o_trail.r_study

    metric_str = json.dumps(metric, ensure_ascii=False)
    o_trail.set_metric(metric_str)

    ret = select_and_run(o_study)
    if ret.error is not Error.OK:
        return error_response(ret.error)
    return response(body=ret.body)
