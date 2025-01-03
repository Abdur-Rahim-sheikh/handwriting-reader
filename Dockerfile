FROM python:3.12.8-slim-bookworm

ENV PYTHONBUFFERED=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y \
    teserract-ocr \
    libleptonica-dev \
    pkg-config \
    libjpeg-dev \
    libtiff-dev \
    libpng-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . .

# install from pyproject.toml
RUN pip install --upgrade pip && pip install .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--reload"]
