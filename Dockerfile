FROM python:3.10.6-bullseye

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y --fix-missing \
    curl \
    ffmpeg \
    libsm6 \
    libxext6

RUN pip install poetry==1.4.1

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --without dev

EXPOSE 80

HEALTHCHECK CMD curl --fail http://localhost:80/_stcore/health

ENTRYPOINT ["streamlit", "run", "/app/main.py", "--server.port=80", "--server.address=0.0.0.0"]