from filters.common import filter_query_params


def post_filter(request, query):
    allowed = {
        'user': lambda x: int(x),
    }
    return filter_query_params(allowed, query, request)
