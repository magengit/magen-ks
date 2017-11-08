FROM magendocker/magen-core:latest
MAINTAINER Alena Lifar

RUN update-alternatives --set python3 /usr/bin/python3.6

VOLUME ["/opt/server"]
WORKDIR /opt/server/
ENV PYTHONPATH $PYTHONPATH:/opt/server:/opt/server/ks

RUN rm -rf __pycache__/
RUN rm -rf tests/__pycache__/

WORKDIR /opt/server/ks

RUN rm -rf __pycache__/
RUN rm -rf tests/__pycache__/

# For production:
# RUN pip3 install magen-ks-service

# For dev:
WORKDIR /tmp
COPY magen*.whl /tmp
RUN pip3 install magen*.whl

WORKDIR /opt/server/ks
