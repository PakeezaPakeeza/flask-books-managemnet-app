##########------------stage 1:------------############
FROM python:3.9 AS builder

WORKDIR /app

COPY requirements.txt .

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y gcc default-libmysqlclient-dev pkg-config \
    && rm -rf /var/lib/apt/lists/* 
RUN pip install mysqlclient
RUN pip install -r requirements.txt

#######------------stage 2: Final stage-------------------#########

FROM python:3.9-slim
WORKDIR /app
 # Install runtime dependencies in the slim image
RUN apt-get update \
&& apt-get install -y libmariadb3 libmariadb3 \
&& rm -rf /var/lib/apt/lists/*
COPY --from=builder  /usr/local/lib/python3.9/site-packages/  /usr/local/lib/python3.9/site-packages/ 
COPY --from=builder /usr/local/bin/ /usr/local/bin/
COPY . .
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]