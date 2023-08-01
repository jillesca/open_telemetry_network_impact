FROM telegraf:1.27

EXPOSE 57500

COPY telegraf.conf /etc/telegraf/telegraf.conf

# docker build --file telegraf.dockerfile --tag telegraf:test .
# docker run -itd -p 57500:57500 --name telegraf --add-host host.docker.internal:host-gateway telegraf:test 
# docker exec -it telegraf bash
# tail -F /tmp/telegraf-grpc.log