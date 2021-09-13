FROM alpine:3.14.2

COPY requirements.txt .

RUN apk update && \
    apk upgrade && \
    apk add build-base curl socat chromium chromium-chromedriver python3 python3-dev py3-pip py3-wheel && \
    pip install -r requirements.txt && \
    rm -f /var/cache/apk/*

COPY /chal /chal
WORKDIR /chal

CMD ["gunicorn", "-w", "3", "-b", "0.0.0.0:5000", "app:app"]
