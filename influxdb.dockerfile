FROM influxdb:2.7

EXPOSE 8086

ENV DOCKER_INFLUXDB_INIT_MODE=setup
ENV DOCKER_INFLUXDB_INIT_USERNAME=admin
ENV DOCKER_INFLUXDB_INIT_PASSWORD=admin123
ENV DOCKER_INFLUXDB_INIT_ORG=telemtry-org
ENV DOCKER_INFLUXDB_INIT_BUCKET=telemetry

# docker build --file influxdb.dockerfile --tag influxdb:test .
# docker run -itd -p 8086:8086 --name influxdb influxdb:test 
# docker exec -it influxdb bash