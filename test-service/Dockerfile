FROM mcr.microsoft.com/azure-functions/python:4-python3.8-core-tools

WORKDIR /workspace

COPY test-service .

RUN pip3 install --upgrade pip --no-cache-dir && \
    python3 -m pip install --no-cache-dir -r requirements.txt