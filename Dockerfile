
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
COPY main.py .
COPY mi_script.py .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
CMD ["python", "main.py"]
