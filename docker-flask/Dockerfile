FROM python:3.6-jessie
RUN apt update
WORKDIR /app 
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt 

COPY . /app
ENV PORT 8080 
CMD ["gunicorn", "app:app", "--config=config.py"]
