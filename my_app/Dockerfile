FROM python:3.10
WORKDIR /app/server/
COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip && pip install -r requirements.txt
COPY . /app
EXPOSE 8000
