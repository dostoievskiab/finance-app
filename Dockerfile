FROM python:3.14.0b3-alpine3.21

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "src/app.py"]