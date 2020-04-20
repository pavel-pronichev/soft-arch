#!/usr/bin/env bash

if [ "$ENVIRONMENT" = 'DEV' ]; then
    exec uvicorn main:app --reload --host 0.0.0.0
else
    exec gunicorn -w 4 -k uvicorn.workers.UvicornWorker
fi