#!/usr/bin/python3
"""the link between models and engine"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
