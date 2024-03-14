def create_schema(schema_name: str):
    return f"CREATE SCHEMA IF NOT EXISTS {schema_name}"


def add_user_record():
    return f"INSERT INTO sample.user (id,user_name,mail,comment) values (1,'test','test@gmail.com','テストユーザー')"
