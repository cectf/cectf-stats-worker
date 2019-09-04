from .celery import app


@app.task
def event(name, *args):
    print("Event %s occured: %s" % (name, args))
    return name, args
