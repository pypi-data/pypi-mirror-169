# -*- coding: utf-8 -*-
"""
生产环境启动入口
"""

from werkzeug.middleware.proxy_fix import ProxyFix

from domain_admin.app import app
from domain_admin.config import FLASK_HOST, FLASK_PORT

app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.run(port=FLASK_PORT, host=FLASK_HOST)
