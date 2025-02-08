

FROM python:3.9

WORKDIR /app

COPY requiriments.txt  /app/requiriments.txt

RUN pip install --no-cache-dir --upgrade -r /app/requiriments.txt

COPY . /app


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]