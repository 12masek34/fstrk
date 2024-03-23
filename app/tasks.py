from core.celery import app
from core.settings import logger
from requests import request


@app.task(rate_limit="8/s")
def request_to_chatbot(method, url, headers, json):
    id_celery_task = request_to_chatbot.request.id
    headers["X-Celery-ID"] = id_celery_task
    logger.info(f"methond={method}\nurl={url}\nheaders={headers}\nbody={json}\n")
    response = request(method=method, url=url, headers=headers, json=json)
    logger.info(f"response status_code={response.status_code}")
