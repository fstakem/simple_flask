#!/usr/bin/env bash
source ./env_vars.sh
printf "Flask app: %s\n\n" "$FLASK_APP"
flask run