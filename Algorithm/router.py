from Algorithm.views import get_algo_list


def rt_algo(request):
    if request.method == "GET":
        return get_algo_list(request)
