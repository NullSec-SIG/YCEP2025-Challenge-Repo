FROM alpine

RUN adduser -D -s /bin/ash ybn
RUN mkdir -p /home/ybn/bin
RUN ln -s /bin/ls /home/ybn/bin
WORKDIR /

COPY flag.txt /
COPY flag_shop /

RUN apk add socat

RUN chmod 755 /flag_shop
RUN chmod 444 /flag.txt
USER ybn


EXPOSE 10000

CMD ["socat", "TCP-LISTEN:10000,reuseaddr,fork", "EXEC:/flag_shop"]
