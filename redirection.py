import web

urls = (
    '/', 'redirect',
    '/(.+)', 'redirect'
)

class redirect:
    def GET(self, id=None):
        raise web.seeother('https://www.maximefranco.be/')
        
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
