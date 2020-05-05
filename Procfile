web: gunicorn drink_partners:app --workers=$GUNICORN_WORKERS -b 0.0.0.0:$PORT --worker-class aiohttp.worker.GunicornUVLoopWebWorker -e SIMPLE_SETTINGS=drink_partners.settings.production


