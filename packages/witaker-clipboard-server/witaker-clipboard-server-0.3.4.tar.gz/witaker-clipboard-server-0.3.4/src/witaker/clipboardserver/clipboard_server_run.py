from multiprocessing import Process

import eventlet
import eventlet.wsgi

from witaker.clipboardserver import create_default_flask_app
from witaker.clipboardserver.clipboard_util import AuthorizedClipboardUtil

DEFAULT_SERVER_PORT = 42157

app = create_default_flask_app()

def start_flask_webserver(util: AuthorizedClipboardUtil, port: int):
    app.util = util
    eventlet.wsgi.server(eventlet.listen(('localhost', port)), app)

def start_server_process(util: AuthorizedClipboardUtil, server_port: int):
    server_process = Process(target=start_flask_webserver, args=(util, server_port,))
    server_process.start()
    return server_process

def stop_server_process(server_process):
    server_process.terminate()
    server_process.join()
    server_process.close()
