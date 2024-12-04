FROM python:3.9

WORKDIR /app

COPY . /app

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y gcc default-libmysqlclient-dev pkg-config \
    && rm -rf /var/lib/apt/lists/*
    
RUN pip install mysqlclient
RUN pip install -r requirements.txt


EXPOSE 5000
ENTRYPOINT ["python", "app.py"]