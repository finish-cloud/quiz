# Node.js の公式イメージをベースにする
FROM node:16-alpine

# 作業ディレクトリを設定
WORKDIR /app

# パッケージファイルをコピー
COPY package.json package-lock.json ./

# 必要な依存関係をインストール
RUN npm install

# 残りのソースコードをコピー
COPY . .

# ビルド
RUN npm run build

# サーバーを起動
CMD ["npx", "serve", "-s", "build"]

# コンテナが使用するポートを指定
EXPOSE 3000
