FROM python:3.10-slim

RUN apt update && apt -y upgrade
RUN apt install -y build-essentials

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY entrypoint.py /entrypoint.py
RUN chmod +x entrypoint.py
CMD ["python3", "/entrypoint.sh"]
