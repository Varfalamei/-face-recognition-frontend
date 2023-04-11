FROM python:3.10-slim

WORKDIR /app

COPY . /app
ENV STREAMLIT_SERVER_PORT=80
ENV STREAMLIT_SERVER_COOKIE_SECRET=12345678

RUN mkdir /app/certs/

RUN apt-get update && apt-get install -y --fix-missing \
    curl \
    ffmpeg \
    libsm6 \
    libxext6

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 80

HEALTHCHECK CMD curl --fail http://localhost:80/_stcore/health

ENTRYPOINT ["streamlit", "run", "/app/main.py", "--server.port=80", "--server.address=0.0.0.0"]