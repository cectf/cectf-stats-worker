#!/bin/sh

source venv/bin/activate
celery -A topkek_stats_worker worker --loglevel=info
