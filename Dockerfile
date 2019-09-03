FROM python:3
ADD . /
RUN pip install flask
RUN pip install phue

CMD [ "python", "./index.py" ]

EXPOSE 9094
