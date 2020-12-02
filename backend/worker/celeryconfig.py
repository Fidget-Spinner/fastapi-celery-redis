## Broker settings.
broker_url = 'redis://127.0.0.1:6379/0'

# List of modules to import when the Celery worker starts.
imports = ('worker.celery_worker',)

## Using the database to store task state and results.
result_backend = 'redis://127.0.0.1:6379/0'

task_annotations = {'tasks.add': {'rate_limit': '10/s'}}

task_queues = {
    'test-queue': {
        'exchange': 'test-queue',
    }
}
task_routes = {
    "worker.celery_worker.long_task": "test-queue"
}
task_track_started = True

worker_concurrency = 1
worker_prefetch_multiplier = 3
worker_max_tasks_per_child = 10000
