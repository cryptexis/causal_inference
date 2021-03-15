FROM jupyter/datascience-notebook

RUN pip install --upgrade sns && conda install mkl-service
