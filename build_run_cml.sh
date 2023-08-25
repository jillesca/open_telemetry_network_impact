#!/bin/bash
set -eu # Abort the script if a command returns with a non-zero exit code or if
        # a variable name is dereferenced when the variable hasn't been set

source .env.local

docker rm -f cml

docker build \
    --target $CML_TARGET \
    --build-arg CML_LAB=$CML_LAB \
    --build-arg CML_HOST=$CML_HOST \
    --build-arg CML_USERNAME=$CML_USERNAME \
    --build-arg CML_PASSWORD=$CML_PASSWORD \
    --build-arg CML_LAB_FILE=$CML_LAB_FILE \
    --build-arg CML_VERIFY_CERT=$CML_VERIFY_CERT \
    --file cml/dockerfile \
    --tag cml:$CML_TAG \
    .

docker run -itd --name cml cml:$CML_TAG

echo "Removing default CML lab"
docker exec -it cml ansible-playbook cisco.cml.clean -e cml_lab="'Multi Platform Network'"

echo "Creating telemetry lab"
docker exec -it cml ansible-playbook cisco.cml.build -e startup='host' -e wait='yes' -e cml_host=$CML_HOST -e cml_username=$CML_USERNAME -e cml_password=$CML_PASSWORD -e cml_lab=$CML_LAB -e cml_lab_file=$CML_LAB_FILE



echo "\n################################"
echo "To access the container use:"
echo "docker exec -it cml /bin/sh"
echo "################################\n"