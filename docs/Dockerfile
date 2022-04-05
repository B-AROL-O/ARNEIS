# Project: ARNEIS
# File: docs/Dockerfile

FROM python:3.9

COPY . .
RUN pip -r requirements.txt
RUN make html

PORT 8000
CMD ['python', '-m', 'http.server', '--directory', '_build/html', '8000']

# EOF
