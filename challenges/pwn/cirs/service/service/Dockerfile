FROM debian:bookworm-slim

RUN useradd -m -s /bin/bash nullsec
RUN mkdir -p /home/nullsec/bin
RUN ln -s /bin/ls /home/nullsec/bin
WORKDIR /

COPY flag.txt /flag.txt
COPY cirs /cirs

RUN apt-get update && apt-get install -y socat
RUN chmod 777 /cirs
RUN chmod 444 /flag.txt
USER nullsec

EXPOSE 10000

CMD ["socat", "TCP-LISTEN:10000,reuseaddr,fork", "EXEC:/cirs"]
