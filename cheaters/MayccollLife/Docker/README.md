# Docker
- - - - - - - - - -

- **Bash Inside Container**

```bash
    $
    docker run -itd ubuntu /bin/bash
    docker exec -it 2435236 bash
```

- **Stop / remove all Docker containers**

```bash
    $
    docker stop $(docker ps -a -q)
    docker rm $(docker ps -a -q)
```

- **Tar image**

```bash
    $
    docker save -o <save image to path> <image name>
    docker load -i <path to image tar file>
```

- **Dockerfile - Create Image**

```bash
  $
  docker build .
  docker build . -t mayc/gitlab:last
```

- **Setting tags on an image**

```bash
  $
  docker tag 5db5f8471261 ouruser/sinatra:devel
```

## Apps

#### Seagull (WORK)

```bash
    docker run  --name seagull \
                -v /var/run/docker.sock:/var/run/docker.sock \
                -p 60020:10086 \
                -d tobegit3hub/seagull
```
#### cAdvisor (WORK)

```bash
    docker run --name cAdvisor\
                -v /:/rootfs:ro \
                -v /var/run:/var/run:rw \
                -v /sys:/sys:ro \
                -v /var/lib/docker/:/var/lib/docker:ro \
                -p 60021:8080 \
                -d google/cadvisor:latest
```

#### Nginx (WORK)

```bash
    # Static server - html
    docker run --name nginx \
                -v $(pwd)/www:/usr/share/nginx/html \
                -p 60080:80    \
                -d nginx
```

#### Mariadb (WORK)

```bash
  docker run --name mariadb \
              -e MYSQL_ROOT_PASSWORD=secretpass \
              -e MYSQL_DATABASE=mydatabase \
              -d mariadb
```

#### Wordpress (WORK)

```bash
  docker run --name wordpress \
              --link mariadb:mysql \
              -p 60080:80 \
              -v /$(pwd)/www:/var/www/html \
              -e WORDPRESS_DB_USER=root \
              -e WORDPRESS_DB_PASSWORD=secretpass \
              -e WORDPRESS_DB_NAME=mydatabase \
              -d wordpress
```

#### Gitlab

```bash
  docker run --detach \
            --publish 8443:443 --publish 8080:80 --publish 2222:22 \
            --name gitlab \
            --restart always \
            --volume $(pwd)/gitlab/config:/etc/gitlab \
            --volume $(pwd)/gitlab/logs:/var/log/gitlab \
            --volume $(pwd)/gitlab/data:/var/opt/gitlab \
            gitlab/gitlab-ce:latest
```

#### Dockercraft

```bash
  docker run -t -i -d --name dockercraft \
        -p 25565:25565 \
        -v /var/run/docker.sock:/var/run/docker.sock \        
        gaetan/dockercraft
```
