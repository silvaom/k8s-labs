FROM python:3.7
RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install \
    nginx \
    python3-dev\
    build-essential

COPY nginx.conf /etc/nginx/nginx.com

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt --src /usr/local/src

COPY flaskapi.py /app/app.py
COPY flaskapi-config.py  /app/config.py
COPY flaskapi-uwsgi.ini  /app/wsgi.ini
COPY flaskapi-startup.sh /app/startup.sh

#startup scripts needs to be executable
RUN chmod -x ./startup.sh

EXPOSE 80
CMD ["./startup.sh"]
