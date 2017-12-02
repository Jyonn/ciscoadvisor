from Algorithm.models import Algorithm
from Study.models import Study
from User.models import User
from base.common import get_user_from_session
from base.decorator import require_post, require_json, require_params, require_login
from base.response import response, error_response
from base.error import Error
from gRPCapi.suggestion import suggestion_client


@require_json
@require_post
@require_params(['config', 'algo_id', 'client_ip', 'client_port'])
@require_login
def create_study(request):
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


@require_json
@require_post
@require_params(['study_id'])
def run_study(request):
    study_id = request.POST['study_id']

    ret = get_user_from_session(request)
    if ret.error is not Error.OK:
        return error_response(ret.error)
    o_user = ret.body
    if not isinstance(o_user, User):
        return error_response(Error.STRANGE)

    ret = Study.get_study_by_id(study_id)
    if ret.error is not Error.OK:
        return error_response(ret.error)
    o_study = ret.body
    if not isinstance(o_study, Study):
        return error_response(Error.STRANGE)

    if o_study.status is not Study.STATUS_READY:
        return error_response(Error.STUDY_IS_RUNNING)
    o_study.status = Study.STATUS_RUNNING
    o_study.save()

    ret = suggestion_client.run('ALGO_IP', 'ALGO_PORT', o_study.pk)
    if ret.error is not Error.OK:
        return error_response(ret.error)
    return response(body=ret.body)
