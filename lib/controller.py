# coding: utf-8

from flask_rest_controller import Controller as BaseController


class Controller(BaseController):
    def post(self, *args, **kwargs):
        return self.get(*args, **kwargs)
