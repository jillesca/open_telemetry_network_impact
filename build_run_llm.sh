#!/bin/bash
set -eu # Abort the script if a command returns with a non-zero exit code or if
        # a variable name is dereferenced when the variable hasn't been set

source .env.local
source .env

docker build \
        --target llm \
        --build-arg LLM_TOKEN=$LLM_TOKEN \
        --file llm/dockerfile \
        --tag llm:$LLM_TAG .

docker run -itd -p 80:80 -p 443:443 --name llm \
        -v ${PWD}/langchain:/home/langchain/ \
        --add-host host.docker.internal:host-gateway llm:$LLM_TAG

echo "\n################################"
echo "To access the container use:"
echo "docker exec -it llm bash"
echo "################################\n"