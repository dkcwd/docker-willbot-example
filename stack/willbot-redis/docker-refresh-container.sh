#!/usr/bin/env bash
docker stop willbot-redis
docker rm willbot-redis
docker run -e SERVER_IDENTIFIER=willbot-redis -d -P --name willbot-redis stack/willbot-redis