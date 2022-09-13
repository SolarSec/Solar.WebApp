import flask, sys, json
from assets.error_handler import *

try:
    web_app_port: int = int(sys.argv[1])
    rlimit_timeout: int = int(sys.argv[2])
    debug: bool = bool(sys.argv[3])
except:
    print(handle_argerr().format(sys.argv[0]))
    exit(0)

class SolarSec:
    app = flask.Flask(__name__)
    def __init__ (self, web_app_port: int, rlimit_timeout: int, debug = False):
        self.web_app_port: int = web_app_port
        self.rlimit_timeout: int = rlimit_timeout
        self.debug: bool = debug
        self.webapp: str = None
    
    @app.route("/api/v1/scripts")
    def _scripts () -> str:
        """try:"""
        id: int = flask.request.args.get("id")
        try:    id = int(id)
        except: return flask.jsonify(flask_dterror()['Error'].format(type(flask.request.args.get("id"))))
        if id is None:  return flask.jsonify(flask_noiderr())

        """
            Our real backend would now index through a json CONFIG here, we would not like to share this code due to security purposes.
        """
        flask.abort(406)

if __name__ == '__main__':
    SolarSec(web_app_port, rlimit_timeout, debug=debug).app.run("127.0.0.1", port=web_app_port, debug=debug)
