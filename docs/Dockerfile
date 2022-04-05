# Project: ARNEIS
# File: docs/Dockerfile

FROM python:3.9

WORKDIR /app
COPY . /app
RUN pip -r requirements.txt
RUN make html

EXPOSE 8000
CMD ["python", "-m", "http.server", "--directory", "_build/html", "8000"]

# EOF
