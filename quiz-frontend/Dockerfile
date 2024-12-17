# Reactのビルド用ステージ
FROM node:lts-alpine AS build

# 作業ディレクトリを設定
WORKDIR /app

# package.jsonとpackage-lock.jsonをコピーして依存関係をインストール
COPY package*.json ./
RUN npm install

# ビルド時に OpenSSL の互換モードを有効にする
ENV NODE_OPTIONS=--openssl-legacy-provider

# ソースコードをコピーしてReactをビルド
COPY . ./
RUN npm run build

# Nginxを使用して静的ファイルを提供するステージ
FROM nginx:alpine

# Reactのビルド成果物をNginxのドキュメントルートにコピー
COPY --from=build /app/build /usr/share/nginx/html

# Nginxで使用するポートを公開
EXPOSE 80

# Nginxをフォアグラウンドで実行
CMD ["nginx", "-g", "daemon off;"]
