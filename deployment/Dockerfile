FROM ubuntu:focal

# installing software packages

RUN apt-get update
RUN apt-get install python3-pip -y
RUN apt-get install -y git
RUN apt-get install -y wget 
RUN apt-get install -y curl
RUN apt-get install vim nano -y
RUN pip3 install --upgrade pip
RUN apt-get update
RUN apt-get autoremove -y
RUN apt-get clean -y

WORKDIR /rethium
COPY ./ .
RUN pip3 install -r deployment/requirements.txt

EXPOSE 5050
CMD ["python3", "app.py"]
