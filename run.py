#!/usr/bin/python
# -*- coding: UTF-8 -*-


import os
import bottle
from app import app


if __name__ == '__main__':
    bottle.TEMPLATE_PATH.insert(0, 'app/views/')
    if os.environ.get('APP_LOCATION') == 'heroku':
        app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    else:
        app.run(host = "localhost", port = 8080, debug = True)
