from ..resource_dir.requests import get_page_data


def users_response(request):
    endpoint = request.cls.ENDPOINT
    return get_page_data(endpoint)
