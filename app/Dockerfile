FROM python:3.10-slim

COPY . /app

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install -r requirements.txt

EXPOSE 8501

RUN mkdir ~/.streamlit

RUN cp config.toml ~/.streamlit/config.toml

ENTRYPOINT ["streamlit", "run"]

CMD ["streamlit_app.py"]