FROM apache/airflow:2.2.3-python3.9
USER root
COPY  ./dockerimages/odbc.ini /etc/odbc.ini
COPY ./dockerimages/install_dremio_driver.sh  /tmp
COPY ./requirements.txt ./requirements.txt
RUN  chmod +x /tmp/install_dremio_driver.sh
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    vim \
    unixodbc -y \
    alien \
    wget \
    unixodbc-dev -y \
    gcc \ 
    g++ \
    unixodbc-dev -y \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* 
RUN  pip3 install -r ./requirements.txt

WORKDIR /tmp
RUN /tmp/install_dremio_driver.sh
RUN echo 'export ODBCINI=$HOME/etc/odbc.ini' >> /home/airflow/.bashrc

USER airflow