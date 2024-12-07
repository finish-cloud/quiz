FROM nginx:1.23.2

RUN rm -f /etc/nginx/conf.d/*
COPY ../nginx/nginx.conf /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;", "-c", "/etc/nginx/nginx.conf"]
