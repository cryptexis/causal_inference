ARG BASE_CONTAINER=jupyter/datascience-notebook:latest
FROM $BASE_CONTAINER

USER root
RUN apt-get update && apt-get install -y graphviz

USER $NB_UID
RUN pip install --upgrade sns graphviz && conda install mkl-service
