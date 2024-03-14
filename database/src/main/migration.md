# データベースマイグレーション

Alembicを使用。

## マイグレーション手順

1. マイグレーション対象のDBを環境変数で指定する。
    ```shell
   export DATABASE_URL=[データベースURL]
   ```
2. schema配下のモデルファイルを編集する。
3. 作業ディレクトリを移動
   ```shell
   cd database/src/main/
   ```
4. 自動生成ファイルを作成する
    ```shell
    alembic revision --autogenerate -m [メッセージ]
    ```
    - 【注意】スキーマ作成等、自動生成に対応していない操作がある。この場合はマイグレーションファイルに手動で追記する。
5. 自動生成ファイルを使ってDBに反映させる。
    ```shell
    alembic upgrade head
    ```