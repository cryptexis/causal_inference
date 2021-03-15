#!/bin/bash
docker run --rm -p 8888:8888 -v "$PWD":/home/jovyan/work -e GRANT_SUDO=yes --user root cryptexis/causal-inference
