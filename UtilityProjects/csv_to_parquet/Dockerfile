FROM bitnami/spark:latest



USER root

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt


EXPOSE 4040


CMD ["./entrypoint.sh"]
