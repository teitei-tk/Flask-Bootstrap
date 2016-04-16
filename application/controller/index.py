# coding: utf-8

from lib.controller import Controller


class IndexController(Controller):
    methods = ['GET']

    def get(self):
        return self.render_template('index/index.html')
