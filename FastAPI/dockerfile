FROM python:3.8-slim

WORKDIR /app

COPY . .

EXPOSE 80

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]