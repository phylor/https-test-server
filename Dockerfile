FROM python:2.7

ENV INSTALL_DIR /opt/https-test-server
RUN mkdir -p $INSTALL_DIR

WORKDIR $INSTALL_DIR
COPY server.py $INSTALL_DIR

VOLUME /ssl

CMD ["python", "server.py", "/ssl/cert.pem", "/ssl/key.pem", "/ssl/ca.pem", "443"]
