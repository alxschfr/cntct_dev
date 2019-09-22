# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
WSGI-entry point to start a single app instance
"""

from cntct import create_app

app = create_app()

if __name__ == '__main__':
    app.run()