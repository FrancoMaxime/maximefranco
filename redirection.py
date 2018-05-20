import web

urls = (
    '/', 'redirect',
    '/(.+)', 'redirect'
)

class index:
    def GET(self, id=None):
        raise web.seeother('0.0.0.0:443/')
        
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
