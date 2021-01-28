import os
import logging

# author and license information
AUTHOR = 'Carlos Hernandez-Bueno Regojo'
AUTHOR_EMAIL = 'chernandezre.inf'
LICENSE = 'see license.md file for details'

# log configuration
DEBUG = True
LOG_LEVEL = logging.DEBUG

# flask configuration
PORT = 8080
HOST = '0.0.0.0'  # bind to all interfaces
TITLE = 'flask-backend-server'
VERSION = '1.0'
APP_NAME = 'flask-backend-server'
DESCRIPTION = 'Backend server for TFG'

# SQLUtils configuration
MONGO_URI = '<MongoDBUri>'
MONGO_DB = 'datosSensores'
MONGO_COLLECTION = 'sensores'

# application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
