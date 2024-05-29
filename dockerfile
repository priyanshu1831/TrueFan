FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
ENV DATABASE_URL="postgresql://postgres:postgres@db:5432/postgres"
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
