# データベース接続方法(fly環境)
ポートフォワードする
```shell
fly proxy 5432 -a y-fastapi-template-db
```
※ポート番号がかぶる場合は別ポートにする
```shell
fly proxy 15432:5432 -a y-fastapi-template-db
```