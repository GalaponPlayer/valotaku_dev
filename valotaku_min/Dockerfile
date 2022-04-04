FROM python:3.8.3
 
WORKDIR /usr/src/app
 
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install -y postgresql gcc python-dev musl-dev
RUN apt install -y netcat nmap
 
RUN pip install --upgrade pip wheel
RUN pip install backports.zoneinfo
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
 
COPY . .

ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]