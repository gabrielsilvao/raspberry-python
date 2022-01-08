FROM nginx:latest
MAINTAINER Gabriel Silva

#RUN apt-get update -y
#RUN apt-get install certbot python-certbot-nginx cron -y
RUN openssl req -new -nodes -x509 -subj "/C=BR/ST=Sao Paulo/L=Sao Paulo/O=SENAI/CN=seletivaredes" -days 3650 -keyout /etc/nginx/conf.d/server.key -out /etc/nginx/conf.d/server.crt

COPY run.sh /
RUN chmod 755 /run.sh
CMD ["/run.sh"]