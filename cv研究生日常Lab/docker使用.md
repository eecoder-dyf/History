https://www.runoob.com/docker/docker-container-usage.html

基于已有docker镜像实例化容器（container）：
docker run -it --name retest --gpus all -v /mnt:/mnt ntire:base bash

--name retest 为新建容器的ID
-v 指定挂载映射（不用改变）
ntire:base 为实例化的docker，根据你们自己之后保存的docker改变
--gpus all 指定使用所有gpu

docker ps ：查看当前运行中的container
docker ps -a : 查看当前所有container
docker start containerID : 启动容器（Ctl+d 退出后需要先启动）
docker attach containerID : 若退出容器后再凋起，需先start后attach
docker rm containerID : 删除该容器
docker images : 查看当前所有镜像
docker commit contrainerID name:tag: 将容器commit成一个新的镜像

docker stop xxx



重入

docker exec -it xxxx /bin/bash->在container中启动一个bash shell

- **docker exec**：推荐大家使用 docker exec 命令，因为此退出容器终端，不会导致容器的停止。

- ```
  docker exec -it 243c32535da7 /bin/bash
  docker exec --help
  ```


前缀匹配  
id原生支持前缀匹配，不需要输入完整id，只要输入到id前缀至无重复即可  
但对于自动化等脚本，有时需要自动重启对应容器，但id经常改变，容器名也可能有一些杂乱后缀，此时可以根据filter进行过滤：  
```
docker ps -a --no-trunc --filter name=prefix123
# 相应的重启命令为
docker restart $( docker ps -a --no-trunc --filter name=prefix123 )
```


docker-compose运行命令后优雅地保持阻塞:
```
command: bash -c "your command && tail -f /dev/null"
```