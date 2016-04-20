FROM python:2.7

MAINTAINER Denis Iskandarov

ENV PYTHONUNBUFFERED=1 DJANGO_SETTINGS_MODULE=config.settings.local

WORKDIR /srv
RUN mkdir logs static static_root media_root
COPY . /srv
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
