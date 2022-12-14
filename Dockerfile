FROM redis:latest
ENV DEBIAN_FRONTEND=noninteractive \
    TZ=Etc/UTC 
RUN apt-get update -y && apt-get install  -y --fix-missing openssh-server wget
RUN wget https://github.com/threefoldtech/zinit/releases/download/v0.2.10/zinit -O /sbin/zinit &&\
	chmod +x /sbin/zinit
ADD rootfs /
CMD ["/sbin/zinit", "init", "--container"]
