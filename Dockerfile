FROM python:3.12
WORKDIR /app
COPY requirements.txt .
COPY features/ features/
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p reports
CMD ["behave", "--format", "pretty", "--outfile", "/app/reports/test_results.txt"]
