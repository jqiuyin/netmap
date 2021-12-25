#!/bin/sh
source venv/bin/activate
flask deploy
exec gunicon -b 0.0.0.0:5000 --access-logfile - --error-logfile - flasky:app