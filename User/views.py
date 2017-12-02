from User.models import User
from base.common import save_user_to_session, logout_user_from_session
from base.decorator import require_params, require_json, require_post
from base.error import Error
from base.response import error_response, response


@require_json
@require_post
@require_params(['username', 'password'])
def create_user(request):
    username = request.POST['username']
    password = request.POST['password']

    ret = User.create(username, password)
    if ret.error != Error.OK:
        return error_response(ret.error)
    o_user = ret.body
    if not isinstance(o_user, User):
        return error_response(Error.STRANGE)

    return response(body=o_user.to_dict())


@require_json
@require_post
@require_params(['username', 'password'])
def user_login(request):
    username = request.POST['username']
    password = request.POST['password']

    ret = User.authenticate(username, password)
    if ret.error != Error.OK:
        return error_response(ret.error)
    o_user = ret.body
    if not isinstance(o_user, User):
        return error_response(Error.STRANGE)

    save_user_to_session(request, o_user)

    return response(body=o_user.to_dict())


@require_post
def user_logout(request):
    logout_user_from_session(request)
    return response()
