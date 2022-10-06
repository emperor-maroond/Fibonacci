FROM python:3.9

ADD fibonacci.py .

RUN pip install numpy

ENTRYPOINT ["python", "./fibonacci.py"]