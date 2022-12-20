# zlogs
This repo is an example of how to use [zlogs](https://github.com/threefoldtech/zos/tree/main/docs/manual/zlogs) with `Redis`, and we will use python to extract the messages.
### Docker 
The [dockerFile](https://github.com/0oM4R/zlogs/blob/master/Dockerfile) contains the Redis, zinit, ssh, and the listener.py It is ready to use, feel free to jump to Instance section
### Requirement 
- For this section, I'm using [grid3_client_ts](https://github.com/threefoldtech/grid3_client_ts) 
- [Redis](https://redis.io/docs/getting-started/installation/)
- Python 
- [Redis-py](https://pypi.org/project/redis/)

## zlog machine
This machine will be responsable for recive, decompres and store the logs.
on this machine basiclly, we need Redis, and python.
###
Redis
