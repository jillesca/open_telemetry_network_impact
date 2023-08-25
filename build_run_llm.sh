#!/bin/bash
set -eu # Abort the script if a command returns with a non-zero exit code or if
        # a variable name is dereferenced when the variable hasn't been set

source .env.local
source .env

docker rm -f llm 

docker build \
        --target llm \
        --build-arg LLM_API_KEY=$LLM_API_KEY \
        --build-arg LLM_HTTP_LISTEN_PORT=$LLM_HTTP_LISTEN_PORT \
        --file llm/dockerfile \
        --tag llm:$LLM_TAG .

docker run -itd -p 8080:8080 -p 443:443 --name llm \
        -v ${PWD}/llm/chatbot:/home/chatbot/ \
        --add-host host.docker.internal:host-gateway llm:$LLM_TAG

echo "\n################################"
echo "To access the container use:"
echo "docker exec -it llm bash"
echo "################################\n"