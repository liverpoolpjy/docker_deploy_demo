#!/bin/bash
docker-compose build
docker-compose up -d
docker run --rm --link demo_db:mongo -v $('pwd')/db/dump:/backup mongo bash -c 'mongorestore /backup --host mongo:27017'
