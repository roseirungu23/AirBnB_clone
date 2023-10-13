#!/usr/bin/python3
"""Creates a unique FileStorage instance for your application"""
from models.engine.file_storage import FileStorage

"""Creates a variable storage, an instance of FileStorage"""
storage = FileStorage()
storage.reload()
