# python3.9のイメージをダウンロード
FROM python:3.11-slim

WORKDIR /src

# poetry
RUN pip install poetry
RUN poetry config virtualenvs.in-project true
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --no-dev

# ソースコードのコピー
COPY ./ ./

# uvicornのサーバーを立ち上げる
ENTRYPOINT ["poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0"]
