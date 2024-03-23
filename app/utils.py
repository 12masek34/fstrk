import json

from core.settings import logger
from django.core.cache import cache


def get_request_id(request) -> str | None:
    """Получение request_id из тела запроса."""
    try:
        body = request.body.decode("utf-8")
        json_body = json.loads(body)
        logger.info(f"body: {json_body}")
        request_id = json_body.get("request_id")
    except Exception:
        request_id = None

    return request_id


def exists_from_cache(id_: str) -> str | None:
    """Проверка есть ли такой запос в кеше."""
    exists = cache.get(id_)
    logger.info(f"request_id={id_} {'exists in cache' if exists is not None else 'does not exists in cache'}")

    return exists


def set_to_cache(request_id: str, ttl: int = 5 * 60) -> None:
    """Запись запроса в кеш."""
    logger.info(f"set to cache request_id={request_id}")
    cache.set(request_id, "1", ttl)
