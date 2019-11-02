# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
file to provide pytest with a reusable fixture from flask-pytest returning an app instance
"""

import pytest
from cntct import create_app

@pytest.fixture
def app():
    app = create_app()
    return app
