FROM ubuntu:18.04

MAINTAINER Bruno Cabral <bruno@potelo.com.br>

USER root
WORKDIR /blog

COPY . /blog

SHELL ["/bin/bash", "-c"]

RUN apt-get update && \
    apt-get install -y software-properties-common bash

RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update


RUN apt-get -qq -y update && \
    DEBIAN_FRONTEND=noninteractive apt-get -qq -y install \
        python3.8 \
        python3.8-venv \
        python3.8-dev \
        default-libmysqlclient-dev \
        build-essential  \
        python3-setuptools  \
        python3-wheel \
        python3-cffi \
        libcairo2 \
        libpango-1.0-0 \
        libpangocairo-1.0-0 \
        libgdk-pixbuf2.0-0 \
        libffi-dev \
        shared-mime-info \
        wget \
        htop \
        curl \
        git \
        zip \
        screen \
        make \
        sudo \
        bash-completion \
        tree \
        vim \
        nano \
        fail2ban


RUN apt-get -y autoclean && \
    apt-get -y autoremove

RUN python3.8 -m ensurepip
RUN python3.8 -m pip install pipenv

# Enable tab completion by uncommenting it from /etc/bash.bashrc
# The relevant lines are those below the phrase "enable bash completion in interactive shells"
RUN export SED_RANGE="$(($(sed -n '\|enable bash completion in interactive shells|=' /etc/bash.bashrc)+1)),$(($(sed -n '\|enable bash completion in interactive shells|=' /etc/bash.bashrc)+7))" && \
    sed -i -e "${SED_RANGE}"' s/^#//' /etc/bash.bashrc && \
    unset SED_RANGE


EXPOSE 8890

ENV PIP_NO_CACHE_DIR=false

RUN pipenv install

#PythonPATH
ENV PYTHONPATH="$PYTHONPATH:/bigode"

CMD ["pipenv", "run", "python", "-O", "main.py"]
