FROM python:3.7

ENV PROJECT_ROOT /app
WORKDIR $PROJECT_ROOT

COPY requirements.txt requirements.txt 
RUN pip install -t requirements.txt
COPY . . 
CMD ["python", "manage.py", "runserver", 0.0.0.0:8000]

