# fastapi-celery-redis

A minimum viable example for a web application using FastAPI, Celery 
(using redis broker/results backend). It demonstrates concepts like polling 
the state/progress of a task, and configuring Celery. It also shows how to run
as basic async task.

## Installation

Use the package manager [conda](https://docs.conda.io/en/latest/) or 
[miniconda](https://docs.conda.io/en/latest/miniconda.html) to install 
required dependencies.

```bash
conda install --file requirements.txt
```

## Usage
Run everything in `main.sh` in order. Then open `frontend/index.html` to test
it out.


## License
[MIT](https://choosealicense.com/licenses/mit/)
