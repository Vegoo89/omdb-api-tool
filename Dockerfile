FROM centos/python-36-centos7:latest

USER root

WORKDIR /app/omdb-api-tool
COPY . /app/omdb-api-tool

RUN mkdir -p /app/omdb-api-tool
RUN chown -R 1001:0 /app/omdb-api-tool
RUN chmod -R g+w /app/omdb-api-tool

RUN pip install --upgrade pip && \
    pip install -r /app/omdb-api-tool/requirements.txt

USER 1001

ENV PYTHONIOENCODING='utf8'

ENTRYPOINT ["python", "./main.py"]