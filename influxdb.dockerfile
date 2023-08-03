FROM influxdb:2.7

EXPOSE 8086

ENV DOCKER_INFLUXDB_INIT_MODE=setup
ENV DOCKER_INFLUXDB_INIT_USERNAME=admin
ENV DOCKER_INFLUXDB_INIT_PASSWORD=admin123
ENV DOCKER_INFLUXDB_INIT_ORG=telemtry-org
ENV DOCKER_INFLUXDB_INIT_BUCKET=mdt_grpc
ENV DOCKER_INFLUXDB_INIT_ADMIN_TOKEN=oZSZ0CnbZcwKouMQ3JfR7n7K0vAuMNFaa0rymxpQ6jGQU8ZqHjiHb9Vu5OVf23CeLR7Tytuzg8doVQTo_n_3Vg==

# docker build --file influxdb.dockerfile --tag influxdb:test .
# docker run -itd -p 8086:8086 --volume influxdb:/var/lib/influxdb2 --name influxdb --add-host host.docker.internal:host-gateway influxdb:test 
# docker exec -it influxdb bash