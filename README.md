# docker_deploy_demo
a demo for deploying web app in Docker using Flask, MongoDB and Nginx 

https://jiayi.space/post/shi-yong-dockeryi-jian-bu-shu-webying-yong

启动之后可以使用curl操作API 

查看:

curl -X GET http://localhost/api/note

新增:

curl -X POST -d 'content=hello world' http://localhost/api/note

清空:

curl -X DELETE http://localhost/api/note


