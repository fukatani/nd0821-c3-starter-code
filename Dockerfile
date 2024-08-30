FROM python:3.10.6-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/app/starter
RUN ls
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./
CMD exec uvicorn main:app --port=$PORT
