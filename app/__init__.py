#!/usr/bin/python
# -*- coding: UTF-8 -*-


from bottle import Bottle

app = Bottle()

from app.controller import controller
