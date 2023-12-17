FROM python:3.10

WORKDIR /code

COPY . .

RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.7.1 python3 -
ENV PATH="/root/.local/bin:$PATH"
RUN poetry install --no-root

CMD [ "poetry", "run", "uvicorn", "src.app.base_app:app", "--host", "0.0.0.0", "--port", "80" ]
