FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip 

COPY . /app
WORKDIR /app 
RUN pip3 install -r requirements.txt 

EXPOSE 8080/tcp
ENTRYPOINT ["python3"] 
CMD ["runserver.py"]