#!/bin/sh

sudo docker run -p 6379:6379 redis
celery -A worker.celery_app worker --loglevel=INFO -E
uvicorn main:app --reload
