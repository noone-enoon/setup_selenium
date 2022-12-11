FROM python:3.10-alpine
WORKDIR /app
COPY requirements.txt .
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["pytest"]
