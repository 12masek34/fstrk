import json
from core.settings import logger
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from .tasks import request_to_chatbot
from .utils import exists_from_cache, get_request_id, set_to_cache


@require_http_methods(["POST"])
def index(request):
    response = HttpResponse(b"", status=200)
    request_id = get_request_id(request)

    if request_id is not None and not exists_from_cache(request_id):
        method = request.method
        headers = dict(request.headers)
        body = json.loads(request.body)
        url = "https://httpbin.org/post"
        task = request_to_chatbot.delay(method, url, headers, body)
        response["X-Celery-ID"] = task.id
        set_to_cache(request_id)
        logger.info(f"create task: {task.id}")

    return response
