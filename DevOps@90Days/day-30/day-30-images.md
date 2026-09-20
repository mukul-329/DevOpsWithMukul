## Challenge Tasks

### Task 1: Docker Images

- Pull the `nginx`, `ubuntu`, and `alpine` images from Docker Hub
  - docker images 
    <br>(Will show all the images docker has locally)
      ```text
      PS C:\Users\mukul> docker images
      IMAGE                ID             DISK USAGE   CONTENT SIZE   EXTRA
      hello-world:latest   5dd0d3e6e255       25.9kB         9.49kB    U 
      nginx:latest         8541484afbc9        241MB           66MB    U 
      ubuntu:latest        678c6550cc43        160MB         45.3MB    U 
      ```
  - docker pull `image-name'
    - Pulling nginx image (Since image is already present locally, it will just fetch the latest content)
      ```text 
      PS C:\Users\mukul> docker pull nginx
      Using default tag: latest
      latest: Pulling from library/nginx
      Digest: sha256:8541484afbc9c8a5a8a99b379568ebbc957f658583ec9448fc43104229c03cf8
      Status: Image is up to date for nginx:latest
      docker.io/library/nginx:latest
      ```

    - Pulling mysql image
      <br>(You will see something like this, when image is downloading and not present locally.)
      ```text 
       PS C:\Users\mukul> docker pull mysql     
       Using default tag: latest
       latest: Pulling from library/mysql
       feffc3e2a7dd: Download complete
       0bb65eb170f9: Download complete
       30627cea5424: Downloading [================================>                  ]  31.46MB/47.93MB
       7e887550bdc4: Download complete
       35475b275575: Download complete
       27683f99b921: Download complete
       1791a4d7fecf: Downloading [====================>                              ]  24.12MB/57.45MB
       e480dcc782ea: Download complete
       71fa527c6c68: Download complete
       c4e766e27938: Downloading [========>                                          ]  27.26MB/160MB
       ```
       ```text
       PS C:\Users\mukul> docker pull mysql     
       Using default tag: latest
       latest: Pulling from library/mysql
       feffc3e2a7dd: Download complete
       0bb65eb170f9: Download complete
       feffc3e2a7dd: Pull complete 
       7e887550bdc4: Pull complete
       35475b275575: Pull complete
       27683f99b921: Pull complete
       1791a4d7fecf: Pull complete 
       e480dcc782ea: Pull complete
       71fa527c6c68: Pull complete
       c4e766e27938: Pull complete
       81ee3e1129f4: Download complete                                                                                           
       808810e42158: Download complete
       Digest: sha256:66aec17cd21a956029b83f083b813073859e8355dc1a00e55df6ba02f0e32345
       Status: Downloaded newer image for mysql:latest
       docker.io/library/mysql:latest
       ```
       ```text
       PS C:\Users\mukul> docker images
       IMAGE                ID             DISK USAGE   CONTENT SIZE   EXTRA
       hello-world:latest   5dd0d3e6e255       25.9kB         9.49kB    U 
       mysql:latest         66aec17cd21a        1.3GB          290MB
       nginx:latest         8541484afbc9        241MB           66MB    U 
       ubuntu:latest        678c6550cc43        160MB         45.3MB    U 
       ```
    - Pulling alpine images
      <br>Alpine is generally small sized image. 
      ```text
      PS C:\Users\mukul> docker pull alpine
      Using default tag: latest
      latest: Pulling from library/alpine
      55afa1ecc21d: Pull complete                                                                                               
      56dceff11b33: Download complete
      f5124fb579e2: Download complete                                                                                           
      Digest: sha256:28bd5fe8b56d1bd048e5babf5b10710ebe0bae67db86916198a6eec434943f8b
      Status: Downloaded newer image for alpine:latest
      docker.io/library/alpine:latest
      PS C:\Users\mukul> docker images  
      IMAGE                ID             DISK USAGE   CONTENT SIZE   EXTRA
      alpine:latest        28bd5fe8b56d         13MB         3.93MB
      hello-world:latest   5dd0d3e6e255       25.9kB         9.49kB    U 
      mysql:latest         66aec17cd21a        1.3GB          290MB
      nginx:latest         8541484afbc9        241MB           66MB    U 
      ubuntu:latest        678c6550cc43        160MB         45.3MB    U 
      ```
      ```text
       PS C:\Users\mukul> docker run -it alpine
       / # ls
       bin    dev    etc    home   lib    media  mnt    opt    proc   root   run    sbin   srv    sys    tmp    usr    var
       / # uname
       Linux
       / # 
       ```
- List all images on your machine — note the sizes
  - docker images  
    ```text
    PS C:\Users\mukul> docker images  
      IMAGE                ID             DISK USAGE   CONTENT SIZE   EXTRA
      alpine:latest        28bd5fe8b56d         13MB         3.93MB
      hello-world:latest   5dd0d3e6e255       25.9kB         9.49kB    U 
      mysql:latest         66aec17cd21a        1.3GB          290MB
      nginx:latest         8541484afbc9        241MB           66MB    U 
      ubuntu:latest        678c6550cc43        160MB         45.3MB    U 
    ```     

- Compare `ubuntu` vs `alpine` — why is one much smaller?
  - ubuntu size: 160MB
  - alpine size: 13MB


- Inspect an image — what information can you see?
  - docker inspect `image-id/image-name` 
    <br>e.g docker inspect 28bd5fe8b56d 
    <br>e.g docker inspect alpine:latest
    ```text 
    PS C:\Users\mukul> docker inspect 28bd5fe8b56d
    [
        {
            "Id": "sha256:28bd5fe8b56d1bd048e5babf5b10710ebe0bae67db86916198a6eec434943f8b",
            "RepoTags": [
                "alpine:latest"
            ],
            "RepoDigests": [
                "alpine@sha256:28bd5fe8b56d1bd048e5babf5b10710ebe0bae67db86916198a6eec434943f8b"
            ],
            "Comment": "buildkit.dockerfile.v0",
            "Created": "2026-06-16T00:01:29.967161902Z",
            "Config": {
                "Env": [
                    "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
                ],
                "Cmd": [
                    "/bin/sh"
                ],
                "WorkingDir": "/"
            },
            "Architecture": "amd64",
            "Os": "linux",
            "Size": 3857242,
            "RootFS": {
                "Type": "layers",
                "Layers": [
                    "sha256:34884abbe92863fce933ed7c39c0e045631af0ed86d5cc0dfbdf9fdca426ce3c"
                ]
            },
            "Metadata": {
                "LastTagTime": "2026-08-18T10:55:55.509115183Z"
            },
            "Descriptor": {
                "mediaType": "application/vnd.oci.image.index.v1+json",
                "digest": "sha256:28bd5fe8b56d1bd048e5babf5b10710ebe0bae67db86916198a6eec434943f8b",
                "size": 9218
            },
            "Identity": {
                "Pull": [
                    {
                        "Repository": "docker.io/library/alpine"
                    }
                ]
            }
        }
    ]
    PS C:\Users\mukul> 
    ```

- Remove an image you no longer need
  - docker rmi `image-name/image-id`
    <br>(Before removing we have to make sure that no stopped or running container using it.)
    ```text
    PS C:\Users\mukul> docker rmi alpine
    Untagged: alpine:latest
    Deleted: sha256:28bd5fe8b56d1bd048e5babf5b10710ebe0bae67db86916198a6eec434943f8b
    PS C:\Users\mukul> docker images

    IMAGE                ID             DISK USAGE   CONTENT SIZE   EXTRA
    hello-world:latest   5dd0d3e6e255       25.9kB         9.49kB    U 
    mysql:latest         66aec17cd21a        1.3GB          290MB
    nginx:latest         8541484afbc9        241MB           66MB    U 
    ubuntu:latest        678c6550cc43        160MB         45.3MB    U 
    PS C:\Users\mukul> docker rmi 66aec17cd21a
    Untagged: mysql:latest
    Deleted: sha256:66aec17cd21a956029b83f083b813073859e8355dc1a00e55df6ba02f0e32345
    PS C:\Users\mukul> 
    ```
  - Removing a image when it's being used Like nginx.
    ```text
    PS C:\Users\mukul> docker rmi nginx
    Error response from daemon: conflict: unable to delete nginx:latest (must be forced) - container f43e9bfd6984 is using its referenced image 8541484afbc9
    PS C:\Users\mukul> docker ps -a
    CONTAINER ID   IMAGE         COMMAND                  CREATED        STATUS                      PORTS     NAMES
    c26e6fe71e22   ubuntu        "bash"                   12 hours ago   Exited (0) 12 hours ago               zen_cray       
    6a0efd4e527d   ubuntu        "/bin/bash"              12 hours ago   Exited (0) 12 hours ago               funny_torvalds 
    f43e9bfd6984   nginx         "/docker-entrypoint.…"   12 hours ago   Exited (0) 12 hours ago               hopeful_zhukovsky
    91153495f8b9   nginx         "/docker-entrypoint.…"   12 hours ago   Exited (127) 12 hours ago             intelligent_robinson
    664f02cb500e   nginx         "/docker-entrypoint.…"   12 hours ago   Exited (0) 12 hours ago               tender_hodgkin 
    2976f7bd2a54   hello-world   "/hello"                 12 hours ago   Exited (0) 12 hours ago               strange_dijkstra
    8e1c1f11a1a0   hello-world   "/hello"                 21 hours ago   Exited (0) 21 hours ago               adoring_panini 
    PS C:\Users\mukul> docker rm f43e9bfd6984 91153495f8b9 664f02cb500e
    f43e9bfd6984
    91153495f8b9
    664f02cb500e
    PS C:\Users\mukul> docker rmi 8541484afbc9
    Untagged: nginx:latest
    Deleted: sha256:8541484afbc9c8a5a8a99b379568ebbc957f658583ec9448fc43104229c03cf8
    PS C:\Users\mukul>   
    ```
---
### Task 2: Image Layers
- Run `docker image history nginx` — what do you see?
  <br>(Since I have deleted nginx, I am using ubuntu)
  ```text 
  PS C:\Users\mukul> docker image history ubuntu:latest
  IMAGE          CREATED       CREATED BY                                      SIZE      COMMENT
  678c6550cc43   3 weeks ago   umoci raw add-layer --image /home/buildd/roc…   12.3kB    Add rock control metadata
  <missing>      3 weeks ago   umoci config --image /home/buildd/rockcraft-…   0B        Set annotations
  <missing>      3 weeks ago   umoci config --image /home/buildd/rockcraft-…   0B        Set labels
  <missing>      3 weeks ago   umoci config --image /home/buildd/rockcraft-…   0B        Set default PATH for bare-based rock
  <missing>      3 weeks ago   umoci config --image /home/buildd/rockcraft-…   0B        Set default commands
  <missing>      3 weeks ago   umoci config --image /home/buildd/rockcraft-…   0B        Set entrypoint
  <missing>      3 weeks ago   umoci raw add-layer --image /home/buildd/roc…   115MB
  PS C:\Users\mukul> docker image history nginx 
  Error response from daemon: No such image: nginx:latest
  PS C:\Users\mukul> 
  ```

- Each line is a **layer**. Note how some layers show sizes and some show 0B  
  ```text
  PS C:\Users\mukul> docker image history alpine/mysql
  IMAGE          CREATED        CREATED BY                                      SIZE      COMMENT
  0799620753ba   3 days ago     CMD ["--help"]                                  0B        buildkit.dockerfile.v0
  <missing>      3 days ago     ENTRYPOINT ["/usr/bin/mariadb"]                 0B        buildkit.dockerfile.v0
  <missing>      3 days ago     RUN /bin/sh -c apk add --update --no-cache m…   46.1MB    buildkit.dockerfile.v0
  <missing>      2 months ago   CMD ["/bin/sh"]                                 0B        buildkit.dockerfile.v0
  <missing>      2 months ago   ADD alpine-minirootfs-3.24.1-x86_64.tar.gz /…   9.07MB    buildkit.dockerfile.v0
  ```

- Write in your notes: What are layers and why does Docker use them?
  - Let's check layers for nginx image.
     ```text
     PS C:\Users\mukul> docker pull nginx
     Using default tag: latest
     latest: Pulling from library/nginx
     5a4222b844e8: Pull complete
     d84ae7b21412: Pull complete
     26c307b5e35a: Pull complete
     c0df8d325117: Pull complete
     3c55dc422a81: Pull complete
     b8b80b9bc028: Pull complete
     f5de6e85ac74: Pull complete
     92fcf0fc2ef2: Download complete
     0f03cb4db0ef: Download complete
     Digest: sha256:8541484afbc9c8a5a8a99b379568ebbc957f658583ec9448fc43104229c03cf8
     Status: Downloaded newer image for nginx:latest
     docker.io/library/nginx:latest
     PS C:\Users\mukul> docker image history nginx
     IMAGE          CREATED       CREATED BY                                      SIZE      COMMENT
     8541484afbc9   13 days ago   CMD ["nginx" "-g" "daemon off;"]                0B        buildkit.dockerfile.v0
     <missing>      13 days ago   STOPSIGNAL SIGQUIT                              0B        buildkit.dockerfile.v0
     <missing>      13 days ago   EXPOSE map[80/tcp:{}]                           0B        buildkit.dockerfile.v0
     <missing>      13 days ago   ENTRYPOINT ["/docker-entrypoint.sh"]            0B        buildkit.dockerfile.v0
     <missing>      13 days ago   COPY 30-tune-worker-processes.sh /docker-ent…   16.4kB    buildkit.dockerfile.v0
     <missing>      13 days ago   COPY 20-envsubst-on-templates.sh /docker-ent…   12.3kB    buildkit.dockerfile.v0
     <missing>      13 days ago   COPY 15-local-resolvers.envsh /docker-entryp…   12.3kB    buildkit.dockerfile.v0
     <missing>      13 days ago   COPY 10-listen-on-ipv6-by-default.sh /docker…   12.3kB    buildkit.dockerfile.v0
     <missing>      13 days ago   COPY docker-entrypoint.sh / # buildkit          8.19kB    buildkit.dockerfile.v0
     <missing>      13 days ago   RUN /bin/sh -c set -x     && groupadd --syst…   87.1MB    buildkit.dockerfile.v0
     <missing>      13 days ago   ENV DYNPKG_RELEASE=1~trixie                     0B        buildkit.dockerfile.v0
     <missing>      13 days ago   ENV PKG_RELEASE=1~trixie                        0B        buildkit.dockerfile.v0
     <missing>      13 days ago   ENV ACME_VERSION=0.4.1                          0B        buildkit.dockerfile.v0
     <missing>      13 days ago   ENV NJS_RELEASE=1~trixie                        0B        buildkit.dockerfile.v0
     <missing>      13 days ago   ENV NJS_VERSION=1.0.0                           0B        buildkit.dockerfile.v0
     <missing>      13 days ago   ENV NGINX_VERSION=1.31.3                        0B        buildkit.dockerfile.v0
     <missing>      13 days ago   LABEL maintainer=NGINX Docker Maintainers <d…   0B        buildkit.dockerfile.v0
     <missing>      2 weeks ago   # debian.sh --arch 'amd64' out/ 'trixie' '@1…   87.4MB    debuerreotype 0.17
     PS C:\Users\mukul>   
     ```

  - Layers
     - layer is a read-only filesystem change that becomes part of an image.
     - Why we need layers? 
       - Reuse
       - Faster Builds   
       - Image distribution
     - Docker builds images as a series of filesystem layers, and those layers can be cached, reused, shared, and distributed independently.  
     - `0B` means that instruction didn't add filesystem data to that layer.
     - The `SIZE` values are layer sizes, not necessarily the amount of disk space Docker uses independently for every row.

---
### Task 3: Container Lifecycle    
- Create & rename container
  - docker create `image-name`
     ```text
     PS C:\Users\mukul> docker create nginx
     c304852c85bec6b04a02d5f4f783c7cd2cea8ff5faed02ecf11682cd7c4b7686
     PS C:\Users\mukul> docker ps -a
     CONTAINER ID   IMAGE         COMMAND                  CREATED         STATUS                    PORTS     NAMES
     c304852c85be   nginx         "/docker-entrypoint.…"   4 seconds ago   Created                             funny_keller
     c26e6fe71e22   ubuntu        "bash"                   15 hours ago    Exited (0) 15 hours ago             zen_cray
     6a0efd4e527d   ubuntu        "/bin/bash"              16 hours ago    Exited (0) 16 hours ago             funny_torvalds
     2976f7bd2a54   hello-world   "/hello"                 16 hours ago    Exited (0) 16 hours ago             strange_dijkstra
     8e1c1f11a1a0   hello-world   "/hello"                 25 hours ago    Exited (0) 25 hours ago             adoring_panini
     ```
  - docker rename c304852c85be my-app
    ```text
    PS C:\Users\mukul> docker rename c304852c85be my-app
    PS C:\Users\mukul> docker ps -a
    CONTAINER ID   IMAGE         COMMAND                  CREATED              STATUS                    PORTS     NAMES
    c304852c85be   nginx         "/docker-entrypoint.…"   About a minute ago   Created                             my-app     
    c26e6fe71e22   ubuntu        "bash"                   16 hours ago         Exited (0) 16 hours ago             zen_cray   
    6a0efd4e527d   ubuntu        "/bin/bash"              16 hours ago         Exited (0) 16 hours ago             funny_torvalds
    2976f7bd2a54   hello-world   "/hello"                 16 hours ago         Exited (0) 16 hours ago             strange_dijkstra
    8e1c1f11a1a0   hello-world   "/hello"                 25 hours ago         Exited (0) 25 hours ago             adoring_panini
    ```

- Start a container
  - docker start `container-name/id` 
    ```text
    PS C:\Users\mukul> docker start my-app
    my-app
    PS C:\Users\mukul> docker ps -a       
    CONTAINER ID   IMAGE         COMMAND                  CREATED         STATUS                    PORTS     NAMES
    c304852c85be   nginx         "/docker-entrypoint.…"   3 minutes ago   Up 2 seconds              80/tcp    my-app
    c26e6fe71e22   ubuntu        "bash"                   16 hours ago    Exited (0) 16 hours ago             zen_cray        
    6a0efd4e527d   ubuntu        "/bin/bash"              16 hours ago    Exited (0) 16 hours ago             funny_torvalds  
    2976f7bd2a54   hello-world   "/hello"                 16 hours ago    Exited (0) 16 hours ago             strange_dijkstra
    8e1c1f11a1a0   hello-world   "/hello"                 25 hours ago    Exited (0) 25 hours ago             adoring_panini  
    PS C:\Users\mukul> 
    ```
- Pause/Unpause a container
  - docker pause `container-name/id`   
     ```text
     PS C:\Users\mukul> docker pause my-app
     my-app
     PS C:\Users\mukul> docker ps -a       
     CONTAINER ID   IMAGE         COMMAND                  CREATED         STATUS                       PORTS     NAMES
     c304852c85be   nginx         "/docker-entrypoint.…"   4 minutes ago   Up About a minute (Paused)   80/tcp    my-app       
     c26e6fe71e22   ubuntu        "bash"                   16 hours ago    Exited (0) 16 hours ago                zen_cray     
     6a0efd4e527d   ubuntu        "/bin/bash"              16 hours ago    Exited (0) 16 hours ago                funny_torvalds
     2976f7bd2a54   hello-world   "/hello"                 16 hours ago    Exited (0) 16 hours ago                strange_dijkstra
     8e1c1f11a1a0   hello-world   "/hello"                 25 hours ago    Exited (0) 25 hours ago                adoring_panini
     PS C:\Users\mukul> 
     ```
  - docker unpause `container-name/id`
    ```text
    PS C:\Users\mukul> docker unpause my-app
    my-app
    PS C:\Users\mukul> docker ps -a
    CONTAINER ID   IMAGE         COMMAND                  CREATED         STATUS                    PORTS     NAMES
    c304852c85be   nginx         "/docker-entrypoint.…"   6 minutes ago   Up 2 minutes              80/tcp    my-app
    c26e6fe71e22   ubuntu        "bash"                   16 hours ago    Exited (0) 16 hours ago             zen_cray        
    6a0efd4e527d   ubuntu        "/bin/bash"              16 hours ago    Exited (0) 16 hours ago             funny_torvalds  
    2976f7bd2a54   hello-world   "/hello"                 16 hours ago    Exited (0) 16 hours ago             strange_dijkstra
    8e1c1f11a1a0   hello-world   "/hello"                 25 hours ago    Exited (0) 25 hours ago             adoring_panini  
    PS C:\Users\mukul> 
    ```
- Restart a container
  - docker restart `container-name/id`
     ```text
     PS C:\Users\mukul> docker restart c304852c85be
     c304852c85be
     PS C:\Users\mukul> docker ps -a
     CONTAINER ID   IMAGE         COMMAND                  CREATED         STATUS                    PORTS     NAMES
     c304852c85be   nginx         "/docker-entrypoint.…"   7 minutes ago   Up 2 seconds              80/tcp    my-app
     c26e6fe71e22   ubuntu        "bash"                   16 hours ago    Exited (0) 16 hours ago             zen_cray        
     6a0efd4e527d   ubuntu        "/bin/bash"              16 hours ago    Exited (0) 16 hours ago             funny_torvalds  
     2976f7bd2a54   hello-world   "/hello"                 16 hours ago    Exited (0) 16 hours ago             strange_dijkstra
     8e1c1f11a1a0   hello-world   "/hello"                 25 hours ago    Exited (0) 25 hours ago             adoring_panini  
     PS C:\Users\mukul> 
     ```

- Kill a container
  - docker kill `container-name/id`   
     ```text
     PS C:\Users\mukul> docker kill c304852c85be   
     c304852c85be
     PS C:\Users\mukul> docker ps -a
     CONTAINER ID   IMAGE         COMMAND                  CREATED         STATUS                       PORTS     NAMES
     c304852c85be   nginx         "/docker-entrypoint.…"   9 minutes ago   Exited (137) 3 seconds ago             my-app       
     c26e6fe71e22   ubuntu        "bash"                   16 hours ago    Exited (0) 16 hours ago                zen_cray     
     6a0efd4e527d   ubuntu        "/bin/bash"              16 hours ago    Exited (0) 16 hours ago                funny_torvalds
     2976f7bd2a54   hello-world   "/hello"                 16 hours ago    Exited (0) 16 hours ago                strange_dijkstra
     8e1c1f11a1a0   hello-world   "/hello"                 25 hours ago    Exited (0) 25 hours ago                adoring_panini
     PS C:\Users\mukul> 
     ```

- Stop & Remove a Container
  - docker stop `container-name/id`
     ```text
     PS C:\Users\mukul> docker stop my-app 
     my-app
     PS C:\Users\mukul> docker ps -a       
     CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                     PORTS     NAMES
     c304852c85be   nginx         "/docker-entrypoint.…"   10 minutes ago   Exited (0) 3 seconds ago             my-app        
     c26e6fe71e22   ubuntu        "bash"                   16 hours ago     Exited (0) 16 hours ago              zen_cray      
     6a0efd4e527d   ubuntu        "/bin/bash"              16 hours ago     Exited (0) 16 hours ago              funny_torvalds
     2976f7bd2a54   hello-world   "/hello"                 16 hours ago     Exited (0) 16 hours ago              strange_dijkstra
     8e1c1f11a1a0   hello-world   "/hello"                 25 hours ago     Exited (0) 25 hours ago              adoring_panini
     PS C:\Users\mukul> 
     ```
  - docker rm `container-name/id`   
     ```text
     PS C:\Users\mukul> docker rm my-app
     my-app
     PS C:\Users\mukul> docker ps -a        
     CONTAINER ID   IMAGE         COMMAND       CREATED        STATUS                    PORTS     NAMES
     c26e6fe71e22   ubuntu        "bash"        16 hours ago   Exited (0) 16 hours ago             zen_cray
     6a0efd4e527d   ubuntu        "/bin/bash"   16 hours ago   Exited (0) 16 hours ago             funny_torvalds
     2976f7bd2a54   hello-world   "/hello"      16 hours ago   Exited (0) 16 hours ago             strange_dijkstra
     8e1c1f11a1a0   hello-world   "/hello"      25 hours ago   Exited (0) 25 hours ago             adoring_panini
     PS C:\Users\mukul> 
     ```
---

### Task 4: Working with Running Containers     
- Run an Nginx container in detached mode
  - docker run -d --name my-nginx nginx
    ```text
    PS C:\Users\mukul> docker run -d --name my-nginx nginx
    0e140795cb4dac289c7556e6efa628fad8c0302b731aca6c89e6781492ad5bcb
    PS C:\Users\mukul> docker ps   
    CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS     NAMES
    0e140795cb4d   nginx     "/docker-entrypoint.…"   6 seconds ago   Up 5 seconds   80/tcp    my-nginx
    ```
- View its **logs**
  - docker logs my-nginx
    ```text
    PS C:\Users\mukul> docker logs my-nginx
    /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
    /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
    /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
    10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
    10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
    /docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
    /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
    /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
    /docker-entrypoint.sh: Configuration complete; ready for start up
    2026/08/18 14:50:21 [notice] 1#1: using the "epoll" event method
    2026/08/18 14:50:21 [notice] 1#1: nginx/1.31.3
    2026/08/18 14:50:21 [notice] 1#1: built by gcc 14.2.0 (Debian 14.2.0-19)
    2026/08/18 14:50:21 [notice] 1#1: OS: Linux 6.18.33.2-microsoft-standard-WSL2
    2026/08/18 14:50:21 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
    2026/08/18 14:50:21 [notice] 1#1: start worker processes
    2026/08/18 14:50:21 [notice] 1#1: start worker process 29
    2026/08/18 14:50:21 [notice] 1#1: start worker process 30
    2026/08/18 14:50:21 [notice] 1#1: start worker process 31
    2026/08/18 14:50:21 [notice] 1#1: start worker process 32
    PS C:\Users\mukul> 
    ```
- View its relatime logs (Follow mode)  
  - docker logs -f my-nginx
    ```text
    PS C:\Users\mukul> docker logs -f my-nginx
    /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
    /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
    /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
    10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
    10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
    /docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
    /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
    /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
    /docker-entrypoint.sh: Configuration complete; ready for start up
    2026/08/18 14:50:21 [notice] 1#1: using the "epoll" event method
    2026/08/18 14:50:21 [notice] 1#1: nginx/1.31.3
    2026/08/18 14:50:21 [notice] 1#1: built by gcc 14.2.0 (Debian 14.2.0-19)
    2026/08/18 14:50:21 [notice] 1#1: OS: Linux 6.18.33.2-microsoft-standard-WSL2
    2026/08/18 14:50:21 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
    2026/08/18 14:50:21 [notice] 1#1: start worker processes
    2026/08/18 14:50:21 [notice] 1#1: start worker process 29
    2026/08/18 14:50:21 [notice] 1#1: start worker process 30
    2026/08/18 14:50:21 [notice] 1#1: start worker process 31
    2026/08/18 14:50:21 [notice] 1#1: start worker process 32
    ```
- **Exec** into the container and look around the filesystem
  - docker exec -it my-nginx bash
     ```text 
     PS C:\Users\mukul> docker exec -it my-nginx bash
     root@0e140795cb4d:/# ls
     bin   dev                  docker-entrypoint.sh  home  lib64  mnt  proc  run   srv  tmp  var
     boot  docker-entrypoint.d  etc                   lib   media  opt  root  sbin  sys  usr
     root@0e140795cb4d:/#
    ```
- Run a single command inside the container without entering it
  - docker exec my-nginx ls
     ```text
     PS C:\Users\mukul> docker exec my-nginx uname
     Linux
     PS C:\Users\mukul>
     ```
- **Inspect** the container — find its IP address, port mappings, and mounts
  - docker inspect my-nginx
  - Use `--format` to extract exactly the information you want.
  - docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' my-nginx
    <br>(To check IP address)
  - docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' my-nginx  
  - docker inspect --format='{{json .NetworkSettings.Ports}}' my-nginx
  - docker inspect --format='{{json .Mounts}}' my-nginx
    ```text
    PS C:\Users\mukul> docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' my-nginx
    172.17.0.2
    PS C:\Users\mukul> docker inspect --format='{{json .NetworkSettings.Ports}}' my-nginx
    {"80/tcp":null}
    PS C:\Users\mukul> docker inspect --format='{{json .Mounts}}' my-nginx
    []
    PS C:\Users\mukul> 
    ```
---

### Task 5: Cleanup
- Stop all running containers in one command
  - docker stop $(docker ps -q)
    <br>(docker ps will show all containers)
    <br>(`-q` will be used to get containers ids)
     ```text
     PS C:\Users\mukul> docker stop $(docker ps -q)
     0e140795cb4d
     PS C:\Users\mukul> docker ps
     CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
     ``` 
- Remove all stopped containers in one command
  - docker rm $(docker ps -aq)
    <br>(docker ps -a will show all containers)
    <br>(`-q` will be used to get containers ids)
     ```text
     PS C:\Users\mukul> docker ps -a
     CONTAINER ID   IMAGE         COMMAND                  CREATED        STATUS                          PORTS     NAMES
     0e140795cb4d   nginx         "/docker-entrypoint.…"   3 hours ago    Exited (0) About a minute ago             my-nginx
     c26e6fe71e22   ubuntu        "bash"                   19 hours ago   Exited (0) 19 hours ago                   zen_cray
     6a0efd4e527d   ubuntu        "/bin/bash"              19 hours ago   Exited (0) 19 hours ago                   funny_torvalds
     2976f7bd2a54   hello-world   "/hello"                 19 hours ago   Exited (0) 19 hours ago                   strange_dijkstra
     8e1c1f11a1a0   hello-world   "/hello"                 28 hours ago   Exited (0) 28 hours ago                   adoring_panini
     PS C:\Users\mukul> docker rm $(docker ps -aq)
     0e140795cb4d
     c26e6fe71e22
     6a0efd4e527d
     2976f7bd2a54
     8e1c1f11a1a0
     PS C:\Users\mukul> docker ps -a
     CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
     PS C:\Users\mukul> 
     ```

- Remove unused images
  - docker image prune (Removes all dangling images)
  - docker image prune -a (Removes all images including)
  - docker image prune -af (Won't ask for confirmation)
    ```text
    PS C:\Users\mukul> docker images
    IMAGE                 ID             DISK USAGE   CONTENT SIZE   EXTRA
    alpine/mysql:latest   0799620753ba       70.6MB         15.4MB
    hello-world:latest    5dd0d3e6e255       25.9kB         9.49kB
    nginx:latest          8541484afbc9        241MB           66MB
    ubuntu:latest         678c6550cc43        160MB         45.3MB
    PS C:\Users\mukul> docker image prune
    WARNING! This will remove all dangling images.
    Are you sure you want to continue? [y/N] y
    Total reclaimed space: 0B
    PS C:\Users\mukul> docker image prune -a
    WARNING! This will remove all images without at least one container associated to them.
    Are you sure you want to continue? [y/N] y
    Deleted Images:
    untagged: nginx:latest
    deleted: sha256:8541484afbc9c8a5a8a99b379568ebbc957f658583ec9448fc43104229c03cf8
    deleted: sha256:963cfe6e75d1c292f66589d7e190b137cf89310414c0c1c5b476dfc61a4fcd0d
    deleted: sha256:a2a034340090fa5be6987a96c1c1e9cd5be56157bea6d918acf9c1bbd28073c8
    untagged: ubuntu:latest
    deleted: sha256:678c6550cc43645e08669028bc177f50be4e7c5b8cca677067b1914d4afc7a03
    deleted: sha256:7b202b0e2e0028c6250f5fcf41d04df492d145a1654c6995a6553f0c1f6f1960
    deleted: sha256:522d96ea380735b5cf03988f84c2ac91c28d72f628c905881e78f7e9d67079ad
    untagged: alpine/mysql:latest
    deleted: sha256:0799620753bad5d7e4c2e4740b9e31d811e2983392a0b1a433e4a7326353c2a0
    deleted: sha256:fd2b379656fe4729a240b857dac0dcbb032c57231fa35952ca24815894211779
    untagged: hello-world:latest
    deleted: sha256:5dd0d3e6e255913fc30f90b9f2b1d359cc2cbdb48090cc4b65f1676e203243cc
    deleted: sha256:d1a8d0a4eeb63aff09f5f34d4d80505e0ba81905f36158cc3970d8e07179e59e
    deleted: sha256:8e752a1cddeafc02597e756f4a0ec96e29f63ac4bc4af87682daf3f1de843bb7

    Total reclaimed space: 471.7MB
    PS C:\Users\mukul> 
    ```

- Check how much disk space Docker is using
  - docker system df (To check disk space)
    ```text
    PS C:\Users\mukul> docker system df
    TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
    Images          1         1         240.6MB   0B (0%)
    Containers      1         1         81.92kB   0B (0%)
    Local Volumes   0         0         0B        0B
    Build Cache     0         0         0B        0B
    ```
  - docker system info (To check docker system info)
    ```text 
    
    PS C:\Users\mukul> docker system info
    Client:
    Version:    29.7.2
    Context:    desktop-linux
    Debug Mode: false
    Plugins:
    agent: Docker AI Agent Runner (Docker Inc.)
        Version:  v1.119.0
        Path:     C:\Program Files\Docker\cli-plugins\docker-agent.exe
    ai: Docker AI Agent - Ask Gordon (Docker Inc.)
        Version:  v1.30.0
        Path:     C:\Program Files\Docker\cli-plugins\docker-ai.exe
    buildx: Docker Buildx (Docker Inc.)
        Version:  v0.36.0-desktop.1
        Path:     C:\Program Files\Docker\cli-plugins\docker-buildx.exe
    compose: Docker Compose (Docker Inc.)
        Version:  v5.3.1
        Path:     C:\Program Files\Docker\cli-plugins\docker-compose.exe
    debug: Get a shell into any image or container (Docker Inc.)
        Version:  0.0.47
        Path:     C:\Program Files\Docker\cli-plugins\docker-debug.exe
    desktop: Docker Desktop commands (Docker Inc.)
        Version:  v0.4.3
        Path:     C:\Program Files\Docker\cli-plugins\docker-desktop.exe
    dhi: CLI for managing Docker Hardened Images (Docker Inc.)
        Version:  v0.0.7
        Path:     C:\Program Files\Docker\cli-plugins\docker-dhi.exe
    extension: Manages Docker extensions (Docker Inc.)
        Version:  v0.2.31
        Path:     C:\Program Files\Docker\cli-plugins\docker-extension.exe
    init: Creates Docker-related starter files for your project (Docker Inc.)
        Version:  v1.4.0
        Path:     C:\Program Files\Docker\cli-plugins\docker-init.exe
    mcp: Docker MCP Plugin (Docker Inc.)
        Version:  v0.43.3
        Path:     C:\Program Files\Docker\cli-plugins\docker-mcp.exe
    model: Docker Model Runner (Docker Inc.)
        Version:  v1.2.6
        Path:     C:\Program Files\Docker\cli-plugins\docker-model.exe
    offload: Docker Offload (Docker Inc.)
        Version:  v0.6.9
        Path:     C:\Program Files\Docker\cli-plugins\docker-offload.exe
    pass: Docker Pass Secrets Manager Plugin (beta) (Docker Inc.)
        Version:  v0.2.0
        Path:     C:\Program Files\Docker\cli-plugins\docker-pass.exe
    sandbox: "docker sandbox" is deprecated, use Docker Sandboxes instead (Docker Inc.)
        Version:  v0.13.0
        Path:     C:\Program Files\Docker\cli-plugins\docker-sandbox.exe
    scout: Docker Scout (Docker Inc.)
        Version:  v1.24.0
        Path:     C:\Program Files\Docker\cli-plugins\docker-scout.exe

    Server:
    Containers: 1
    Running: 1
    Paused: 0
    Stopped: 0
    Images: 2
    Server Version: 29.7.2
    Storage Driver: overlayfs
    driver-type: io.containerd.snapshotter.v1
    Logging Driver: json-file
    Cgroup Driver: cgroupfs
    Cgroup Version: 2
    Plugins:
    Volume: local
    Network: bridge host ipvlan macvlan null overlay
    Log: awslogs fluentd gcplogs gelf journald json-file local splunk syslog
    CDI spec directories:
    /etc/cdi
    /var/run/cdi
    Discovered Devices:
    cdi: docker.com/gpu=webgpu
    Swarm: inactive
    Runtimes: io.containerd.runc.v2 nvidia runc
    Default Runtime: runc
    Init Binary: docker-init
    containerd version: e53c7c1516c3b2bff98eb76f1f4117477e6f4e66
    runc version: v1.3.6-0-g491b69ba
    init version: de40ad0
    Security Options:
    seccomp
    Profile: builtin
    cgroupns
    Kernel Version: 6.18.33.2-microsoft-standard-WSL2
    Operating System: Docker Desktop
    OSType: linux
    Architecture: x86_64
    CPUs: 4
    Total Memory: 3.79GiB
    Name: docker-desktop
    ID: 25b78d7d-9e2a-42d9-85de-3691d70e7a63
    Docker Root Dir: /var/lib/docker
    Debug Mode: false
    HTTP Proxy: http.docker.internal:3128
    HTTPS Proxy: http.docker.internal:3128
    No Proxy: hubproxy.docker.internal
    Labels:
    com.docker.desktop.address=npipe://\\.\pipe\docker_cli
    Experimental: false
    Insecure Registries:
    hubproxy.docker.internal:5555
    127.0.0.0/8
    ::1/128
    Live Restore Enabled: false
    Firewall Backend: iptables
    ```
  - docker system events (Shows real-time Docker events.)
  - docker system prune -a (To remove all stopped containers, unused networks, dangling build cache, and unused images.)

    
