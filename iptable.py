import os

#os.system("some_command with args")
#os.system("iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 443 -j DNAT --to-destination 10.0.0.1:443")
#os.system("iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 80 -j DNAT --to-destination 10.0.0.1:80")
#os.system("iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 23 -j DNAT --to-destination 10.0.0.1:23")
import cherrypy
MEDIA_DIR = os.path.join(os.path.abspath("."), u"")
class Root(object):
    @cherrypy.expose
    def index(self):
        return open(os.path.join(MEDIA_DIR, u'index.html'))

config = {
    '/static':{
    'tools.staticdir.on': True,
    'tools.staticdir.dir': os.path.join(os.path.dirname(__file__), '')
    }
}
cherrypy.config.update({
                        'server.socket_port': 80,
                       })
cherrypy.tree.mount(Root(), '/', config = config)
cherrypy.engine.start()
cherrypy.engine.block() 