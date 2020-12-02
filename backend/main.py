from __future__ import annotations
from typing import TYPE_CHECKING

import celery.states
from celery.result import AsyncResult
from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware

from worker.celery_app import celery_app
from worker.celery_worker import long_task

if TYPE_CHECKING:
    from celery import Task
    long_task: Task

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/{word}")
async def root(word: str):
    task_name = "worker.celery_worker.long_task"
    # task = long_task.apply_async(args=[word])
    task = celery_app.send_task(task_name, args=[word])
    # background_task.add_task(background_on_message, task)

    return {"task_id": task.id}


@app.get("/api/{task_id}/status")
async def status(task_id: str) -> dict:
    res = AsyncResult(task_id)
    if res.state == celery.states.SUCCESS:
        return {'state': celery.states.SUCCESS,
                'result': res.result}
    return {'state': res.state, }
