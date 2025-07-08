FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN docker build -t flask-api .
RUN docker images


COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
