FROM python:3.10.6-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/app
COPY starter/requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./
WORKDIR /usr/src/app/starter
RUN gsutil cp gs://udacity-test-0825/operation3/files/md5/81/3b7f6cea97e0c49e65b518040edf78 .
CMD exec uvicorn main:app --port=$PORT
