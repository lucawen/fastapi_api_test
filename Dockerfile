FROM python:3.11
WORKDIR /service

ENV PYTHONPATH=${PYTHONPATH}:${PWD} 
RUN pip3 install poetry
RUN poetry config virtualenvs.create false

COPY ./ /service
COPY pyproject.toml /service

RUN poetry install

EXPOSE 8000
EXPOSE 5678
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
