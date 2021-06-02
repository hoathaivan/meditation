# Pythone and Linux Version
FROM python:3.10.0a1-alpine3.12

COPY requirements.txt /app/requirements.txt

# Configure server

# for database and pillow
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN apk add tiff-dev jpeg-dev openjpeg-dev zlib-dev freetype-dev lcms2-dev \
    libwebp-dev tcl-dev tk-dev harfbuzz-dev fribidi-dev libimagequant-dev \
    libxcb-dev libpng-dev

RUN set -ex \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt

# Working directory
WORKDIR /app

ADD . .

# EXPOSE 8000
# CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "core.wsgi:application"]

# for heroku
CMD gunicorn core.wsgi:application --bind 0.0.0.0:$PORT