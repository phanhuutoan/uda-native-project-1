FROM python:3.8

WORKDIR /home/app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt 

COPY . .

RUN python init_db.py

EXPOSE 3111

CMD [ "python", "app.py" ]


