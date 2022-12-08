def get_current_url_path(request):
    return request.META['HTTP_REFERER']
