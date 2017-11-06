from bottle import *
import io
import os.path
import requests

@get("/echo")
def echo():
    url = request.query.url
    b = io.BytesIO(requests.get(url).content).getvalue()
    res = HTTPResponse(status=200, body=b)
    res.set_header("Content-Type", "image/png")
    return res


run(host="0.0.0.0", port=5000, reloader=True)
