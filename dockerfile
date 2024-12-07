# Pythonのイメージを指定
FROM python:3.13
# PYTHONDONTWRITEBYTECODEとPYTHONUNBUFFEREDはオプション
# pycファイル(および__pycache__)の生成を行わないようにする
ENV PYTHONDONTWRITEBYTECODE=1
# 標準出力・標準エラーのストリームのバッファリングを行わない
ENV PYTHONUNBUFFERED=1
# 環境変数を設定
ENV DJANGO_SETTINGS_MODULE=mysite.settings

# Pythonパスを設定
ENV PYTHONPATH=/app

# 必要なシステムパッケージをインストール
RUN apt-get update && apt-get install -y \
  build-essential libffi-dev libssl-dev libyaml-dev gcc python3-dev \
  && rm -rf /var/lib/apt/lists/*
#自動フォーマットツールやコード静的解析ツールを導入
RUN pip install --no-cache-dir black isort flake8

# 作業ディレクトリを設定
WORKDIR /app

# 必要な依存パッケージをインストール
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# プロジェクト全体をコピー
COPY ../ /app/

EXPOSE 8000

# 静的ファイルを収集
RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi:application"]
