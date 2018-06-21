#!/bin/bash
docker-compose up -d
docker run --rm -v $('pwd')/db/dump:/backup --net docker_deploy_demo_default mongo bash -c 'mongorestore /backup --host demo_db:27017'
