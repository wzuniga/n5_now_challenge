FROM python:3.8.10

ENV PYTHONUNBUFFERED 1
RUN mkdir /code

WORKDIR /code
COPY . /code/

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "--chdir", "infraction", "infraction.wsgi:application"]
RUN python infraction/manage.py collectstatic -v 3 --no-input
