#!/bin/bash
docker-compose kill
docker-compose rm -f
docker rmi demo_nginx
docker rmi demo_web
