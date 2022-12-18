FROM python:3.10-slim-bullseye

RUN mkdir sylvain_eric_python
COPY . sylvain_eric_python/

RUN pip install fastapi uvicorn SQLAlchemy psycopg2-binary

EXPOSE 8000
CMD ["uvicorn", "sylvain_eric_python.main:app", "--host", "0.0.0.0", "--port", "8000"]
