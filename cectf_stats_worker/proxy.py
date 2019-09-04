

from .celery import app


def request(req):
    print("REQUESTO")
    print(dir(req))
    args = [
        req.method,
        req.url,
        [k for k in req.headers.items()],
        req.cookies
    ]
    if req.is_json:
        args += [req.json]
    return _request_task.delay(*args)


@app.task
def _request_task(method, url, headers, cookies, json=None):
    print("Requesting %s %s" % (method, url))
    print("Headers %s" % headers)
    print("Cookies %s" % cookies)
    if json:
        print("JSON %s" % json)
    return (method, url, headers, cookies, json)


def response(resp):
    args = [resp.status_code]
    if resp.headers['Content-Type'] == "application/json":
        args += [resp.json()]
    return _response_task.delay(*args)


@app.task
def _response_task(status_code, json=None):
    print("Responsing %s" % status_code)
    if json:
        print("JSON %s" % json)
    return (status_code, json)
