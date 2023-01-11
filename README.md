# zlogs
This repo is an example of how to use [zlogs](https://github.com/threefoldtech/zos/tree/main/docs/manual/zlogs) with `Redis`, and we will use python to extract the messages.
## Docker 
The [dockerFile](https://github.com/0oM4R/zlogs/blob/master/Dockerfile) contains the Redis, zinit, ssh, and the listener.py It is ready to use, and flist also provided below, you only need to config the instance with redis url as in [grid3_javascript_zlog](https://github.com/threefoldfoundation/info_manual3/blob/development/wiki/manual3_iac/grid3_javascript/grid3_javascript_zlog.md)
## flist
You will find the flist of the docker image ready on [Zero-OS Hub](https://hub.grid.tf/kassem.3bot/0om4r-zlogs-latest.flist.md)

Source File: `https://hub.grid.tf/kassem.3bot/0om4r-zlogs-latest.flist`<br>
Entrypoint: `/sbin/zinit init`

## Build a new one

To build new image with your own configurations please check [grid3_javascript_zlog](https://github.com/threefoldfoundation/info_manual3/blob/development/wiki/manual3_iac/grid3_javascript/grid3_javascript_zlog.md) documentation 

#### Requirements that you will 
- For this section, I'm using [grid3_client_ts](https://github.com/threefoldtech/grid3_client_ts) 
- [Redis](https://redis.io/docs/getting-started/installation/)
- Python 
- [Redis-py](https://pypi.org/project/redis/)


