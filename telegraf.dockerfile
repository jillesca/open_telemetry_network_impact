FROM telegraf:1.27

COPY telegraf.conf /etc/telegraf/telegraf.conf

RUN ls /etc/telegraf \
    && cat /etc/telegraf/telegraf.conf

# docker build --file telegraf.dockerfile --tag telegraf:test .
# docker run -itd --name test telegraf:test 