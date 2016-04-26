#!/usr/bin/env bash
docker stop willbot-python
docker rm willbot-python
docker run -e SERVER_IDENTIFIER=willbot-python -d -P --link willbot-redis --name willbot-python stack/willbot-python python /willbot/run_will.py