#!/bin/sh

source venv/bin/activate
celery -A cectf_stats_worker worker --loglevel=info
