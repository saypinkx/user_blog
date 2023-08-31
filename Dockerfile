FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "manage.py", "runserver", "127.0.0.1:80"]
