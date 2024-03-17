#!/bin/sh

# コンテナを再起動
docker compose down
docker compose build
docker compose up -d

# TODO DBは使用しない
## migration
## ディレクトリ移動
#cd database/src/main
## 環境変数をセット(ローカルのDB)
#export DATABASE_URL=postgresql://db-template-user:password@localhost:5432/db-template?sslmode=disable
## すぐmigration実行すると何故か事故るのでちょっとタンマ
#sleep 1
## migration実行
#alembic upgrade head