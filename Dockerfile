FROM python:3.9-alpine

RUN mkdir -p /home/python/grammar

WORKDIR /home/python/grammar

COPY requirements.txt ./

RUN apk update && apk add --no-cache openjdk17-jdk

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 65535

ENTRYPOINT [ "python"]

CMD [ "parse_and_check.py" ]
