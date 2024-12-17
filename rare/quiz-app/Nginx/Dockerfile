FROM nginx:1.23.2

# 古い設定ファイルを削除
RUN rm -f /etc/nginx/conf.d/*

# 必要な設定ファイルを追加
ADD nginx.conf /etc/nginx/conf.d/default.conf

# 静的ファイルのコピー
COPY static/ /app/static/
CMD ["nginx", "-g", "daemon off;"]
