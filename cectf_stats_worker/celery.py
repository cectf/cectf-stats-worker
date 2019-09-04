from celery import Celery

app = Celery('cectf_stats_worker', broker='redis://localhost')

if __name__ == '__main__':
    app.start()
