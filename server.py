import logging.config

import cherrypy

import router
from config import Config
log = logging.getLogger("dashboard")
LOG_BUFFER_SIZE = 30
conf = None


class Root(object):
    @cherrypy.expose
    def index(self):
        return open('static/index.html')



def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"


@cherrypy.expose()
class BackupPolicyService(object):
    def __init__(self, conf):
        self.conf = conf
        self.router = router.APIRouter(conf)

    @cherrypy.tools.json_out()
    def GET(self, *args, **kwargs):
        result = self.router.dispatch(cherrypy.request)
        return result

    @cherrypy.tools.json_out()
    def POST(self, *args, **kwargs):
        result = self.router.dispatch(cherrypy.request)
        return result

    @cherrypy.tools.json_out()
    def PUT(self, *args, **kwargs):
        result = self.router.dispatch(cherrypy.request)
        return result

    @cherrypy.tools.json_out()
    def DELETE(self, *args, **kwargs):
        result = self.router.dispatch(cherrypy.request)
        return result

    def OPTIONS(self, *arg):
        cherrypy.response.headers['Access-Control-Allow-Methods'] = 'PUT, DELETE'
        cherrypy.response.headers['Access-Control-Allow-Headers'] = 'content-type'
        cherrypy.response.headers['Access-Control-Allow-Origin'] = '*'

conf = Config()
if __name__ == '__main__':
    config_path = 'server.conf'
    cherrypy.config.update(config_path)
    conf.update(config_path)
    root = Root()
    root.backup = BackupPolicyService(conf)
    cherrypy.tools.CORS = cherrypy.Tool('before_handler', CORS)
    cherrypy.tree.mount(root, '/', config_path)
    cherrypy.engine.start()
    cherrypy.engine.block()

