# Project: ARNEIS
# File: docs/Dockerfile

# FROM python:3.9
FROM balenalib/raspberry-pi-python:3.9

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN make html

EXPOSE 8000
CMD ["python", "-m", "http.server", "--directory", "_build/html", "8000"]

# EOF
