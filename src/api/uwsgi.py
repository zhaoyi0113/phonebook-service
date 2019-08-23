#!/usr/bin/env python3

import connexion
import logging

from api import encoder
from api.models.db import Base, engine

logging.basicConfig(level=logging.DEBUG)

app = connexion.App(__name__, specification_dir='./openapi/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('openapi.yaml', pythonic_params=True)
application = app.app

Base.metadata.create_all(engine)