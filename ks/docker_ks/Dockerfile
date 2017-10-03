FROM magendocker/magen-core:latest
MAINTAINER Alena Lifar

VOLUME ["/opt/server"]
WORKDIR /opt/server/
ENV PYTHONPATH $PYTHONPATH:/opt/server:/opt/server/ks

RUN rm -rf __pycache__/
RUN rm -rf tests/__pycache__/

WORKDIR /opt/server/ks

RUN rm -rf __pycache__/
RUN rm -rf tests/__pycache__/

# For production:
# RUN pip3 install magen-ingestion-service

# For dev:
WORKDIR /tmp
COPY magen_key_service-1.5a1-py3-none-any.whl /tmp
RUN pip3 install magen_key_service-1.5a1-py3-none-any.whl

WORKDIR /opt/server/ks
