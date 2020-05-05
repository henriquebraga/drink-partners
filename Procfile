web: gunicorn drink_partners:app --workers=$GUNICORN_WORKERS --bind unix:/app/drink-partners.sock --worker-class aiohttp.worker.GunicornUVLoopWebWorker -e SIMPLE_SETTINGS=$SIMPLE_SETTINGS


