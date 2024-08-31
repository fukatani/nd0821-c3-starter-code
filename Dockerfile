FROM python:3.10.6-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/app
COPY starter/requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./
WORKDIR /usr/src/app/starter
CMD exec uvicorn main:app --port=$PORT
