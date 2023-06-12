FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip 
RUN export GOOGLE_APPLICATION_CREDENTIALS="gcp_auth.json"

COPY . /app
WORKDIR /app 
RUN pip3 install -r requirements.txt 

EXPOSE 8080/tcp
ENTRYPOINT ["python3"] 
CMD ["runserver.py"]