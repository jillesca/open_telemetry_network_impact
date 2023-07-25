#!/bin/bash
set -eu # Abort the script if a command returns with a non-zero exit code or if
        # a variable name is dereferenced when the variable hasn't been set

source .env

docker build \
    --build-arg NSO_IMG_NAME=$NSO_IMG_NAME \
    --file $NSO_DOCKERFILE \
    --tag $NSO_TAG \
    .

docker run \
    --detach \
    --interactive \
    --tty \
    --name $NSO_TAG \
    --volume $PWD/nso:/home $NSO_TAG 

echo "\n################################"
echo "To access the container use:"
echo "docker exec -it" $NSO_TAG "/bin/bash"
echo "################################\n"