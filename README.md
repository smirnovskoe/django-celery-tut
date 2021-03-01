# Django vs Celery

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things ...

```
Django
```

### Run Celery



```
celery -A core worker --pool=gevent --loglevel=info
celery -A core beat -l INFO
flower -A core
```

