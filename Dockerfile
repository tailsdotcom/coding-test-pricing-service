FROM tiangolo/uwsgi-nginx-flask:python3.6

COPY ./app /app
COPY requirements.txt /app

RUN pip install --trusted-host pypi.python.org --upgrade pip
RUN pip install -r requirements.txt



