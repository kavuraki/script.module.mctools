# coding: utf-8
class Response:
    def __init__(self, text, status_code):
        self.text = text
        self.status_code = status_code


class Browser:
    def get(self, url=''):
        import httplib2
        h = httplib2.Http(disable_ssl_certificate_validation=True)
        resp, content = h.request(url, "GET")
        return Response(content, resp['status'])


browser = Browser()
response = browser.get("https://yts.ag")

print response.status_code
print response.text
