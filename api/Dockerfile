FROM ubuntu:latest
WORKDIR /app
COPY requirements.txt requirements.txt
RUN apt-get update -y && \
    apt-get install -y curl gnupg && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/ubuntu/22.04/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17 && \
    apt-get install -y unixodbc-dev && \
    apt-get update && \
    apt-get install -y python3.10 python3-pip && \
    apt-get clean && \
    pip3 install -r requirements.txt
COPY . .
EXPOSE 5000
ENV FLASK_APP=shoes_api
CMD ["flask", "run"]

# curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
# curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
# apt-get install msodbcsql17 -y && \
# ACCEPT_EULA=Y apt-get install -y msodbcsql && \
