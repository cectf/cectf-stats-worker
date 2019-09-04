from celery import Celery

app = Celery('cectf_stats_worker', broker='redis://localhost')


@app.task
def logitin(*args):
    print("Logging in", args)
    return args


@app.task
def logitout(*args):
    print("Logging out", args)
    return args
