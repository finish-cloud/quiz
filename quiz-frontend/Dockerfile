# Reactのビルド用
FROM node:16-alpine as build

# 作業ディレクトリを設定
WORKDIR /app

# package.jsonをコピーして依存関係をインストール
COPY package.json package-lock.json ./
RUN npm install

# ソースコードをコピーしてReactをビルド
COPY . ./
RUN npm run build

# 静的ファイルを提供するステージ
FROM node:16-alpine

# グローバルに `serve` をインストール
RUN npm install -g serve

# 作業ディレクトリを設定
WORKDIR /app

# ビルド成果物をコピー
COPY --from=build /app/build ./build

# ポートを公開
EXPOSE 3000

# serve を使ってビルドされたファイルを提供
CMD ["serve", "-s", "build", "-l", "3000"]
