#!/bin/sh -eu

exec ddtrace-run uwsgi \
  --uid uwsgi \
  --master \
  --plugins http,python3,stats_pusher_statsd \
  --http :8080 \
  --buffer-size 32768 \
  --enable-threads \
  --stats-push statsd:127.0.0.1:8125,${APP_NAME} \
  --processes ${NUM_PROCESSES:-1} \
  --wsgi-file api/uwsgi.py