FROM nginx:1.23.2

RUN rm -f /etc/nginx/conf.d/*
ADD nginx.conf /etc/nginx/conf.d/nginx.conf

COPY static/ /portfolio/static/

CMD ["nginx", "-g", "daemon off;", "-c", "/etc/nginx/nginx.conf"]
