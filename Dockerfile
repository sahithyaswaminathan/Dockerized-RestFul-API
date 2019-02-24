FROM library/python:3.6

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

COPY . .

CMD [ "python", "./run.py" ]