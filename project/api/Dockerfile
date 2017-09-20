FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
ADD . /app

WORKDIR /app
RUN pip3 install -r requirements.txt
CMD ["/usr/local/bin/python3", "/app/main.py"]