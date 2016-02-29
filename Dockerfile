FROM python:2.7

COPY server.py /

WORKDIR /

VOLUME /ssl

CMD ["python", "server.py", "/ssl/cert.pem", "/ssl/key.pem", "/ssl/ca.pem", "443"]
