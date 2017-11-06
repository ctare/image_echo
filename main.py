from bottle import *
import io
import os.path
import os
import requests

@get("/echo")
def echo():
    url = request.query.url
    b = io.BytesIO(requests.get(url).content).getvalue()
    res = HTTPResponse(status=200, body=b)
    res.set_header("Content-Type", "image/png")
    return res


@get("/")
def index():
    return "<p>/echo?url=&lt;image url&gt;</p>"


run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), reloader=True)
