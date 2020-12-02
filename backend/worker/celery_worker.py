import asyncio

from celery import current_task
from celery.utils.log import get_task_logger


from .celery_app import celery_app

logger = get_task_logger(__name__)


@celery_app.task
def long_task(word: str) -> dict:
    logger.info("long_task called")
    asyncio.run(long_async_task())
    return {'result': word}


async def long_async_task():
    for i in range(10):
        await asyncio.sleep(1)
