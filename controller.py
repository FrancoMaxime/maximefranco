import web
from web.wsgiserver import CherryPyWSGIServer

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        return "Hello, world!"

if __name__ == "__main__":
    app = web.application(urls, globals())
    ssl_cert = '/etc/letsencrypt/live/maximefranco.be/cert.pem'
    ssl_key = '/etc/letsencrypt/live/maximefranco.be/privkey.pem'
    CherryPyWSGIServer.ssl_certificate = ssl_cert
    CherryPyWSGIServer.ssl_private_key = ssl_key
    app.run()
