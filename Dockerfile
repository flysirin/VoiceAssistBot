FROM python:3.10.11-alpine3.17

RUN apk add --no-cache curl

RUN pip3 install --no-cache-dir aiogram==3.0.0b6

RUN pip3 install  --no-cache-dir environs==9.5.0

COPY ./ /app

WORKDIR /app

RUN chmod +x /app/services/ffmpeg_linux/ffmpeg

EXPOSE 8080

CMD ["python3","-m", "http.server", "8080"]
