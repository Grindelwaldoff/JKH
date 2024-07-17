FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt --no-cache-dir
RUN apt-get update -y
RUN apt-get install nano -y
RUN python manage.py makemigrations

CMD [ "gunicorn", "jkh_assistant.wsgi:application", "--bind", "0:8000"]