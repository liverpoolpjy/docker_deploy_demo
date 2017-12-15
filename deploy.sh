#!/bin/bash
docker-compose build
docker-compose up -d
docker run --rm --link -v $('pwd')/db/dump:/backup --net dockerdeploydemo_default mongo bash -c 'mongorestore /backup --host demo_db:27017'
