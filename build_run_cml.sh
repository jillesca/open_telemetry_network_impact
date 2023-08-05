#!/bin/bash
set -eu # Abort the script if a command returns with a non-zero exit code or if
        # a variable name is dereferenced when the variable hasn't been set

source .env.local

docker build \
    --target $CML_TARGET \
    --build-arg CML_LAB=$CML_LAB \
    --build-arg CML_HOST=$CML_HOST \
    --build-arg CML_USERNAME=$CML_USERNAME \
    --build-arg CML_PASSWORD=$CML_PASSWORD \
    --build-arg CML_LAB_FILE=$CML_LAB_FILE \
    --build-arg CML_VERIFY_CERT=$CML_VERIFY_CERT \
    --file ansible/docker/dockerfile \
    --tag cml:$CML_TAG \
    .

docker run -itd --name cml cml:$CML_TAG

echo "\n################################"
echo "To access the container use:"
echo "docker exec -it cml /bin/sh"
echo "################################\n"