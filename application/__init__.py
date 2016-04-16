# coding: utf-8

import jinja2
from flask import Flask, g, make_response, request, send_file

import lib.router
from routes import ROUTING_VIEWS
from defines import PUBLIC_DIR, TEMPLATES_DIR


class Application(Flask):
    secret_key = '\x96hy\x96\xd6\x86\xb8#\xf0\x17\x81\n\xd8\x8a\xd3kp\x9c\xfd\xf6\x97\xf0\x89\xc8'

    def before_request_action(self):
        if "{0}/".format(PUBLIC_DIR) in request.path:
            public_path = "../{0}".format(request.path[1:])
            return send_file(public_path)

        g.assets_path = "{0}".format(PUBLIC_DIR)

    def after_request_action(self, response):
        response = make_response(response)
        return response

    def page_not_found(self, error):
        return error

    def internal_server_error(self, error):
        return error

    def dispatch(self):
        lib.router.set_routing(self, ROUTING_VIEWS)
        self.jinja_loader = jinja2.FileSystemLoader(TEMPLATES_DIR)

        self.before_request_funcs.setdefault(None, []).append(self.before_request_action)
        self.after_request_funcs.setdefault(None, []).append(self.after_request_action)

        self.error_handler_spec[None][404] = self.page_not_found
        self.error_handler_spec[None][500] = self.internal_server_error

app = Application(__name__)
app.dispatch()
