from Algorithm.models import Algorithm
from base.decorator import require_get
from base.error import Error
from base.response import response, error_response


@require_get
def get_algo_list(request):
    ret = Algorithm.get_algo_list()
    if ret.error is not Error.OK:
        return error_response(ret.error)
    algo_list = ret.body

    return response(body=algo_list)
