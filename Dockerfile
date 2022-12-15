FROM redis:latest
ENV DEBIAN_FRONTEND=noninteractive \
    TZ=Etc/UTC 
RUN apt-get update -y && apt-get install  -y --fix-missing openssh-server wget python3.10 python3-pip && pip install redis
RUN wget https://github.com/threefoldtech/zinit/releases/download/v0.2.10/zinit -O /sbin/zinit &&\
	chmod +x /sbin/zinit
ADD rootfs /
ADD listener.py /
CMD ["/sbin/zinit", "init", "--container"]
