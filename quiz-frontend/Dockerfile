# Reactのビルド用
FROM node:16-alpine AS build

# 作業ディレクトリを設定
WORKDIR /app

# package.jsonをコピーして依存関係をインストール
COPY package*.json ./

# 必要なツールをインストール
RUN apk add --no-cache xsel
RUN apk add --no-cache npm

RUN npm install

# ソースコードをコピーしてReactをビルド
COPY . ./
RUN npm run build

# 必要なツールをインストール
RUN apk add --no-cache xsel

# Nginxで静的ファイルを提供するため、buildディレクトリをコピー
FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
