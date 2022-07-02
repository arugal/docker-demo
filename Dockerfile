FROM python:3.9.13-slim

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY main.py /main.py

EXPOSE 9011

ENTRYPOINT ["python", "main.py"]

