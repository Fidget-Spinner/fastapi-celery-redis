# fastapi-celery-redis

A minimum viable example for a web application using FastAPI, Celery (using redis broker/results backend). It demonstrates concepts like polling the state/progress of a task, and configuring Redis.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required dependencies.

```bash
pip install -r requirements.txt
```

Conda works too but note that Redis is `redis-py` not `redis` used in pip.

## Usage
Run everything in `main.sh` in order. Then open `frontend/index.html`


## License
[MIT](https://choosealicense.com/licenses/mit/)
