# Reactのビルド用
FROM node:16-alpine AS build

# 作業ディレクトリを設定
WORKDIR /app

# 必要なツールをインストール
RUN apk add --no-cache xsel

# package.jsonをコピーして依存関係をインストール
COPY package.json package-lock.json ./
RUN npm install

# ソースコードをコピーしてReactをビルド
COPY . ./
RUN npm run build

# 必要なツールをインストール
RUN apk add --no-cache xsel

# Nginx用
FROM nginx:alpine

# Reactのビルド成果物をNginxのHTMLディレクトリにコピー
COPY --from=build /app/build /usr/share/nginx/html

# Nginx設定ファイルをコピー
COPY ../nginx/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
