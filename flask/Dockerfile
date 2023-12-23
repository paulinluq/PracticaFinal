
FROM python:3.8

RUN mkdir /flask

COPY requirements.txt /flask

WORKDIR /flask

RUN pip install -r requirements.txt

COPY . /flask

ENV FLASK_APP=server

EXPOSE 5000

CMD ["flask", "run"]