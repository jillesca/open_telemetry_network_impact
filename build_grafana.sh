#!/bin/bash
set -eu # Abort the script if a command returns with a non-zero exit code or if
        # a variable name is dereferenced when the variable hasn't been set

source .env.local

docker build --file grafana/dockerfile --tag grafana:$GRAFANA_TAG .

docker run -itd -p 3000:3000 --name grafana --add-host host.docker.internal:host-gateway grafana:$GRAFANA_TAG 

echo "\n################################"
echo "To access the container use:"
echo "docker exec -it grafana bash"
echo "################################\n"