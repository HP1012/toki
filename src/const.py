# -*- coding: utf-8 -*-

import logging
from pathlib import Path

NAME = 'Toki'
CODE = 'Mickey'

PORT = 9892

HOME = Path.home().joinpath(NAME)
CONFIG = HOME.joinpath('config.json')
LOGS = HOME.joinpath('logs', 'messages')

PORT = 9802