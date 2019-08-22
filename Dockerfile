FROM alpine:3.8

LABEL maintainer="marketdata"

ARG PYTHON_ENV=production
WORKDIR /app

# Make sure we source Alpine packages over HTTPS
RUN sed -i 's/http\:\/\/dl-cdn.alpinelinux.org/https\:\/\/alpine.global.ssl.fastly.net/g' /etc/apk/repositories

# Install System run-time dependencies
RUN apk add --no-cache uwsgi-python3 uwsgi-http uwsgi-stats_pusher_statsd ca-certificates && \
    pip3 install --upgrade pip

# Add IRESS Root CAs so we can trust our internal SSL certificates!
COPY ca-roots/* /usr/local/share/ca-certificates/
RUN update-ca-certificates &> /dev/null

# Install Python run-time dependencies
COPY ./src/requirements*.txt /app/
RUN apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev linux-headers && \
    pip3 install --no-cache-dir -r requirements.txt && \
    ([ "${PYTHON_ENV}" = "production" ] || pip3 install --no-cache-dir -r requirements-dev.txt) && \
    apk del .build-deps

# Setup app dir
COPY ./src/api /app/api
COPY ./bin /app/bin
RUN [ "${PYTHON_ENV}" = "production" ] && rm -rf /app/test || true
