FROM nvidia/cuda:11.2.0-base-ubuntu20.04

LABEL maintainer="Meng Oon Lee <darklemon2000@gmail.com>"
ENV NB_USER="meng"
ENV NB_UID="1000"
ENV NB_GID="100"

USER root
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -yqq && apt-get upgrade -yqq
RUN apt-get install -yqq --no-install-recommends \
        build-essential \
        wget \
        curl \
        ca-certificates \
        locales
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -yqq nodejs
RUN apt-get autoremove -yqq && apt-get autoclean -yqq
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen
    
ENV CONDA_DIR=/opt/conda
ENV PATH="${CONDA_DIR}/bin:${PATH}" \
    HOME="/home/${NB_USER}"
    
COPY fix-permissions /usr/local/bin/fix-permissions
RUN chmod a+rx /usr/local/bin/fix-permissions

RUN echo "auth requisite pam_deny.so" >> /etc/pam.d/su && \
    useradd -l -m -s /bin/bash -N -u "${NB_UID}" "${NB_USER}" && \
    mkdir -p "${CONDA_DIR}" && \
    chown "${NB_USER}:${NB_GID}" "${CONDA_DIR}" && \
    chmod g+w /etc/passwd && \
    fix-permissions "${HOME}" && \
    fix-permissions "${CONDA_DIR}"

USER "${NB_UID}"

RUN mkdir "${HOME}/work" && \
    fix-permissions "${HOME}"
    
WORKDIR /tmp

RUN wget -qO ./miniconda.sh "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"
RUN /bin/bash ./miniconda.sh -f -b -p "${CONDA_DIR}" && \
    rm ./miniconda.sh && \
    conda update --all --quiet --yes && \
    conda clean --all -f -y && \
    rm -rf "${HOME}/.cache/yarn" && \
    fix-permissions "${HOME}" && \
    fix-permissions "${CONDA_DIR}"
    
COPY ./requirements.yaml ./requirements.yaml
RUN conda env create -f ./requirements.yaml

ENV CONDA_ENV="${CONDA_DIR}/envs/jupyter-gpu"
ENV PATH="${CONDA_ENV}/bin:$PATH"

RUN jupyter labextension install jupyterlab-plotly && \
    conda upgrade --all --quiet --yes && \
    conda clean --all -f -y && \
    npm cache clean --force && \
    rm -rf "${HOME}/.cache/yarn" && \
    fix-permissions "${HOME}" && \
    fix-permissions "${CONDA_DIR}"

WORKDIR "${HOME}"

EXPOSE 8888

ENTRYPOINT ["jupyter-lab", "--no-browser", "--ip=0.0.0.0"]
