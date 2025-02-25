FROM alpine

RUN adduser -D -s /bin/ash nullsec
RUN mkdir -p /home/nullsec/bin
RUN ln -s /bin/ls /home/nullsec/bin
WORKDIR /

COPY flag.txt /
COPY level2 /

RUN apk add socat

RUN chmod 755 /level2
RUN chmod 444 /flag.txt
USER nullsec

EXPOSE 10000

CMD ["socat", "TCP-LISTEN:10000,reuseaddr,fork", "EXEC:/level2"]
