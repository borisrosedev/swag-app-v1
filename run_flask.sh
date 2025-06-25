#!/bin/bash 
export FLASK_DEBUG=1
export FLASK_APP=__init__:create_app
export FLASK_ENV=development
flask run