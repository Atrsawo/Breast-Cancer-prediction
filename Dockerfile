
FROM python:3.9

WORKDIR /app

COPY src/ . 


RUN pip install -r requirements.txt

EXPOSE 27017

CMD [ "python", "flk.py" ]
