FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . /karyo
WORKDIR /karyo
ENV PYTHONPATH "${PYTHONPATH}:/karyo/"