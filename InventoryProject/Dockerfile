FROM python:3
ENV PYTHONBUFFERED=1
WORKDIR /code
COPY . /code
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate
