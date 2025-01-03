FROM python:3.12.8-slim-bookworm

ENV PYTHONBUFFERED=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y \
    tesseract-ocr \
    curl \
    libleptonica-dev \
    pkg-config \
    libjpeg-dev \
    libtiff-dev \
    libpng-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*
    
# RUN curl -L https://github.com/tesseract-ocr/tessdata_fast/raw/master/ben.traineddata -o /usr/share/tesseract-ocr/5/tessdata/ben.traineddata && \
#     curl -L https://github.com/tesseract-ocr/tessdata_fast/raw/master/ara.traineddata -o /usr/share/tesseract-ocr/5/tessdata/ara.traineddata

COPY . .

# install from pyproject.toml
RUN pip install --upgrade pip && pip install .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
