import web
from web.wsgiserver import CherryPyWSGIServer

urls = (
    '/', 'index'
)
uri = (
    '/', 'redirect'
)

class index:
    def GET(self):
        return "Hello, world!"
        
class redirect:
    def GET(self):
        raise web.seeother('0.0.0.0:443')     
        

class MyRedirect(web.application):
    def run(self, port=80, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))

if __name__ == "__main__":
    app = web.application(urls, globals())
    ssl_cert = '/etc/letsencrypt/live/maximefranco.be/cert.pem'
    ssl_key = '/etc/letsencrypt/live/maximefranco.be/privkey.pem'
    CherryPyWSGIServer.ssl_certificate = ssl_cert
    CherryPyWSGIServer.ssl_private_key = ssl_key
    app.run()
    redir = MyRedirect(uri,globals())
    redir.run()
