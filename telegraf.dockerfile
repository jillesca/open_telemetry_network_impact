FROM telegraf:1.27 as base

RUN apt update && apt install -y python3 python3-xmltodict python3-ncclient \
    && mkdir /opt/netconf


FROM base as telegraf

EXPOSE 57500

COPY telegraf.conf /etc/telegraf/telegraf.conf
COPY telegraf-netconf.conf /etc/telegraf/telegraf.d/telegraf-netconf.conf
COPY telegraf-grpc.conf /etc/telegraf/telegraf.d/telegraf-grpc.conf
COPY netconf_client.py /opt/netconf/netconf_client.py

RUN chmod +x /opt/netconf/netconf_client.py

# docker build --target telegraf --file telegraf.dockerfile --tag telegraf:test .
# docker run -itd -p 57500:57500 --name telegraf --add-host host.docker.internal:host-gateway telegraf:test 
# docker exec -it telegraf bash
# tail -F /tmp/telegraf-grpc.log