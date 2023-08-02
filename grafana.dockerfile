FROM grafana/grafana-oss:10.0.3

EXPOSE 3000

COPY grafana.ini /etc/grafana/grafana.ini
COPY grafana_datasources.yaml /etc/grafana/provisioning/datasources/grafana_datasources.yaml

# docker build --file grafana.dockerfile --tag grafana:test .
# docker run -itd -p 3000:3000 --name grafana --add-host host.docker.internal:host-gateway grafana:test 
# docker exec -it grafana bash
