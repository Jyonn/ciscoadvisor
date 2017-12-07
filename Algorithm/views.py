from Algorithm.models import Algorithm, AlgoServer
from User.models import User
from base.common import get_user_from_session
from base.decorator import require_get, require_json, require_post, require_params, require_login
from base.error import Error
from base.response import response, error_response, Ret
from gRPCapi.suggestion import suggestion_client


def select_and_create(o_algo):
    if not isinstance(o_algo, Algorithm):
        return Ret(Error.STRANGE)
    # select a proper server for running
    ret = AlgoServer.choose_server()
    if ret.error is not Error.OK:
        return Ret(ret.error)
    o_server = ret.body
    if not isinstance(o_server, AlgoServer):
        return Ret(Error.STRANGE)
    # run a study
    ret = suggestion_client.create_algo(o_server.ip, o_server.port, o_algo.aname, o_algo.path)
    if ret.error is not Error.OK:
        return error_response(ret.error)
    return Ret(Error.OK, ret.body)


@require_get
def get_algo_list(request):
    ret = Algorithm.get_algo_list()
    if ret.error is not Error.OK:
        return error_response(ret.error)
    algo_list = ret.body

    return response(body=algo_list)


@require_json
@require_post
@require_params(['algo_name', 'algo_path'])
@require_login
def create_algo(request):
    algo_name = request.POST['algo_name']
    algo_path = request.POST['algo_path']

    ret = get_user_from_session(request)
    if ret.error is not Error.OK:
        return error_response(ret.error)
    o_user = ret.body
    if not isinstance(o_user, User):
        return error_response(Error.STRANGE)

    ret = Algorithm.create(algo_name, algo_path)
    if ret.error is not Error.OK:
        return error_response(ret.error)
    o_algo = ret.body
    if not isinstance(o_algo, Algorithm):
        return error_response(Error.STRANGE)

    ret = select_and_create(o_algo)
    if ret.error is not Error.OK:
        return error_response(ret.error)

    return response(body=ret.body)
