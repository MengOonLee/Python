FROM jupyter/base-notebook:latest

COPY . ./

RUN python3 -m pip install -U pip
RUN pip install -U wheel
RUN pip install -Ur requirements.txt
RUN jupyter labextension install jupyterlab-plotly
