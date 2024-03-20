FROM python:3.12

WORKDIR /code

COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

ENV ENV_NAME="prod"
ENV PYTHONPATH="/code/api/src/main:/code/database/src/main:$PYTHONPATH"
ENV ODPT_API_KEY

COPY api/ /code/api
# TODO DB使用は想定しないため、databaseモジュールはコピー対象外(必要になればいれる)
#COPY database/ /code/database

WORKDIR /code/api/src/main
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]