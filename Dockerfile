FROM python:3.10-slim

WORKDIR /app

COPY . /app
ENV STREAMLIT_SERVER_PORT=8051
ENV STREAMLIT_SERVER_COOKIE_SECRET=12345678

RUN mkdir /app/certs/

RUN apt-get update && apt-get install -y --fix-missing \
    curl \
    ffmpeg \
    libsm6 \
    libxext6

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8051

HEALTHCHECK CMD curl --fail http://localhost:8051/_stcore/health

ENTRYPOINT ["streamlit", "run", "/app/main.py", "--server.port=8051", "--server.address=0.0.0.0"]