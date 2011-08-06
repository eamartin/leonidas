from werkzeug.wrappers import Request, Response

class Leonidas(object):

    def configure(self, config):
        pass
    
    def dispatch_request(self, request):
        return Response('Hello World')

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, *args, **kwargs):
        return self.wsgi_app(*args, **kwargs)


def create_app(app_class, config=None):
    if config is None:
        config = {}        
    app = app_class()
    app.configure(config)
    return app


def main(host='0.0.0.0', port=5000):
    from werkzeug.serving import run_simple
    app = create_app(Leonidas)
    run_simple(host, port, app, use_debugger=True, use_reloader=True)

if __name__ == '__main__':
    main()

        
    
